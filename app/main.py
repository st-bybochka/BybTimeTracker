import asyncio
from aiogram import Bot, Dispatcher
from app.config import settings
from app.handlers import routers




async def main():
    bot = Bot(token=settings.TG_TOKEN)
    dp = Dispatcher()

    for router in routers:
        dp.include_router(router)

    await dp.start_polling(bot)

if __name__ == "__main__":
    asyncio.run(main())
