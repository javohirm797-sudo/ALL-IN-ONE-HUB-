from datetime import datetime
from sqlalchemy import select, func, delete
from sqlalchemy.ext.asyncio import AsyncSession
from bot.database.models import User, UserProgress

async def get_or_create_user(
    session: AsyncSession,
    telegram_id: int,
    username: str | None = None,
    full_name: str | None = None
) -> User:
    # Search for user
    stmt = select(User).where(User.telegram_id == telegram_id)
    result = await session.execute(stmt)
    user = result.scalar_one_or_none()

    if not user:
        # Create new user if not found
        user = User(
            telegram_id=telegram_id,
            username=username,
            full_name=full_name,
            language="uz"
        )
        session.add(user)
        await session.commit()
    else:
        # Update details if changed
        updated = False
        if user.username != username:
            user.username = username
            updated = True
        if user.full_name != full_name:
            user.full_name = full_name
            updated = True
        
        if updated:
            await session.commit()
            
    return user

async def get_completed_step_ids(
    session: AsyncSession,
    telegram_id: int,
    course_id: str
) -> set[str]:
    stmt = select(UserProgress.step_id).where(
        UserProgress.telegram_id == telegram_id,
        UserProgress.course_id == course_id
    )
    result = await session.execute(stmt)
    return set(result.scalars().all())

async def mark_step_completed(
    session: AsyncSession,
    telegram_id: int,
    course_id: str,
    step_id: str
) -> bool:
    # Check if already completed
    stmt = select(UserProgress).where(
        UserProgress.telegram_id == telegram_id,
        UserProgress.course_id == course_id,
        UserProgress.step_id == step_id
    )
    result = await session.execute(stmt)
    progress = result.scalar_one_or_none()

    if not progress:
        progress = UserProgress(
            telegram_id=telegram_id,
            course_id=course_id,
            step_id=step_id
        )
        session.add(progress)
        await session.commit()
        return True
    return False

async def reset_step_completed(
    session: AsyncSession,
    telegram_id: int,
    course_id: str,
    step_id: str
) -> bool:
    stmt = delete(UserProgress).where(
        UserProgress.telegram_id == telegram_id,
        UserProgress.course_id == course_id,
        UserProgress.step_id == step_id
    )
    result = await session.execute(stmt)
    await session.commit()
    return result.rowcount > 0

async def get_user_stats(
    session: AsyncSession,
    telegram_id: int
) -> dict:
    # Total progress count
    stmt = select(func.count(UserProgress.id)).where(UserProgress.telegram_id == telegram_id)
    result = await session.execute(stmt)
    completed_count = result.scalar() or 0
    
    # Progress by course
    stmt_courses = select(UserProgress.course_id, func.count(UserProgress.id)).where(
        UserProgress.telegram_id == telegram_id
    ).group_by(UserProgress.course_id)
    result_courses = await session.execute(stmt_courses)
    course_stats = {row[0]: row[1] for row in result_courses.all()}
    
    return {
        "total_completed": completed_count,
        "course_stats": course_stats
    }
