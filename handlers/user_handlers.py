from aiogram import Router
from aiogram.filters import CommandStart, Text
from aiogram.types import Message, CallbackQuery
from aiogram.fsm.state import State, StatesGroup
from aiogram.fsm.context import FSMContext
from aiogram3_calendar import SimpleCalendar, simple_cal_callback

from keyboards.user_keyboards import start_keyboard, get_new_entry_keyboard

router = Router()


class NewEntry(StatesGroup):
    procedure_name = State()
    procedure_date = State()
    procedure_time = State()
    procedure_specialist = State()


# Этот хэндлер срабатывает на команду /start
@router.message(CommandStart())
async def process_admin_command(message: Message):
    await message.answer(
        text="Добро пожаловать!",
        reply_markup=start_keyboard()
    )


@router.message(Text(startswith=["Хочу записать"]))
async def get_new_entry(message: Message, state: FSMContext):
    await message.answer(
        text="Выберите процедуру, пожалуйста 💁‍♀️",
        reply_markup=get_new_entry_keyboard()
    )

    await state.set_state(NewEntry.procedure_name)


@router.callback_query(Text(startswith=["procedure"]), NewEntry.procedure_name)
async def get_procedure_name(callback: CallbackQuery, state: FSMContext):
    procedure_name = callback.data
    await state.update_data(procedure_name=procedure_name)

    await callback.message.edit_text(
        text="Выберите дату, пожалуйста:",
        reply_markup=await SimpleCalendar.start_calendar()
    )
    await state.set_state(NewEntry.procedure_date)
    await callback.answer()


@router.callback_query(simple_cal_callback.filter(), NewEntry.procedure_date)
async def get_procedure_date(callback: CallbackQuery, callback_data, state: FSMContext):
    selected, date = await SimpleCalendar().process_selection(callback, callback_data)
    if selected:
        procedure_date = date.strftime("%d/%m/%Y")
        await state.update_data(procedure_date=procedure_date)
    await callback.message.edit_text(
        text="Выберите время, пожадуйста:"
    )
    await state.set_state(NewEntry.procedure_time)
    await callback.answer()


@router.callback_query(NewEntry.procedure_time)
async def get_procedure_time(callback: CallbackQuery, state: FSMContext):
    pass


@router.callback_query(Text(startswith=["specialist"]), NewEntry.procedure_specialist)
async def get_procedure_specialist(callback: CallbackQuery, state: FSMContext):
    procedure_specialist = callback.data.split("_")[1]
    print(procedure_specialist)

