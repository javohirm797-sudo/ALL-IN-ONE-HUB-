from aiogram.types import ReplyKeyboardMarkup, KeyboardButton

def get_main_menu_keyboard() -> ReplyKeyboardMarkup:
    kb = [
        [
            KeyboardButton(text="💻 IT va Ta'lim"),
            KeyboardButton(text="🎮 O'yinlar va Kibersport")
        ],
        [
            KeyboardButton(text="🛠 Kreativ Vositalar (AI)"),
            KeyboardButton(text="⭐ Premium va Monetizatsiya")
        ],
        [
            KeyboardButton(text="👤 Mening Profilim")
        ]
    ]
    return ReplyKeyboardMarkup(
        keyboard=kb,
        resize_keyboard=True,
        placeholder="Bo'limni tanlang..."
    )
