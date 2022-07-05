from aiogram.types import ReplyKeyboardMarkup, KeyboardButton

client_kb = ReplyKeyboardMarkup(resize_keyboard=True, one_time_keyboard=True)
# кнопка выбора модели
b1 = KeyboardButton('/VGG19')
b2 = KeyboardButton('/Gan')

client_kb.row(b1, b2)
