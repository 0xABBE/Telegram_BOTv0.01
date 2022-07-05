from aiogram.types import ReplyKeyboardMarkup, KeyboardButton

accept_kb = ReplyKeyboardMarkup(resize_keyboard=True, one_time_keyboard=True)
# кнопка подтверждения продолжения работы
b1 = KeyboardButton('/accept')

accept_kb.row(b1)
