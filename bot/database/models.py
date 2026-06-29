from datetime import datetime
from sqlalchemy import BigInteger, String, DateTime, Boolean, ForeignKey, Integer, UniqueConstraint
from sqlalchemy.orm import Mapped, mapped_column, relationship
from bot.database.base import Base

class User(Base):
    __tablename__ = "users"

    telegram_id: Mapped[int] = mapped_column(BigInteger, primary_key=True)
    username: Mapped[str | None] = mapped_column(String(100), nullable=True)
    full_name: Mapped[str | None] = mapped_column(String(200), nullable=True)
    registered_at: Mapped[datetime] = mapped_column(DateTime, default=datetime.utcnow)
    language: Mapped[str] = mapped_column(String(10), default="uz")
    is_premium: Mapped[bool] = mapped_column(Boolean, default=False)

    progress: Mapped[list["UserProgress"]] = relationship(
        "UserProgress", back_populates="user", cascade="all, delete-orphan"
    )

    def __repr__(self) -> str:
        return f"<User {self.telegram_id} ({self.username or self.full_name})>"

class UserProgress(Base):
    __tablename__ = "user_progress"

    id: Mapped[int] = mapped_column(Integer, primary_key=True, autoincrement=True)
    telegram_id: Mapped[int] = mapped_column(BigInteger, ForeignKey("users.telegram_id", ondelete="CASCADE"), nullable=False)
    course_id: Mapped[str] = mapped_column(String(50), nullable=False)
    step_id: Mapped[str] = mapped_column(String(50), nullable=False)
    completed_at: Mapped[datetime] = mapped_column(DateTime, default=datetime.utcnow)

    user: Mapped["User"] = relationship("User", back_populates="progress")

    __table_args__ = (
        UniqueConstraint("telegram_id", "course_id", "step_id", name="uq_user_course_step"),
    )

    def __repr__(self) -> str:
        return f"<UserProgress user={self.telegram_id} course={self.course_id} step={self.step_id}>"
