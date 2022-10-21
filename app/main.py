from aiogram import Bot, Dispatcher, executor
from aiogram.contrib.fsm_storage.memory import MemoryStorage
from aiogram.contrib.middlewares.logging import LoggingMiddleware

from app import logger, settings
from app.handlers import Handlers


token = (settings.DEV, settings.DEV_BOT_TOKEN)[settings.DEV]

bot = Bot(token=token, parse_mode='HTML')
dp = Dispatcher(bot, storage=MemoryStorage())
dp.middleware.setup(LoggingMiddleware())


async def on_startup(_dp: Dispatcher = None) -> None:
    logger.info('Starting bot...')

    _dp = _dp or dp
    Handlers(_dp)()  # register handlers with current dp
    # print(await bot.set_webhook(WEBHOOK_URL))


async def on_shutdown(_dp: Dispatcher) -> None:
    logger.info('Shutting down bot...')

    _dp = _dp or dp
    Handlers(_dp).unregister()  # unregister handlers
    # await bot.delete_webhook()
    # await dp.storage.close()
    # await dp.storage.wait_closed()


if __name__ == '__main__':
    logger.info(f'Bot started{" in dev mode" if settings.DEV else ""}')

    if settings.LONG_POLLING:
        executor.start_polling(
            dispatcher=dp,
            on_startup=on_startup,
            on_shutdown=on_shutdown,
            skip_updates=True
        )
    else:
        executor.start_webhook(
            dispatcher=dp,
            webhook_path=settings.WEBHOOK_PATH,
            on_startup=on_startup,
            on_shutdown=on_shutdown,
            skip_updates=True,
            host=settings.WEBAPP_HOST,
            port=settings.WEBAPP_PORT,
        )
