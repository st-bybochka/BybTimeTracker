from aiogram import Router
from aiogram.handlers import message
from aiogram.filters import CommandStart

router = Router()

@router.message(CommandStart())
async def cnd_start(message: message):
    await message.answer(f"{message.from_user.full_name} has started the bot!")