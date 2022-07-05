from aiogram.types import ReplyKeyboardMarkup, KeyboardButton

gan_kb = ReplyKeyboardMarkup(resize_keyboard=True, one_time_keyboard=True)
# кнопка выбора между обучением Gan и продолжением добавления картинок
b1 = KeyboardButton('/Gan')
b2 = KeyboardButton('/Add_Style_Image')
gan_kb.row(b1, b2)
