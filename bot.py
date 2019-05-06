import telebot
import pyowm

own = pyowm.OWM("84a6548ab22e73804b69892ac22d0d28", language = "ru");
bot = telebot.TeleBot("738729535:AAHfrW4K0Sw9p1bED4-jGWA09juDY4QB1TY")

@bot.message_handler(content_types=['text'])
def send_echo(message):

    bot.reply_to(message, "Введите название города: ")
    observation = own.weather_at_place(message.text)
    w = observation.get_weather()
    temp = w.get_temperature('celsius')["temp"]

    answer = "В городе " + message.text + " сейчас " + w.get_detailed_status() + "\n"
    answer += "Температура сейчас в районе " + str(temp) + "\n\n"

    if temp < 10:
        answer += "Сейчас пипец как холодно!"
    elif temp < 20:
        answer += "Сейчас холодно - одевайся потеплее"
    else:
        answer += "Temperature is ok - wear whatever you want!"

    bot.send_message(message.chat.id, answer)

bot.polling(none_stop = True)

# @bot.message_handler(func=lamda m:Type)
#     def echo_all(message):
#         bot.reply_to(message, message.text)