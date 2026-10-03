import asyncio
import logging

from aiogram import Bot, Dispatcher
from aiogram.fsm.storage.memory import MemoryStorage

from config import api_key
from comma.handlers import router


logging.basicConfig(level=logging.INFO)

bot = Bot(token=api_key)
dp = Dispatcher(storage=MemoryStorage())
dp.include_router(router)


async def main():
    print("Бот запущен")
    await dp.start_polling(bot)


if __name__ == "__main__":
    try:
        asyncio.run(main())
    except KeyboardInterrupt:
        print("Бот остановлен")