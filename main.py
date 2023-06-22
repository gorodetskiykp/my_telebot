import telebot

from cred import TOKEN
from get_vacancies import get_vacancies

bot = telebot.TeleBot(TOKEN, parse_mode=False)


@bot.message_handler(commands=['start'])
def hello_handler(message):
    bot.send_message(message.from_user.id, 'Привет!')
    print('hello_handler')


@bot.message_handler(commands=['help'])
def help_handler(message):
    bot.send_message(message.from_user.id, 'Это тестовый бот!\nКоманды:\n/start\n/help\n/vacancies')
    print('help_handler')


@bot.message_handler(commands=['vacancies'])
def vacancies_handler(message):
    resp_message = get_vacancies()
    bot.send_message(message.from_user.id, resp_message)
    print('vacancies_handler')


bot.infinity_polling()
