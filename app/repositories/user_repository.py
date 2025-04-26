from sqlalchemy import select

from app.database import async_session_maker
from app.models.user_model import UserProfile


class UserRepository:

    async def get_by_id(self, user_id: int) -> UserProfile | None:
        async with async_session_maker() as session:
            query = select(UserProfile).where(UserProfile.id == user_id)
            user = await session.execute(query)
            return user.scalar_one_or_none()

    async def create_user(self, user: UserProfile) -> None:
        async with async_session_maker() as session:
            session.add(user)
            await session.commit()
