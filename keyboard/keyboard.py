from aiogram.types import ReplyKeyboardMarkup, KeyboardButton

button_quiz = KeyboardButton("/quiz")
button_problem = KeyboardButton("/problem")
button_location = KeyboardButton("Share Location", request_location=True)
button_info = KeyboardButton("Share Info", request_contact=True)

keyboard_stat = ReplyKeyboardMarkup(resize_keyboard=True, row_width=2, one_time_keyboard=True)

keyboard_stat.add(button_problem, button_quiz, button_info, button_location)

