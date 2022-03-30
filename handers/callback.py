from aiogram import types, Dispatcher
from aiogram.types import InlineKeyboardMarkup, InlineKeyboardButton

from bot_instance import bot


async def problem_1(call: types.CallbackQuery):
    markup = InlineKeyboardMarkup()
    button_call_1 = InlineKeyboardButton("След задача", callback_data="button_call_2")
    markup.add(button_call_1)
    question = "Output:"
    answers = ["1", "2", "3", "4", "5", "6", "7"]
    photo = open("media/msg-1403173883-83(1).jpg", "rb")
    await bot.send_photo(call.message.chat.id, photo=photo)
    await bot.send_poll(
        call.message.chat.id,
        question=question,
        options=answers,
        is_anonymous=False,
        correct_option_id=2,
        type="quiz",
    )


async def flex_4(call: types.CallbackQuery):
    question = "Flex Question"
    answers = ["1", "2", "3", "4", "Error", "None"]
    photo = open("media/flex_5.jpg")
    await bot.send_photo(call.message.chat.id, photo=photo)
    await bot.send_poll(
        call.message.chat.id,
        question=question,
        options=answers,
        is_anonymous=False,
        correct_option_id=4,
        type="quiz",
    )


def register_handlers_callback(dp: Dispatcher):
    dp.register_callback_query_handler(
        problem_1, lambda func: func.data == "button_call_1"
    )
    dp.register_callback_query_handler(
        flex_4, lambda func: func.data == "button_call_2"
    )
