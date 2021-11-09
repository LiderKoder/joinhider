from aiogram.types import InlineKeyboardButton, InlineKeyboardMarkup

from data.config import MYBOT

def add():
    keyboard = InlineKeyboardMarkup(row_width=1)
    keyboard.row(
        InlineKeyboardButton("➕ Guruhga qo'shish", url=f"https://t.me/{MYBOT}?startgroup=new")
    )

    return keyboard