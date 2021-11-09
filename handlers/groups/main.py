from aiogram import types

from loader import dp

from keyboards.inline.main import add

@dp.message_handler(content_types=['new_chat_members'])
async def join_del(message: types.Message):
    new = message.new_chat_members[0].id
    if new == 1906146386:
        await message.answer(f"""Salom👋
<b>👮🏻‍♂ Gruppada yangi a'zolar Qo'shildi - Chiqdi yani (Kirdi - Chiqdi) haqida malumotni o'chirish uchun maxsus bot.🗑</b>

⚠️ Ish boshlashim uchun guruhda <b>ADMIN</b> bo'lishim zarur!""",reply_markup=add())
    else:
        try:
            await message.delete()
        except:
            pass

# @dp.message_handler(content_types=['new_chat_members','left_chat_member'])
# async def join_del(message: types.Message):
#     # await message.delete()
#     await message.answer("Salom")