import telebot
import currency

bot = telebot.TeleBot('6165190464:AAG__3v5Vn3MX5WBR8NykF8StSQhx2vIsCw')

dollar = 11500
evro = 12300

@bot.message_handler(commands=['start'])
def start_message(message):
    bot.send_message(message.from_user.id, 'Привет!', reply_markup=currency.choice_currency())


@bot.message_handler(content_types=['text'])
def text_message(message):
    if message.text.lower() == 'привет':
        bot.send_message(message.from_user.id, 'Рад знакомству!')
    elif message.text.lower() == 'пока':
        bot.send_message(message.from_user.id, 'Ну ладно, пока😢😢😢')
    elif message.text.lower() == 'доллар':
        bot.send_message(message.from_user.id, 'Введите сумму в долларах', reply_markup=telebot.types.ReplyKeyboardRemove())
        bot.register_next_step_handler(message, dollar_button)
    elif message.text.lower() == 'евро':
        bot.send_message(message.from_user.id, 'Введите сумму в евро', reply_markup=telebot.types.ReplyKeyboardRemove())
        bot.register_next_step_handler(message, evro_button)


def dollar_button(message):
    try:
        bot.send_message(message.from_user.id, f'Всего {int(message.text) * dollar} сум', reply_markup=currency.choice_currency())
        bot.register_next_step_handler(message, text_message)
    except telebot.apihelper.ApiTelegramException:
        bot.send_message(message.from_user.id, 'Увы, но я не знаю😭😭😭')
        bot.register_next_step_handler(message, dollar_button)


def evro_button(message):
    try:
        bot.send_message(message.from_user.id, f'Всего {int(message.text) * evro} сум', reply_markup=currency.choice_currency())
        bot.register_next_step_handler(message, evro_button)
    except telebot.apihelper.ApiTelegramException:
        bot.send_message(message.from_user.id, 'Увы, но я не знаю😭😭😭')
        bot.register_next_step_handler(message, evro_button)



bot.polling()

































