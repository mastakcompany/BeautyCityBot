from aiogram.types import (
    ReplyKeyboardMarkup,
    KeyboardButton,
    InlineKeyboardMarkup,
    InlineKeyboardButton,
)


def start_keyboard():
    buttons_data = [
        ('Хочу записать', 'Выбрать мастера'),
        ('Отзывы', 'О нас'),
        ('Позвонить нам',)
    ]

    return ReplyKeyboardMarkup(
        keyboard=[
            [KeyboardButton(text=text) for text in row] for row in buttons_data
        ],
        resize_keyboard=True
    )
