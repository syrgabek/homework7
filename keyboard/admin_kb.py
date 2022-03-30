from aiogram.types import KeyboardButton, ReplyKeyboardMarkup

button_download = KeyboardButton("/download")
button_delete = KeyboardButton("/delete")

button_admin = ReplyKeyboardMarkup(resize_keyboard=True).add(button_download, button_delete)