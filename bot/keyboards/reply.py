from aiogram.types import ReplyKeyboardMarkup, KeyboardButton

more = KeyboardButton(text="ПОДРОБНЕЕ")
markup = ReplyKeyboardMarkup(resize_keyboard=True)

markup.add(more)
