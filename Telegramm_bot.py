import random

import telebot
from telebot import types

bot = telebot.TeleBot('6314151534:AAEBtwi4z7EKK-Uz53rFo0WwyDxssDkVAYY')


@bot.message_handler(commands=['start'])
def start(message):
    markup = types.ReplyKeyboardMarkup(resize_keyboard=True)
    btn1 = types.KeyboardButton('Начать')
    btn2 = types.KeyboardButton('Помощь')
    markup.add(btn1, btn2)
    bot.send_message(
        message.from_user.id,
        'Привет!Это игра "Угадай число"!Нажав на кнопку "Начать" ты начнёшь игру.Чтобы узнать подробности об игре нажми "Помощь',
        reply_markup=markup
            )

@bot.message_handler(content_types=['text'])
def game_and_rules(message):
    if message.text == 'Начать':
        markup = types.ReplyKeyboardMarkup(resize_keyboard=True)


        btn1 = types.KeyboardButton('лёгкий (от 1 до 100')
        btn2 = types.KeyboardButton('средний (от 1 до 1000')
        btn3 = types.KeyboardButton('сложный (от 1 до 10000')
        markup.add(btn1, btn2, btn3)
        bot.send_message(
            message.from_user.id,
            'Выберите сложность!',
            reply_markup=markup
        )
    elif message.text == 'лёгкий (от 1 до 100)':
        bot.send_message(message.from_user.id, 'Вы выбрали уровень лёгкй.')
        global popytki
        popytki = 0
        global n_easy
        n_easy = random.randint(1,100)
        global input_number
        while input_number != n_easy:
            bot.send_message(message.from_user.id, 'Введите число')
            bot.register_next_step_handler(message, input_number)
            if input_number > n_easy:
                bot.send_message(message.from_user.id, 'Число', input_number,',больше задуманного числа')
                popytki +=1
            elif input_number < n_easy:
                bot.send_message(message.from_user.id, 'Число', input_number,',меньше задуманного числа')
                popytki +=1

        bot.send_message(message.from_user.id, 'Поздравляю!Вы отгадали загаданное число.Чтобы это сделать вам понадобилось', popytki,'попытки')














    elif message.text == 'средний (от 1 до 1000)':
        bot.send_message(message.from_user.id, 'Вы выбрали уровень средний.Введите число')
        global n_medium
        n_medium = random.randint(1,1000)
















    elif message.text == 'сложный (от 1 до 10000)':
        bot.send_message(message.from_user.id, 'Вы выбрали уровень сложный.Введите число')
        global n_hard
        n_hard = random.randint(1,10000)











    elif message.text == 'Помощь':
        markup = types.ReplyKeyboardMarkup(resize_keyboard=True)
        btn1 = types.KeyboardButton('Правила игры')
        btn2 = types.KeyboardButton('Про автора/проекте')
        markup.add(btn1, btn2)
        bot.send_message(
            message.from_user.id,
            'Выбери,что ты хочешь узнать?',
            reply_markup=markup
        )
    elif message.text == 'Правила игры':
        bot.send_message(message.from_user.id,'Задачей игрока является угадать загаданное число.Бот загадывает число.Игрок вводит число.В ответ пользователю бот выведет информацию,о том что больше или меньше введёное число по сравннию с загаданным.Когда игрок угадал задуманное число игра заканчивается.')
    elif message.text == 'Про автора/проекте':
        bot.send_message(message.from_user.id, 'Учебный проект,созданный юным программистом.')



bot.polling(none_stop=True, interval=0)