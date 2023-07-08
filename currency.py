from telebot import types

def choice_currency():
    #Создаем пространство для кнопок
    kb = types.ReplyKeyboardMarkup(resize_keyboard=True)

    #Создаем сами кнопки
    dollar_button = types.KeyboardButton('Доллар')
    evro_button = types.KeyboardButton('Евро')

    #Добавляем кнопки в пространство
    kb.add(dollar_button, evro_button)

    #Вернуть пространство
    return kb

# import telebot
# from currency_converter import CurrencyConverter
# from telebot import types
#
# bot = telebot.TeleBot("6165190464:AAHuYDmEbVQ0pb5wDCif3XkQdmYcPy_q33E")
# currency = CurrencyConverter()
# amount = 0
#
#
# @bot.message_handler(commands=["start"])
# def start(message):
#     bot.send_message(message.chat.id, "Привет, введите сумму")
#     bot.register_next_step_handler(message, summa)
#
#
# def summa(message):
#     global amount
#     try:
#         amount = int(message.text.strip())
#     except ValueError:
#         bot.send_message(message.chat.id, 'Неверный формат ввода')
#         bot.register_next_step_handler(message, summa)
#         return
#
#     if amount > 0:
#         markup = types.ReplyKeyboardMarkup(resize_keyboard=True)
#         btn1 = types.KeyboardButton('Доллар')
#         btn2 = types.KeyboardButton('Евро')
#
#         markup.add(btn1, btn2)
#         bot.send_message(message.chat.id, 'Выберите пару валют', reply_markup=markup)
#     else:
#         bot.send_message(message.chat.id, 'Число должно быть больше 0')
#         bot.register_next_step_handler(message, summa)
#
#
# @bot.callback_query_handler(func=lambda call: True)
# def callback(call):
#     values = call.data.upper().split('/')
#     res = currency.convert(amount, values[0], values[1])
#     bot.send_message(call.message.chat.id, f'Получается: {round(res, 2)}. Можете заново вписать сумму')
#     bot.register_next_step_handler(call.message, summa)



# bot.polling(none_stop=True)