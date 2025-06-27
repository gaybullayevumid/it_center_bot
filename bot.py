import asyncio
import random
from aiogram import Bot, Dispatcher, types, F
from aiogram.types import Message
from aiogram.enums import ParseMode
from aiogram.filters import CommandStart
from aiogram.utils.keyboard import InlineKeyboardBuilder
from aiogram.client.default import DefaultBotProperties

from config import BOT_TOKEN

gifts = [
    "🎉 Siz -30% chegirma yutib oldingiz!",
    "🎉 Siz -10% chegirma yutib oldingiz!",
    "🎉 Siz -20% chegirma yutib oldingiz!",
    "🎁 Bepul kirish darsi!",
]

user_gifts = {}

bot = Bot(token=BOT_TOKEN, default=DefaultBotProperties(parse_mode=ParseMode.HTML))

dp = Dispatcher()

@dp.message(CommandStart())
async def start_handler(message: Message):
    await message.answer(
        "🎯 Omadli sovg'ani yutib olish uchun pastdagi tugmani bosing 👇",
        reply_markup=gift_button(),
    )

def gift_button():
    builder = InlineKeyboardBuilder()
    builder.button(text="🎁 Sovgani olish", callback_data="get_gift")
    return builder.as_markup()

@dp.callback_query(F.data == "get_gift")
async def send_gift(callback: types.CallbackQuery):
    user_id = callback.from_user.id
    if user_id in user_gifts:
        gift = user_gifts[user_id]
    else:
        gift = random.choice(gifts)
        user_gifts[user_id] = gift
    await callback.message.answer(f"{gift}")
    await callback.answer()

async def main():
    await dp.start_polling(bot)

if __name__ == "__main__":
    asyncio.run(main())