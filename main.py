import asyncio
from aiogram import Bot, Dispatcher, executor, types
import logging
from env import Env
from aiogram.contrib.fsm_storage.memory import MemoryStorage


# Create bot, loop and logging
logging.basicConfig(level=logging.INFO)
bot = Bot(token=Env.TOKEN, parse_mode='HTML')
dp = Dispatcher(bot, storage=MemoryStorage())
loop = asyncio.get_event_loop()


# Create start handler
@dp.message_handler(commands=['start', 'help'])
async def start(msg: types.Message):
    response = "Я бот Журнал. Я записываю учеников. Если нужно помогу.\n"
    response += "Для админов группы\n"
    response += ""
    try:
        await bot.send_message(msg.from_user.idm, response)
    except Exception as ex:
        print(f"Error {ex}")
        await msg.reply("Вы не включили меня в вашем контакт. Пере  дите по этой ссылке: https://t.me/SchoolLateBot")

# run bot
if __name__ == '__main__':
    executor.start_polling(dp, loop=loop, skip_updates=True)
