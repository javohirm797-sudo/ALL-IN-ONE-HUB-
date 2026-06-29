from aiogram import Router, F
from aiogram.types import Message, CallbackQuery
from bot.keyboards.inline import (
    get_courses_keyboard,
    get_roadmap_keyboard,
    get_roadmap_steps_list_keyboard
)
from bot.database.courses_data import COURSES
from bot.database.connection import AsyncSessionLocal
from bot.database.crud import (
    get_completed_step_ids,
    mark_step_completed,
    reset_step_completed
)

router = Router()

@router.message(F.text == "💻 IT va Ta'lim")
async def show_education_menu(message: Message):
    text = (
        "💻 *IT va Ta'lim markaziga xush kelibsiz!*\n\n"
        "Bu yerda siz dasturlash, dizayn va sun'iy intellektdan samarali foydalanishni "
        "o'rganishingiz mumkin. O'zingiz qiziqqan yo'nalishni tanlang va qadam-baqadam "
        "yo'l xaritasi (Roadmap) orqali bilimingizni oshiring:\n\n"
        "Quyidagi kurslardan birini tanlang 👇"
    )
    await message.answer(
        text=text,
        parse_mode="Markdown",
        reply_markup=get_courses_keyboard()
    )

@router.callback_query(F.data == "courses_list")
async def process_courses_list(callback: CallbackQuery):
    text = (
        "💻 *IT va Ta'lim yo'nalishlari:*\n\n"
        "O'rganishni istagan yo'nalishingizni tanlang 👇"
    )
    await callback.message.edit_text(
        text=text,
        parse_mode="Markdown",
        reply_markup=get_courses_keyboard()
    )
    await callback.answer()

@router.callback_query(F.data.startswith("course:"))
async def process_course_detail(callback: CallbackQuery):
    course_id = callback.data.split(":")[1]
    course = COURSES.get(course_id)
    
    if not course:
        await callback.answer("Kurs topilmadi ❌", show_alert=True)
        return
        
    text = (
        f"🎯 *{course['title']}*\n\n"
        f"{course['description']}\n\n"
        f"📋 Ushbu kursda jami *{len(course['steps'])}* ta o'quv bosqichlari mavjud.\n"
        f"Boshlash uchun quyidagi tugmani bosing 👇"
    )
    
    # Inline buttons for starting roadmap
    from aiogram.types import InlineKeyboardMarkup, InlineKeyboardButton
    keyboard = InlineKeyboardMarkup(inline_keyboard=[
        [InlineKeyboardButton(text="🚀 O'rganishni boshlash (Roadmap)", callback_data=f"roadmap_nav:{course_id}:0")],
        [InlineKeyboardButton(text="⬅️ Kurslarga qaytish", callback_data="courses_list")]
    ])
    
    await callback.message.edit_text(text=text, parse_mode="Markdown", reply_markup=keyboard)
    await callback.answer()

@router.callback_query(F.data.startswith("roadmap_nav:"))
async def process_roadmap_nav(callback: CallbackQuery):
    _, course_id, step_index_str = callback.data.split(":")
    step_index = int(step_index_str)
    
    course = COURSES.get(course_id)
    if not course or step_index < 0 or step_index >= len(course["steps"]):
        await callback.answer("Bosqich topilmadi ❌", show_alert=True)
        return
        
    step = course["steps"][step_index]
    
    async with AsyncSessionLocal() as session:
        completed_step_ids = await get_completed_step_ids(session, callback.from_user.id, course_id)
        
    is_completed = step["id"] in completed_step_ids
    status_emoji = "✅ Bajarilgan" if is_completed else "⏳ Bajarilmoqda"
    
    text = (
        f"📖 *{course['title']}* — _Bosqich {step_index + 1}/{len(course['steps'])}_\n"
        f"📌 *Mavzu:* {step['title']}\n"
        f"⚙️ *Holat:* {status_emoji}\n\n"
        f"{step['content']}"
    )
    
    keyboard = get_roadmap_keyboard(
        course_id=course_id,
        step_index=step_index,
        total_steps=len(course["steps"]),
        is_completed=is_completed
    )
    
    await callback.message.edit_text(text=text, parse_mode="Markdown", reply_markup=keyboard, disable_web_page_preview=True)
    await callback.answer()

