from aiogram import Router, F
from aiogram.filters import CommandStart
from aiogram.types import Message
from bot.keyboards.reply import get_main_menu_keyboard
from bot.database.connection import AsyncSessionLocal
from bot.database.crud import get_or_create_user, get_user_stats

router = Router()

@router.message(CommandStart())
async def cmd_start(message: Message):
    # Register/Get User in Database
    async with AsyncSessionLocal() as session:
        await get_or_create_user(
            session=session,
            telegram_id=message.from_user.id,
            username=message.from_user.username,
            full_name=message.from_user.full_name
        )
        
    welcome_text = (
        "✨ *All-In-One Hub* Telegram platformasiga xush kelibsiz!\n\n"
        "Ushbu platforma 10 yoshdan 20 yoshgacha bo‘lgan yoshlarning ta’lim olish, "
        "texnologiyalar bilan ishlash va hordiq chiqarish bo‘yicha kundalik ehtiyojlarini "
        "bitta bot ichida birlashtiradi.\n\n"
        "🚀 *Asosiy imkoniyatlar:*\n"
        "1️⃣ *IT va Ta’lim markazi:* Dasturlash, Figma dizayn va AI bo'yicha bosqichma-bosqich o‘quv yo‘l xaritalari (Roadmap).\n"
        "2️⃣ *O‘yinlar va Kibersport:* Ommabop o‘yinlar (CS2, MLBB, Standoff 2) bo'yicha yangiliklar va foydali promo-kodlar.\n"
        "3️⃣ *Kreativ vositalar (Tools):* Kontent yaratuvchilar uchun matn yozuvchi, rasmni qayta ishlovchi AI asboblar.\n"
        "4️⃣ *Premium:* Telegram Stars orqali eksklyuziv darslar va yopiq guruhlar.\n\n"
        "Quyidagi menyu orqali kerakli bo'limni tanlang 👇"
    )
    
    await message.answer(
        text=welcome_text,
        parse_mode="Markdown",
        reply_markup=get_main_menu_keyboard()
    )

@router.message(F.text == "👤 Mening Profilim")
async def show_profile(message: Message):
    async with AsyncSessionLocal() as session:
        user = await get_or_create_user(
            session=session,
            telegram_id=message.from_user.id,
            username=message.from_user.username,
            full_name=message.from_user.full_name
        )
        stats = await get_user_stats(session, user.telegram_id)
        
    status = "⭐ Premium" if user.is_premium else "📝 Oddiy foydalanuvchi"
    
    profile_text = (
        "👤 *Foydalanuvchi Profili*\n\n"
        f"👤 *Ism:* {user.full_name or 'Noma`lum'}\n"
        f"🆔 *Telegram ID:* `{user.telegram_id}`\n"
        f"🌐 *Username:* @{user.username or 'yo`q'}\n"
        f"📅 *Ro'yxatdan o'tilgan sana:* {user.registered_at.strftime('%d.%m.%Y %H:%M')}\n"
        f"🏷 *Status:* {status}\n\n"
        f"🏆 *O'quv ko'rsatkichlari (Roadmap):*\n"
        f"🔹 Jami yakunlangan darslar: *{stats['total_completed']}* ta\n"
        f"  - 🐍 Python: {stats['course_stats'].get('python', 0)} ta\n"
        f"  - 🎨 Figma: {stats['course_stats'].get('figma', 0)} ta\n"
        f"  - 🤖 AI: {stats['course_stats'].get('ai', 0)} ta"
    )
    
    await message.answer(text=profile_text, parse_mode="Markdown")

@router.message(F.text == "🎮 O'yinlar va Kibersport")
async def show_games_module(message: Message):
    text = (
        "🎮 *O‘yinlar va Kibersport zonasi*\n\n"
        "Bu bo'lim orqali siz yaqin kunlarda:\n"
        "• CS2, Standoff 2 va Mobile Legends o'yinlarining so'nggi yangiliklari;\n"
        "• Skinlar narxini kuzatish tizimi;\n"
        "• Eksklyuziv promo-kodlar bazasidan foydalana olasiz.\n\n"
        "⏳ _Ushbu modul hozirda loyihalashtirilmoqda va keyingi yangilanishlarda taqdim etiladi!_"
    )
    await message.answer(text=text, parse_mode="Markdown")

@router.message(F.text == "🛠 Kreativ Vositalar (AI)")
async def show_tools_module(message: Message):
    text = (
        "🛠 *Kreativ vositalar (Tools)*\n\n"
        "Bu bo'lim orqali blogerlar va ijodkorlar uchun:\n"
        "• AI yordamida matnlar yozish (Copywriting);\n"
        "• Rasmlarni qayta ishlash va generatsiya qilish;\n"
        "• Videolarni tahrirlash bo'yicha yordamchi asboblar ishga tushadi.\n\n"
        "⏳ _Modul tez orada faollashtiriladi!_"
    )
    await message.answer(text=text, parse_mode="Markdown")

@router.message(F.text == "⭐ Premium va Monetizatsiya")
async def show_premium_module(message: Message):
    text = (
        "⭐ *Premium va Monetizatsiya (Telegram Stars)*\n\n"
        "Tez orada ushbu bo'limda siz:\n"
        "• Telegram Stars orqali yopiq o'quv guruhlariga a'zo bo'lish;\n"
        "• Murakkab amaliy loyihalarning to'liq kodlarini xarid qilish;\n"
        "• Mutaxassislardan individual konsultatsiyalar olishingiz mumkin bo'ladi.\n\n"
        "💳 _Hozircha tizim test bosqichida va yaqin orada ishga tushadi!_"
    )
    await message.answer(text=text, parse_mode="Markdown")
