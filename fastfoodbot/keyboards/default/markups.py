from aiogram.types import ReplyKeyboardMarkup

back_message = '👈 Orqaga'
confirm_message = '✅ Buyurtmani tasdiqlang'
all_right_message = '✅ Hammasi to\'g\'ri'
cancel_message = '🚫 Bekor qilish'


def confirm_markup():
    markup = ReplyKeyboardMarkup(resize_keyboard=True)
    markup.add(confirm_message)
    markup.add(back_message)

    return markup


def back_markup():
    markup = ReplyKeyboardMarkup(resize_keyboard=True)
    markup.add(back_message)

    return markup


def check_markup():
    markup = ReplyKeyboardMarkup(resize_keyboard=True)
    markup.row(back_message, all_right_message)

    return markup


def submit_markup():
    markup = ReplyKeyboardMarkup(resize_keyboard=True)
    markup.row(cancel_message, all_right_message)

    return markup