@router.callback_query(F.data.startswith("roadmap_complete:"))
async def process_roadmap_complete(callback: CallbackQuery):
    _, course_id, step_index_str = callback.data.split(":")
    step_index = int(step_index_str)
    
    course = COURSES.get(course_id)
    if not course or step_index < 0 or step_index >= len(course["steps"]):
        await callback.answer("Bosqich topilmadi ❌", show_alert=True)
        return
        
    step = course["steps"][step_index]
    
    async with AsyncSessionLocal() as session:
        marked = await mark_step_completed(session, callback.from_user.id, course_id, step["id"])
        completed_step_ids = await get_completed_step_ids(session, callback.from_user.id, course_id)
        
    if marked:
        await callback.answer("🎉 Qadam yakunlandi! Rivojlanishda davom eting! 💪", show_alert=True)
    else:
        await callback.answer("Bu qadam allaqachon bajarilgan.")
        
    # Re-render current page
    status_emoji = "✅ Bajarilgan"
    text = (
        f"📖 *{course['title']}* — _Bosqich {step_index + 1}/{len(course['steps'])}_\n"
        f"📌 *Mavzu:* {step['title']}\n"
        f"⚙️ *Holat:* {status_emoji}\n\n"
        f"{step['content']}"
    )
    
    keyboard = get_roadmap_keyboard(
        course_id=course_id,
        step_index=step_index,
        total_steps=len(course["steps"]),
        is_completed=True
    )
    
    await callback.message.edit_text(text=text, parse_mode="Markdown", reply_markup=keyboard, disable_web_page_preview=True)

@router.callback_query(F.data.startswith("roadmap_reset:"))
async def process_roadmap_reset(callback: CallbackQuery):
    _, course_id, step_index_str = callback.data.split(":")
    step_index = int(step_index_str)
    
    course = COURSES.get(course_id)
    if not course or step_index < 0 or step_index >= len(course["steps"]):
        await callback.answer("Bosqich topilmadi ❌", show_alert=True)
        return
        
    step = course["steps"][step_index]
    
    async with AsyncSessionLocal() as session:
        await reset_step_completed(session, callback.from_user.id, course_id, step["id"])
        
    await callback.answer("🔄 Qadam holati qayta tiklandi.", show_alert=False)
    
    # Re-render current page
    status_emoji = "⏳ Bajarilmoqda"
    text = (
        f"📖 *{course['title']}* — _Bosqich {step_index + 1}/{len(course['steps'])}_\n"
        f"📌 *Mavzu:* {step['title']}\n"
        f"⚙️ *Holat:* {status_emoji}\n\n"
        f"{step['content']}"
    )
    
    keyboard = get_roadmap_keyboard(
        course_id=course_id,
        step_index=step_index,
        total_steps=len(course["steps"]),
        is_completed=False
    )
    
    await callback.message.edit_text(text=text, parse_mode="Markdown", reply_markup=keyboard, disable_web_page_preview=True)

@router.callback_query(F.data.startswith("roadmap_list:"))
async def process_roadmap_list(callback: CallbackQuery):
    course_id = callback.data.split(":")[1]
    course = COURSES.get(course_id)
    
    if not course:
        await callback.answer("Kurs topilmadi ❌", show_alert=True)
        return
        
    async with AsyncSessionLocal() as session:
        completed_step_ids = await get_completed_step_ids(session, callback.from_user.id, course_id)
        
    text = (
        f"📋 *{course['title']} — O'quv Rejasi (Mundarija)*\n\n"
        "Quyida kursning barcha qadamlari ro'yxati ko'rsatilgan. "
        "Istagan qadamingizga bosib, darsni davom ettirishingiz mumkin:\n\n"
        "✅ - Bajarilgan qadam\n"
        "⏳ - Bajarilmagan qadam"
    )
    
    keyboard = get_roadmap_steps_list_keyboard(
        course_id=course_id,
        steps=course["steps"],
        completed_step_ids=completed_step_ids
    )
    
    await callback.message.edit_text(text=text, parse_mode="Markdown", reply_markup=keyboard)
    await callback.answer()
