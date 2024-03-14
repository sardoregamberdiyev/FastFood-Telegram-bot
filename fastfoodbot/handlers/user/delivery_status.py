from aiogram.types import Message
from loader import dp, db
from .menu import delivery_status
from filters import IsUser


@dp.message_handler(IsUser(), text=delivery_status)
async def process_delivery_status(message: Message):
    orders = db.fetchall('SELECT * FROM orders WHERE cid=?', (message.chat.id,))

    if len(orders) == 0:
        await message.answer('Sizda faol buyurtmalar yo‘q 🚫')
    else:
        for order in orders:
            if len(order) >= 5:  # Check if order has at least 5 elements (including product_id)
                await display_order_details(message, order)
            else:
                await message.answer("Sizning buyurtmangiz qabul qilingan, yoki yo'lda muammolar bo'lsa admin bilan "
                                     "bog'laning 📞\n\n+998994986565")


async def display_order_details(message, order):
    product_id = order[4]  # Extract the product ID from the order
    product_info = db.fetchone('SELECT * FROM products WHERE id=?', (product_id,))

    if product_info:
        product_name = product_info[1]  # Get the product name
        product_quantity = order[5]  # Get the quantity of the product in the order
        product_price = int(product_info[2])  # Get the price of the product

        total_price = product_quantity * product_price  # Calculate the total price

        response = (
            f"Buyurtma raqami: {order[0]}\n"
            f"Mahsulot nomi: {product_name}\n"
            f"Umumiy narxi: {total_price} so'm\n"
        )
    else:
        response = 'Mahsulot topilmadi.'

    await message.answer(response, parse_mode="HTML")

