from aiogram import types, Dispatcher
from bot_instance import bot


async def secret_word(message: types.Message):
    await message.reply("Yes, my master")


def register_handlers_extra(dp: Dispatcher):
    dp.register_message_handler(secret_word, lambda word: "dorei" in word.text)
