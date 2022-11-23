import asyncio
from aiogram import Bot, Dispatcher, executor, types
import logging
from bot.env import Env
from aiogram.contrib.fsm_storage.memory import MemoryStorage

from bot.keyboards import markup

# Create bot, loop and logging
logging.basicConfig(level=logging.INFO)
bot = Bot(token=Env.TOKEN, parse_mode='HTML')
dp = Dispatcher(bot, storage=MemoryStorage())
loop = asyncio.get_event_loop()


# Create start handler
@dp.message_handler(commands='start')
async def start(message: types.Message):
    text = f'Привет.'
    text2 = f'Я бот журнал.'
    text3 = f'Я записиваю в мою базу данных учеников которые не пришли в школу.\n'
    text3 += f'Узнать по подробнее "Подробнее"'
    await bot.send_message(message.from_user.id, text, reply_markup=markup)
    await bot.send_message(message.from_user.id, text2)
    await bot.send_message(message.from_user.id, text3)
    if message.text == 'Подробнее':
        await more()


@dp.message_handler(content_types='text')
async def more(message: types.Message):
    resp_msg = "/write - записать список учеников\n/write_down - записать отсуствещих\n/show_now - показать отсуствущих на сегодня\n"
    await bot.send_message(message.from_user.id, resp_msg)

# run bot
if __name__ == '__main__':
    executor.start_polling(dp, loop=loop, skip_updates=False)
