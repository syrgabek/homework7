import asyncio
import aioschedule
from aiogram import types, Dispatcher

from bot_instance import bot


async def echo_and_ban(message: types.Message):
    ban_words = ["java", "bitch", "slut", "python is bad"]
    global chat_id
    chat_id = message.chat.id
    for i in ban_words:
        if i in message.text.lower().replace(" ", ""):
            await message.delete()
            await bot.send_message(message.chat.id, "Bot-Admin deleted bad words")
    if message.text.lower() == "dice":
        await bot.send_dice(message.chat.id, emoji="🎲")
    elif message.text == "wake me up":
        await message.reply("OK")
    elif message.text.startswith("pin"):
        await bot.pin_chat_message(message.chat.id, message.message_id)


async def wake_up():
    await bot.send_message(chat_id=chat_id, text="Wake up please Master!")


async def scheduler():
    aioschedule.every().day.at("20:33").do(wake_up)
    while True:
        await aioschedule.run_pending()
        await asyncio.sleep(1)


def register_handler_notification(dp: Dispatcher):
    dp.register_message_handler(echo_and_ban)
