import asyncio
from aiogram import Bot, Dispatcher, executor
import logging
from setting_bot.env import Env
from aiogram.contrib.fsm_storage.memory import MemoryStorage
from setting_bot.handlers.user import register_user_handler

# Create bot, loop and logging
logging.basicConfig(level=logging.INFO)
bot = Bot(token=Env.TOKEN, parse_mode='HTML')
dp = Dispatcher(bot, storage=MemoryStorage())
loop = asyncio.get_event_loop()


# Create start handler
register_user_handler(dp)


# run bot
if __name__ == '__main__':
    executor.start_polling(dp, loop=loop, skip_updates=False)
