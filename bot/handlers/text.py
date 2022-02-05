from main import bot, dp, anti_flood
from aiogram.types import Message
from tools import sql


@dp.message_handler(content_types=['text'])
@dp.throttled(anti_flood, rate=2)
async def echo(message: Message):
    return await bot.send_message(message.from_user.id, text="Не надо мне сюда писать...")
