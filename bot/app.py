from aiogram import executor

from loader import dp
import handlers
from utils import on_startup_notify
from utils import set_default_commands


async def onStartup(dispatcher):
    await set_default_commands(dispatcher)
    await on_startup_notify(dispatcher)

if __name__ == "__main__":
    executor.start_polling(dp, on_startup=onStartup)
