from aiogram import Router
from aiogram.types import Message
from aiogram.filters import Command, Text
from aiogram.fsm.context import FSMContext
from aiogram.fsm.state import State, StatesGroup
from aiogram.types import Message, CallbackQuery

from lexicon.lexicon_ru import LEXICON_RU
from keyboards import admin_keyboards
from database import database_funcs
from config_data.config import load_config
from utils import utils

from sqlite3_api.Table import Table

router = Router()


class GetCellNumber(StatesGroup):
    cell_number = State()
    order_id = State()
    link = State()
    link_name = State()


@router.message(Command(commands=['admin']))
async def process_admin_command(message: Message):
    pass

