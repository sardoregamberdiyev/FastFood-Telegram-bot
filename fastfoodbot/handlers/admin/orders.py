import sqlite3

from aiogram import types
from aiogram.types import InlineKeyboardMarkup, InlineKeyboardButton
from loader import dp, db, bot
from handlers.user.menu import orders
from filters import IsAdmin

conn = sqlite3.connect('data/database.db')
cursor = conn.cursor()


@dp.message_handler(IsAdmin(), text=orders)
async def process_orders(message: types.Message):
    users = db.fetchall('SELECT DISTINCT cid FROM orders')

    if len(users) == 0:
        await message.answer('Hozircha hech qanday buyurtmalar mavjud emas 😊')
    else:
        for user_id in users:
            await order_answer(message, user_id[0])


async def order_answer(message, user_id):
    orders = db.fetchall('SELECT * FROM orders WHERE cid=?', (user_id,))

    if len(orders) == 0:
        await message.answer(f'{user_id} foydalanuvchisi uchun hech qanday buyurtma yo`q.')
    else:
        for order in orders:
            keyboard = InlineKeyboardMarkup()
            delete_button = InlineKeyboardButton(text="O'chirish", callback_data=f"delete_order_{order[0]}")
            keyboard.add(delete_button)

            await message.answer(f'<b>Buyurtma</b> №{order[0]}\n'
                                 f'<b>Buyurtma nomi:</b> {order[3]}\n\n'
                                 f'<b>Ism Familya:</b> {order[1]}\n'
                                 f'<b>Manzil va Telefon raqami:</b> {order[2]}\n', reply_markup=keyboard)


@dp.message_handler(IsAdmin(), text=orders)
async def process_orders(message: types.Message):
    users = db.fetchall('SELECT DISTINCT cid FROM orders')

    if len(users) == 0:
        await message.answer('Hozircha hech qanday buyurtmalar mavjud emas 😊')
    else:
        for user_id in users:
            await order_answer(message, user_id[0])


import sqlite3

# Ma'lumotlar bazasi ulanishni boshqarish
conn = sqlite3.connect('your_database.db')
cursor = conn.cursor()

async def delete_order(callback_query):
    try:
        message = callback_query.message
        if message:
            message_id = message.message_id
            chat_id = message.chat.id

            # Buyurtma ID ni olish
            order_id = callback_query.data.split('_')[-1]  # Buyurtma ID sini olish

            # Bu joyda bazada o'zgartirish kiritmaslik kerak
            print(f"Buyurtma o'chirildi: {order_id}")

            # Buyurtmalarim tugmasini o'chirish
            await bot.edit_message_reply_markup(chat_id=chat_id, message_id=message_id, reply_markup=None)

            # Xabarni o'chirish
            await bot.delete_message(chat_id=chat_id, message_id=message_id)

            # Ma'lumotni bazadan o'chirish
            cursor.execute('DELETE FROM orders WHERE id=?', (order_id,))
            conn.commit()
        else:
            print("Xatolik: Tugma o'chirilmadi, yangilanmadi, yoki aniqlanmadi")
    except Exception as e:
        print("Xatolik: ", e)


@dp.callback_query_handler(lambda callback_query: callback_query.data.startswith('delete_order'))
async def process_delete_order(callback_query: types.CallbackQuery):
    await delete_order(callback_query)

