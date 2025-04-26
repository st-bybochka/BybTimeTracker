import asyncio

from aiogram import Dispatcher, Bot

from app.config import settings
from app.handlers import routers


async def main():
    bot = Bot(token=settings.TG_TOKEN)
    dp = Dispatcher()

    for router in routers:
        dp.include_router(router)

    await dp.start_polling(bot)


try:
    asyncio.run(main())
except KeyboardInterrupt:
    pass
