import asyncio
from aiogram.contrib.fsm_storage.memory import MemoryStorage
from aiogram import Bot, Dispatcher, executor
from config import BOT_TOKEN, admin_id

loop = asyncio.get_event_loop()
bot = Bot(BOT_TOKEN)
storage = MemoryStorage()
dp = Dispatcher(bot, storage=storage, loop=loop)


async def anti_flood(*args, **kwargs):
    m = args[0]
    await m.answer("Не флуди...")


async def send_to_admin(dp):
    await bot.send_message(chat_id=admin_id, text=f"bot_started")


if __name__ == "__main__":
    from handlers.commands import dp
    executor.start_polling(dp, on_startup=send_to_admin)
    import handlers
