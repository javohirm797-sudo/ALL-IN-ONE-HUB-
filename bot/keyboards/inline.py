from aiogram.types import InlineKeyboardMarkup, InlineKeyboardButton

def get_courses_keyboard() -> InlineKeyboardMarkup:
    buttons = [
        [InlineKeyboardButton(text="🐍 Python Dasturlash", callback_data="course:python")],
        [InlineKeyboardButton(text="🎨 Figma Dizayn", callback_data="course:figma")],
        [InlineKeyboardButton(text="🤖 Sun'iy Intellekt (AI)", callback_data="course:ai")],
    ]
    return InlineKeyboardMarkup(inline_keyboard=buttons)

def get_roadmap_keyboard(course_id: str, step_index: int, total_steps: int, is_completed: bool) -> InlineKeyboardMarkup:
    buttons = []
    
    # Completion/Status button
    if not is_completed:
        buttons.append([
            InlineKeyboardButton(text="✅ Qadamni tugatdim", callback_data=f"roadmap_complete:{course_id}:{step_index}")
        ])
    else:
        buttons.append([
            InlineKeyboardButton(text="🎉 Bajarildi! (Qayta yuklash 🔄)", callback_data=f"roadmap_reset:{course_id}:{step_index}")
        ])
        
    # Navigation row
    nav_row = []
    if step_index > 0:
        nav_row.append(InlineKeyboardButton(text="◀️ Oldingi", callback_data=f"roadmap_nav:{course_id}:{step_index-1}"))
    if step_index < total_steps - 1:
        nav_row.append(InlineKeyboardButton(text="Keyingi ▶️", callback_data=f"roadmap_nav:{course_id}:{step_index+1}"))
        
    if nav_row:
        buttons.append(nav_row)
        
    # Utility row
    buttons.append([
        InlineKeyboardButton(text="📋 Qadamlar ro'yxati", callback_data=f"roadmap_list:{course_id}"),
        InlineKeyboardButton(text="⬅️ Kurslarga qaytish", callback_data="courses_list")
    ])
    
    return InlineKeyboardMarkup(inline_keyboard=buttons)

def get_roadmap_steps_list_keyboard(course_id: str, steps: list, completed_step_ids: set) -> InlineKeyboardMarkup:
    buttons = []
    for idx, step in enumerate(steps):
        status_icon = "✅" if step["id"] in completed_step_ids else "⏳"
        buttons.append([
            InlineKeyboardButton(text=f"{status_icon} {idx+1}. {step['title']}", callback_data=f"roadmap_nav:{course_id}:{idx}")
        ])
        
    buttons.append([InlineKeyboardButton(text="⬅️ Orqaga", callback_data=f"course:{course_id}")])
    return InlineKeyboardMarkup(inline_keyboard=buttons)
