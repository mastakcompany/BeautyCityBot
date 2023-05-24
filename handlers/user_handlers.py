from aiogram import Router
from aiogram.filters import Command, CommandStart, Text
from aiogram.types import Message, CallbackQuery, FSInputFile
from aiogram.fsm.state import State, StatesGroup
from aiogram.fsm.context import FSMContext

from keyboards import user_keyboards
from keyboards.user_keyboards import start_keyboard
from lexicon.lexicon_ru import LEXICON_RU
from aiogram3_calendar import DialogCalendar, dialog_cal_callback

from database import database_funcs


router = Router()


class MyCellsState(StatesGroup):
    cell_number = State()
    all_things = State()  # True клиент заберет все вещи, если часть - False


class GetUserInfo(StatesGroup):
    new_user = State()
    weight = State()
    dimension = State()
    rental_period = State()
    phone = State()
    deliver = State()
    yourself_delivery = State()
    courier_delivery = State()
    address = State()


'''
Что сохраняем в БД:

'user_id': 'telegram_id',
'weight': масса вещей,
'cell_size': значение габаритов ячейки, если клиент не хочет сам мерять то False,
'storage_time': срок аренды ячейки,
'phone': user_phone,
'yourself': Bool,
'address': user_address, если пустое, то клиент сам привезет свои вещи,
'is_processed': обработан ли заказ (True) или это новый (False),
'cell_number': номера ячеек хранения,
'''


# Этот хэндлер срабатывает на команду /start
@router.message(CommandStart())
async def process_admin_command(message: Message):
    await message.answer(
        text="Добро пожаловать!",
        reply_markup=start_keyboard()
    )

