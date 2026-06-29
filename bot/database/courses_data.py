COURSES = {
    "python": {
        "title": "🐍 Python Dasturlash",
        "description": "Python - bu eng mashhur va oson o'rganiladigan dasturlash tili. Uni o'rganib sun'iy intellekt, veb-saytlar va botlar yaratishingiz mumkin.",
        "steps": [
            {
                "id": "py_intro",
                "title": "Python Kirish va O'rnatish",
                "content": (
                    "📝 *Qadam 1: Python nima?*\n\n"
                    "Python - sodda sintaksisga ega bo'lgan kuchli til. Uni o'rganishni quyidagi amallardan boshlang:\n\n"
                    "1️⃣ Python rasmiy saytidan (python.org) dasturni yuklab oling va o'rnating.\n"
                    "2️⃣ O'rnatish oynasida 'Add Python to PATH' tugmasini bosishni unutmang.\n"
                    "3️⃣ VS Code yoki PyCharm muharririni o'rnating.\n\n"
                    "🔗 Batafsil o'rganish uchun video darslik: https://youtube.com/playlist?list=PLwGpS7yM9SjdmjR6sVfK0V7kM748HuxaP"
                )
            },
            {
                "id": "py_variables",
                "title": "O'zgaruvchilar va Ma'lumot turlari",
                "content": (
                    "📝 *Qadam 2: O'zgaruvchilar va Ma'lumot turlari*\n\n"
                    "Python-da ma'lumotlarni saqlash uchun o'zgaruvchilar ishlatiladi.\n\n"
                    "• `name = \"Ali\"` - matn (string)\n"
                    "• `age = 15` - butun son (integer)\n"
                    "• `height = 1.75` - o'nlik son (float)\n"
                    "• `is_student = True` - mantiqiy qiymat (boolean)\n\n"
                    "💡 *Amaliy topshiriq:* O'zingiz haqingizdagi ma'lumotlarni o'zgaruvchilarga saqlang va `print(name, age)` yordamida ekranga chiqaring."
                )
            },
            {
                "id": "py_conditions",
                "title": "Shart Operatorlari (if-elif-else)",
                "content": (
                    "📝 *Qadam 3: Dasturni boshqarish (Shartlar)*\n\n"
                    "Shart operatorlari dasturni ma'lum shartlar asosida ishlashiga yordam beradi.\n\n"
                    "```python\n"
                    "yosh = 15\n"
                    "if yosh >= 18:\n"
                    "    print(\"Siz voyaga yetgansiz\")\n"
                    "else:\n"
                    "    print(\"Siz hali voyaga yetmagansiz\")\n"
                    "```\n\n"
                    "💡 *Amaliy topshiriq:* Foydalanuvchidan bal ko'rsatkichini so'rab, uning bahosini chiqaruvchi dastur yozing (masalan, 90 dan yuqori bo'lsa 'A')."
                )
            }
        ]
    },
    "figma": {
        "title": "🎨 Figma Dizayn",
        "description": "Figma - bu veb-saytlar va mobil ilovalar dizaynini yaratish uchun eng yetakchi onlayn grafik muharrir.",
        "steps": [
            {
                "id": "figma_intro",
                "title": "Figma Interfeysi va Frame bilan ishlash",
                "content": (
                    "📝 *Qadam 1: Figma nima va u bilan ishlash*\n\n"
                    "Figma orqali siz brauzerning o'zida zamonaviy UI/UX dizaynlar chizishingiz mumkin.\n\n"
                    "1️⃣ figma.com saytida ro'yxatdan o'ting.\n"
                    "2️⃣ Yangi loyiha oching (`Drafts -> New design file`).\n"
                    "3️⃣ `Frame` asbobini (F harfi) tanlab, ekran o'lchamini (masalan, iPhone 14) tanlang.\n\n"
                    "🔗 Figma darsligi (boshlang'ich): https://youtube.com/playlist?list=PL_XfE2c1Z8QyC74eZtG932N46lBqXk6v5"
                )
            },
            {
                "id": "figma_shapes",
                "title": "Shakllar, Ranglar va Matnlar",
                "content": (
                    "📝 *Qadam 2: Shakllar va Vizual elementlar*\n\n"
                    "Dizayn asosi shakllar va matnlardan iborat:\n\n"
                    "• R (Rectangle) - To'rtburchak chizish\n"
                    "• O (Ellipse) - Doira chizish\n"
                    "• T (Text) - Matn yozish\n\n"
                    "💡 *Dizayn qoidasi:* Bir ekranda 3 tadan ko'p rang yoki shrift ishlatmaslikka harakat qiling. Bu dizaynning toza va professional ko'rinishini ta'minlaydi."
                )
            },
            {
                "id": "figma_project",
                "title": "Birinchi Tugma va Interaktivlik",
                "content": (
                    "📝 *Qadam 3: Tugma (Button) chizish va Auto Layout*\n\n"
                    "Auto Layout Figmaning eng kuchli asboblaridan biri bo'lib, elementlarni avtomatik joylashtirishni ta'minlaydi.\n\n"
                    "1️⃣ Matn yozing (masalan, 'Kirish').\n"
                    "2️⃣ Shift + A tugmalarini bosib Auto Layout qo'shing.\n"
                    "3️⃣ Atrofini rang bilan to'ldiring (Fill) va chetlarini yumaloqlang (Corner radius: 8px).\n\n"
                    "🎉 Tabriklaymiz, siz birinchi tugmangizni tayyorladingiz!"
                )
            }
        ]
    },
    "ai": {
        "title": "🤖 Sun'iy Intellekt (AI)",
        "description": "Sun'iy intellektdan (ChatGPT, Midjourney) unumli foydalanish va to'g'ri 'prompt' (buyruq) berishni o'rganing.",
        "steps": [
            {
                "id": "ai_intro",
                "title": "Neyrotarmoqlar va Prompt Engineering",
                "content": (
                    "📝 *Qadam 1: Prompt nima va u qanday ishlaydi?*\n\n"
                    "Prompt - bu sun'iy intellektga beriladigan aniq ko'rsatma yoki buyruq.\n\n"
                    "AI sizga eng yaxshi javobni berishi uchun unga 3 ta narsani bering:\n"
                    "1️⃣ *Rol:* Unga kasb bering (Masalan: 'Sen tajribali ingliz tili o'qituvchisisan').\n"
                    "2️⃣ *Vazifa:* Nima qilish kerakligini ayting (Masalan: 'Menga 5 ta yangi so'zni tushuntir').\n"
                    "3️⃣ *Format:* Qanday shaklda chiqarib bersin (Masalan: 'Jadval shaklida, o'zbekcha tarjimasi bilan')."
                )
            },
            {
                "id": "ai_chatgpt",
                "title": "ChatGPT-dan o'quv jarayonida foydalanish",
                "content": (
                    "📝 *Qadam 2: ChatGPT orqali o'rganish*\n\n"
                    "ChatGPT nafaqat savollarga javob beradi, balki shaxsiy repetitor ham bo'la oladi.\n\n"
                    "💡 *Foydali prompt:* \n"
                    "_\"Menga Pythondagi 'list' mavzusini 12 yoshli bolaga tushuntirgandek sodda misollar bilan tushuntirib ber.\"_\n\n"
                    "Ushbu so'rov orqali murakkab mavzularni juda oson o'rganishingiz mumkin."
                )
            },
            {
                "id": "ai_images",
                "title": "AI tasvirlar yaratish (Midjourney/DALL-E)",
                "content": (
                    "📝 *Qadam 3: Rasmlar generatsiyasi*\n\n"
                    "Matn orqali ajoyib rasmlar yaratuvchi neyrotarmoqlar bilan ishlash qoidalari:\n\n"
                    "• Tasvir ob'ektini batafsil yozing.\n"
                    "• Uslubni (style) ko'rsating: 3D render, digital art, realistic, pixel art.\n"
                    "• Rangi va yoritilishini belgilang.\n\n"
                    "💡 *Prompt misoli:* `A cute futuristic robot programming on a laptop, 3D render, vibrant colors, dark background`."
                )
            }
        ]
    }
}
