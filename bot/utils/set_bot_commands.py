from aiogram.types import BotCommand
from aiogram import Dispatcher


async def set_default_commands(dp: Dispatcher):
    await dp.bot.set_my_commands(
        [
            BotCommand("start", "Qayta baslaw")
        ]
    )
