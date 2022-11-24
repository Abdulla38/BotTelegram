from aiogram import Dispatcher, types
from setting_bot.keyboards import markup


async def start(message: types.Message):
    text = f'Привет.'
    text2 = f'Я бот журнал.'
    text3 = f'Я записиваю в мою базу данных учеников которые не пришли в школу.\n'
    text3 += f'Узнать по подробнее "Подробнее"'
    await message.bot.send_message(message.from_user.id, text, reply_markup=markup)
    await message.bot.send_message(message.from_user.id, text2)
    await message.bot.send_message(message.from_user.id, text3)
    if message.text == 'Подробнее':
        await more()


async def more(message: types.Message):
    resp_msg = "/write - записать список учеников\n/write_down - записать отсутствующих\n"
    resp_msg += "/show_now - показать отсуствущих на сегодня\n/show_all - Показать отсутствующих всю четверть"
    resp_msg += "/"
    await message.bot.send_message(message.from_user.id, resp_msg)


def register_user_handler(dp: Dispatcher):
    dp.register_message_handler(start, commands='start')
    dp.register_message_handler(more, content_types='texr')
