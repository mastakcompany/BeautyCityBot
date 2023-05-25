from aiogram.types import (
    ReplyKeyboardMarkup,
    KeyboardButton,
    InlineKeyboardMarkup,
    InlineKeyboardButton,
)
from lexicon.lexicon_ru import LEXICON_RU


def start_keyboard():
    buttons_data = [
        ('Хочу записать 🕟', 'Выбрать мастера 💞'),
        ('Отзывы 💌', 'О нас 😇'),
        ('Позвонить нам ☎️',)
    ]

    return ReplyKeyboardMarkup(
        keyboard=[
            [KeyboardButton(text=text) for text in row] for row in buttons_data
        ],
        resize_keyboard=True
    )


def get_new_entry_keyboard():
    buttons_data = [
        ('Маникюр - 200 рублей', 'procedure_manicure'),
        ('Педикюр - 250 рублей', 'procedure_pedicure'),
        ('Стрижка - 400 рублей', 'procedure_haircut'),
        ('Уход за лицом - 700 рублей', 'procedure_facial'),
        ('Эпиляция - 550 рублей', 'procedure_removal'),
        ('Отменить', 'cancel'),
    ]

    return InlineKeyboardMarkup(
        inline_keyboard=[
            [InlineKeyboardButton(text=text, callback_data=data)] for text, data in buttons_data
        ]
    )


def get_specialists_keyboard():
    buttons_data = [
        (LEXICON_RU["specialists"][1], "specialist_1"),
        (LEXICON_RU["specialists"][2], "specialist_2"),
        (LEXICON_RU["specialists"][3], "specialist_3"),
    ]
    return InlineKeyboardMarkup(
        inline_keyboard=[
            [InlineKeyboardButton(text=text, callback_data=data)] for text, data in buttons_data
        ]
    )


def get_time_keyboard():
    pass
