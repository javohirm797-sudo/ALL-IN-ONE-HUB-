from sqlalchemy.ext.asyncio import create_async_engine, async_sessionmaker, AsyncSession
from bot.config import settings
from bot.database.base import Base

# Connection arguments (e.g. for SQLite)
connect_args = {}
if settings.database_url.startswith("sqlite"):
    connect_args["check_same_thread"] = False

engine = create_async_engine(
    settings.database_url,
    connect_args=connect_args,
    echo=False
)

AsyncSessionLocal = async_sessionmaker(
    bind=engine,
    class_=AsyncSession,
    expire_on_commit=False
)

async def init_db():
    async with engine.begin() as conn:
        # This will create tables defined in models.py if they don't exist
        await conn.run_sync(Base.metadata.create_all)
