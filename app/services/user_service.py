from app.repositories.user_repository import UserRepository
from app.models.user_model import UserProfile
from app.exceptions import UserAlreadyExistsError

class UserService:
    user_repository = UserRepository()

    async def create_user_if_not_exists(self, user_id: int, name: str, last_name: str) -> None:
        existing_user = await self.user_repository.get_by_id(user_id)
        if existing_user:
            raise UserAlreadyExistsError

        user = UserProfile(
            id=user_id,
            name=name,
            last_name=last_name
        )
        await self.user_repository.create_user(user)

