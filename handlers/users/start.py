from aiogram import types
from aiogram.dispatcher.filters.builtin import CommandStart

from loader import dp

from keyboards.inline.main import add


@dp.message_handler(CommandStart())
async def bot_start(message: types.Message):
    await message.answer(f"""Salom๐
<b>๐ฎ๐ปโโ Gruppada yangi a'zolar Qo'shildi - Chiqdi yani (Kirdi - Chiqdi) haqida malumotni o'chirish uchun maxsus bot.๐</b>

โ ๏ธ Ish boshlashim uchun guruhda <b>ADMIN</b> bo'lishim zarur!""",reply_markup=add())
