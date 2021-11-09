from aiogram import types
from aiogram.dispatcher.filters.builtin import CommandStart

from loader import dp

from keyboards.inline.main import add


@dp.message_handler(CommandStart())
async def bot_start(message: types.Message):
    await message.answer(f"""Salom👋
<b>👮🏻‍♂ Gruppada yangi a'zolar Qo'shildi - Chiqdi yani (Kirdi - Chiqdi) haqida malumotni o'chirish uchun maxsus bot.🗑</b>

⚠️ Ish boshlashim uchun guruhda <b>ADMIN</b> bo'lishim zarur!""",reply_markup=add())
