import asyncio
import logging

from aiogram import Bot, Dispatcher
from aiogram.fsm.storage.memory import MemoryStorage

from config import settings
from comma.handlers import router


logging.basicConfig(level=logging.INFO)
logger = logging.getLogger(__name__)

bot: Bot = Bot(token=settings.bot_token)
dp: Dispatcher = Dispatcher(storage=MemoryStorage())
dp.include_router(router)


async def main() -> None:
    logger.info('Бот запущен')
    await dp.start_polling(bot)


if __name__ == "__main__":
    try:
        asyncio.run(main())
    except KeyboardInterrupt:
        logger.info('Бот остановлен')


