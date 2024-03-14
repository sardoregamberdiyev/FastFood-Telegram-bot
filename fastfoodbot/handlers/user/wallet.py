
from loader import dp
from aiogram.dispatcher import FSMContext
from aiogram.types import Message
from filters import IsUser
from .menu import balance

# test card ==> 1111 1111 1111 1111, 00/00, CVC 000

# shopId 506751

# shopArticleId 538350


@dp.message_handler(IsUser(), text=balance)
async def process_balance(message: Message, state: FSMContext):
    await message.answer('Afsuski, onlayn to`lov xizmati mavjud emas. Ammo mahsulot yetkazib berilgandan so`ng '
                         'to\'lov qabul qilinadi ...')

