from aiogram import types, Dispatcher
from aiogram.dispatcher import FSMContext
from aiogram.dispatcher.filters import Text
from aiogram.dispatcher.filters.state import State, StatesGroup
from aiogram.types import InlineKeyboardButton, InlineKeyboardMarkup
from database import bot_db
from bot_instance import dp, bot
from aiogram.dispatcher.filters import Text
from keyboard import admin_kb


class FSMADMIN(StatesGroup):
    photo = State()
    title = State()
    description = State()


async def is_admin_func(message: types.Message):
    global ADMIN_ID
    ADMIN_ID = message.from_user.id
    await bot.send_message(
        message.from_user.id,
        "Admin, What do u need",
        reply_markup=admin_kb.button_admin,
    )


async def cancel_handler(message: types.Message, state: FSMContext):
    if message.from_user.id == ADMIN_ID:
        current_state = await state.get_state()
        await state.finish()
        await message.reply("Canceled Successfully")


async def fsm_start(message: types.Message):
    if message.from_user.id == ADMIN_ID:
        await FSMADMIN.photo.set()
        await message.reply("Admin, Send me photo please")


async def load_photo(message: types.Message, state: FSMContext):
    if message.from_user.id == ADMIN_ID:
        async with state.proxy() as data:
            data["photo"] = message.photo[0].file_id
        await FSMADMIN.next()
        await message.reply("Send me title of photo")


async def load_title(message: types.Message, state: FSMContext):
    # if message.from_user.id == ADMIN_ID:
    async with state.proxy() as data:
        data["title"] = message.text
    await FSMADMIN.next()
    await message.reply("Admin, send me description, please")


async def load_description(message: types.Message, state: FSMContext):
    if message.from_user.id == ADMIN_ID:
        async with state.proxy() as data:
            data["description"] = message.text
        # async with state.proxy() as data:
        #     await message.reply(str(data))
        await bot_db.sql_command_insert(state)
        await state.finish()


async def complete_delete(call: types.CallbackQuery):
    await bot_db.sql_command_delete(call.data.replace("delete ", ""))
    await call.answer(
        text=f"{call.data.replace('delete ', '')} deleted", show_alert=True
    )


async def delete_data(message: types.Message):
    if message.from_user.id == ADMIN_ID:
        inserting = await bot_db.sql_casual_select()
        for result in inserting:
            await bot.send_photo(
                message.from_user.id,
                result[0],
                caption=f"Title: {result[1]}\n" f"Description: {result[2]}",
                reply_markup=InlineKeyboardMarkup().add(
                    InlineKeyboardButton(
                        f"delete: {result[1]}", callback_data=f"delete {result[1]}"
                    )
                ),
            )


def register_handler_fsmadmin(dp: Dispatcher):
    dp.register_message_handler(fsm_start, commands=["download"], state=None)
    dp.register_message_handler(cancel_handler, state="*", commands="cancel")
    dp.register_message_handler(
        cancel_handler, Text(equals="cancel", ignore_case=True), state="*"
    )
    dp.register_message_handler(
        load_photo, content_types=["photo"], state=FSMADMIN.photo
    )
    dp.register_message_handler(load_title, state=FSMADMIN.title)
    dp.register_message_handler(load_description, state=FSMADMIN.description)
    dp.register_message_handler(is_admin_func, commands=["admin"], is_chat_admin=True)
    dp.register_callback_query_handler(
        complete_delete, lambda call: call.data and call.data.startswith("delete ")
    )
    dp.register_message_handler(delete_data, commands=["delete"])
