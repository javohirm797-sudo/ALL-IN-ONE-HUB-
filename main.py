import asyncio
import logging
import sys

from aiogram import Bot, Dispatcher
from aiogram.client.default import DefaultBotProperties
from aiogram.enums import ParseMode

from bot.config import settings
from bot.database.connection import init_db
from bot.handlers.common import router as common_router
from bot.handlers.education import router as education_router

async def on_startup(bot: Bot):
    # Initialize database and tables
    logging.info("Initializing database tables...")
    await init_db()
    logging.info("Database initialized successfully.")

async def main():
    # Setup logging
    logging.basicConfig(
        level=logging.INFO,
        format="%(asctime)s - %(name)s - %(levelname)s - %(message)s",
        handlers=[
            logging.StreamHandler(sys.stdout)
        ]
    )

    # Initialize Bot
    # Note: Default parsing mode is Markdown
    bot = Bot(
        token=settings.bot_token,
        default=DefaultBotProperties(parse_mode=ParseMode.MARKDOWN)
    )

    # Initialize Dispatcher
    dp = Dispatcher()

    # Register routers
    dp.include_router(common_router)
    dp.include_router(education_router)

    # Register startup callback
    dp.startup.register(on_startup)

    logging.info("Starting bot polling...")
    try:
        await dp.start_polling(bot)
    finally:
        await bot.session.close()

if __name__ == "__main__":
    asyncio.run(main())
