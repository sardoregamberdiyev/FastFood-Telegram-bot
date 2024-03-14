from aiogram.types import Message, CallbackQuery, ReplyKeyboardMarkup
from loader import dp
from filters import IsAdmin, IsUser

catalog = '🍽 Menyu'
balance = '💰 Balans'
cart = '🛒 Savat'
delivery_status = '🚚 Buyurtma holati'

settings = '⚙️ Katalogni sozlash'
orders = '🚚 Buyurtmalar'
questions = '❓ Savollar'


@dp.message_handler(IsAdmin(), commands='menu')
async def admin_menu(message: Message):
    markup = ReplyKeyboardMarkup(resize_keyboard=True)
    markup.add(settings)
    markup.add(questions, orders)

    await message.answer('Kerakli menyuni tanlang 👇🏻', reply_markup=markup)


@dp.message_handler(IsUser(), commands='menu')
async def user_menu(message: Message):
    markup = ReplyKeyboardMarkup(resize_keyboard=True)
    markup.add(catalog)
    markup.add(balance, cart)
    markup.add(delivery_status)

    await message.answer('Kerakli menyuni tanlang 👇🏻', reply_markup=markup)
