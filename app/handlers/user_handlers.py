from aiogram import Router, F
from aiogram.types import Message
from aiogram.filters import CommandStart

from app.services import UserService
from app.exceptions.user_exceptions import UserAlreadyExistsError

router = Router()

@router.message(CommandStart())
async def start_cmd(message: Message):
    service = UserService()

    user_id = message.from_user.id
    first_name = message.from_user.first_name
    last_name = message.from_user.last_name

    try:
        await service.create_user_if_not_exists(
            user_id=user_id,
            name=first_name,
            last_name=last_name,
        )
        await message.answer("Hello, user!")
    except UserAlreadyExistsError as e:
        print(e.detail)
        await message.answer("User already exists!")
