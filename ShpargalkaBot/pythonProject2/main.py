import keyboards as kb
import telebot
import re
from telebot import types
from translate import Translator

bot = telebot.TeleBot('5386714175:AAF0tjsHQaJ2zJA0E63uKToOpAieF2m3ldo')


@bot.message_handler(commands=['start'])
def start(message):
    ms = 'Здравствуёте, ' + message.from_user.first_name
    bot.send_message(message.chat.id, ms)
    bot.send_message(message.chat.id, "Выберете предмет", reply_markup=kb.sub())


@bot.message_handler(commands=['help'])
def help(message):
    ms = "Этот бот помогает в решении домашних работ, " \
         "а также является шпаргалкой во время самостоятельных, контрольных." + \
         "\n" + "Бот предназначен для 7, 8, 9 класса " \
                "и включает в себя такие предметы, как Математика, Физика, Английский язык."
    bot.send_message(message.chat.id, ms)


@bot.callback_query_handler(func=lambda call: call.data.startswith('btn1_7math'))
def btn1_7math(call: types.CallbackQuery):
    photo = open("subjects/math/7math/свойства степеней.jpg", 'rb')
    bot.send_photo(call.from_user.id, photo)
    bot.send_message(call.from_user.id, "Выберете тему", reply_markup=kb.math(7))


@bot.callback_query_handler(func=lambda call: call.data.startswith('btn2_7math'))
def btn2_7math(call: types.CallbackQuery):
    photo = open("subjects/math/7math/форм сокр умн.jpg", 'rb')
    bot.send_photo(call.from_user.id, photo)
    bot.send_message(call.from_user.id, "Выберете тему", reply_markup=kb.math(7))


@bot.callback_query_handler(func=lambda call: call.data.startswith('btn3_7math'))
def btn3_7math(call):
    photo = open("subjects/math/7math/графики.png", 'rb')
    bot.send_photo(call.from_user.id, photo)
    bot.send_message(call.from_user.id, "Выберете тему", reply_markup=kb.math(7))


@bot.callback_query_handler(func=lambda call: call.data.startswith('btn4_7math'))
def btn4_7math(call):
    btn = types.InlineKeyboardMarkup()
    btn.add(types.InlineKeyboardButton("Нажми кнопку", url="https://gdz.ru/class-7/algebra/"))
    bot.send_message(call.from_user.id, 'Давай', reply_markup=btn)


@bot.callback_query_handler(func=lambda call: call.data.startswith('btn1_8math'))
def btn1_8math(call):
    photo = open("subjects/math/8math/свойства квадратного корня.png", 'rb')
    bot.send_photo(call.from_user.id, photo)
    bot.send_message(call.from_user.id, "Выберете тему", reply_markup=kb.math(8))


@bot.callback_query_handler(func=lambda call: call.data.startswith('btn2_8math'))
def btn2_8math(call):
    photo = open("subjects/math/8math/форм сокр умн.jpg", 'rb')
    bot.send_photo(call.from_user.id, photo)
    bot.send_message(call.from_user.id, "Выберете тему", reply_markup=kb.math(8))


@bot.callback_query_handler(func=lambda call: call.data.startswith('btn3_8math'))
def btn3_8math(call):
    photo = open("subjects/math/8math/дискрминант.jpg", 'rb')
    bot.send_photo(call.from_user.id, photo)
    bot.send_message(call.from_user.id, "Выберете тему", reply_markup=kb.math(8))


@bot.callback_query_handler(func=lambda call: call.data.startswith('btn4_8math'))
def btn4_8math(call):
    photo = open("subjects/math/8math/таблица квадратов.jpeg", 'rb')
    bot.send_photo(call.from_user.id, photo)
    bot.send_message(call.from_user.id, "Выберете тему", reply_markup=kb.math(8))


@bot.callback_query_handler(func=lambda call: call.data.startswith('btn5_8math'))
def btn5_8math(call):
    btn = types.InlineKeyboardMarkup()
    btn.add(types.InlineKeyboardButton("Нажми кнопку", url="https://gdz.ru/class-8/algebra/"))
    bot.send_message(call.from_user.id, 'Давай', reply_markup=btn)


@bot.callback_query_handler(func=lambda call: call.data.startswith('btn1_9math'))
def btn1_9math(call):
    photo = open("subjects/math/9math/дискрминант.jpg", 'rb')
    bot.send_photo(call.from_user.id, photo)
    bot.send_message(call.from_user.id, "Выберете тему", reply_markup=kb.math(9))


@bot.callback_query_handler(func=lambda call: call.data.startswith('btn2_9math'))
def btn2_9math(call):
    photo = open("subjects/math/9math/квадратные неравенства.jpg", 'rb')
    bot.send_photo(call.from_user.id, photo)
    bot.send_message(call.from_user.id, "Выберете тему", reply_markup=kb.math(9))


@bot.callback_query_handler(func=lambda call: call.data.startswith('btn3_9math'))
def btn3_9math(call):
    photo = open("subjects/math/9math/прогрессия.jpg", 'rb')
    bot.send_photo(call.from_user.id, photo)
    bot.send_message(call.from_user.id, "Выберете тему", reply_markup=kb.math(9))


@bot.callback_query_handler(func=lambda call: call.data.startswith('btn4_9math'))
def btn4_9math(call):
    photo = open("subjects/math/9math/теория вероятностей.jpg", 'rb')
    bot.send_photo(call.from_user.id, photo)
    bot.send_message(call.from_user.id, "Выберете тему", reply_markup=kb.math(9))


@bot.callback_query_handler(func=lambda call: call.data.startswith('btn5_9math'))
def btn5_9math(call):
    photo = open("subjects/math/9math/таблица квадратов.jpeg", 'rb')
    bot.send_photo(call.from_user.id, photo)
    bot.send_message(call.from_user.id, "Выберете тему", reply_markup=kb.math(9))


@bot.callback_query_handler(func=lambda call: call.data.startswith('btn6_9math'))
def btn6_9math(call):
    btn = types.InlineKeyboardMarkup()
    btn.add(types.InlineKeyboardButton("Нажми кнопку", url="https://gdz.ru/class-9/algebra/"))
    bot.send_message(call.from_user.id, 'Давай', reply_markup=btn)


@bot.callback_query_handler(func=lambda call: call.data.startswith('btn1_7physics'))
def btn1_7physics(call):
    photo = open("subjects/physics/7physics/взаимодействие тел.png", 'rb')
    bot.send_photo(call.from_user.id, photo)
    bot.send_message(call.from_user.id, "Выберете тему", reply_markup=kb.physics(7))


@bot.callback_query_handler(func=lambda call: call.data.startswith('btn2_7physics'))
def btn2_7physics(call):
    photo = open("subjects/physics/7physics/давление.png", 'rb')
    bot.send_photo(call.from_user.id, photo)
    bot.send_message(call.from_user.id, "Выберете тему", reply_markup=kb.physics(7))


@bot.callback_query_handler(func=lambda call: call.data.startswith('btn3_7physics'))
def btn3_7physics(call):
    photo = open("subjects/physics/7physics/работа и мощность.png", 'rb')
    bot.send_photo(call.from_user.id, photo)
    bot.send_message(call.from_user.id, "Выберете тему", reply_markup=kb.physics(7))


@bot.callback_query_handler(func=lambda call: call.data.startswith('btn4_7physics'))
def btn4_7physics(call):
    btn = types.InlineKeyboardMarkup()
    btn.add(types.InlineKeyboardButton("Нажми кнопку", url="https://gdz.ru/class-7/fizika/"))
    bot.send_message(call.from_user.id, 'Давай', reply_markup=btn)


@bot.callback_query_handler(func=lambda call: call.data.startswith('btn1_8physics'))
def btn1_8physics(call):
    photo = open("subjects/physics/8physics/тепловые явления.png", 'rb')
    bot.send_photo(call.from_user.id, photo)
    bot.send_message(call.from_user.id, "Выберете тему", reply_markup=kb.physics(8))


@bot.callback_query_handler(func=lambda call: call.data.startswith('btn2_8physics'))
def btn2_8physics(call):
    photo = open("subjects/physics/8physics/электрические явления.png", 'rb')
    bot.send_photo(call.from_user.id, photo)
    bot.send_message(call.from_user.id, "Выберете тему", reply_markup=kb.physics(8))


@bot.callback_query_handler(func=lambda call: call.data.startswith('btn3_8physics'))
def btn3_8physics(call):
    photo = open("subjects/physics/8physics/электромагнитные явления.png", 'rb')
    bot.send_photo(call.from_user.id, photo)
    bot.send_message(call.from_user.id, "Выберете тему", reply_markup=kb.physics(8))


@bot.callback_query_handler(func=lambda call: call.data.startswith('btn4_8physics'))
def btn4_8physics(call):
    photo = open("subjects/physics/8physics/световые явления.png", 'rb')
    bot.send_photo(call.from_user.id, photo)
    bot.send_message(call.from_user.id, "Выберете тему", reply_markup=kb.physics(8))


@bot.callback_query_handler(func=lambda call: call.data.startswith('btn5_8physics'))
def btn5_8physics(call):
    btn = types.InlineKeyboardMarkup()
    btn.add(types.InlineKeyboardButton("Нажми кнопку", url="https://gdz.ru/class-8/fizika/"))
    bot.send_message(call.from_user.id, 'Давай', reply_markup=btn)


@bot.callback_query_handler(func=lambda call: call.data.startswith('btn1_9physics'))
def btn1_9physics(call):
    photo = open("subjects/physics/9physics/закон взаим и тд.png", 'rb')
    bot.send_photo(call.from_user.id, photo)
    bot.send_message(call.from_user.id, "Выберете тему", reply_markup=kb.physics(9))


@bot.callback_query_handler(func=lambda call: call.data.startswith('btn2_9physics'))
def btn2_9physics(call):
    photo = open("subjects/physics/9physics/колеб и волны.png", 'rb')
    bot.send_photo(call.from_user.id, photo)
    bot.send_message(call.from_user.id, "Выберете тему", reply_markup=kb.physics(9))


@bot.callback_query_handler(func=lambda call: call.data.startswith('btn3_9physics'))
def btn3_9physics(call):
    photo = open("subjects/physics/9physics/электромаг.png", 'rb')
    bot.send_photo(call.from_user.id, photo)
    bot.send_message(call.from_user.id, "Выберете тему", reply_markup=kb.physics(9))


@bot.callback_query_handler(func=lambda call: call.data.startswith('btn4_9physics'))
def btn4_9physics(call):
    btn = types.InlineKeyboardMarkup()
    btn.add(types.InlineKeyboardButton("Нажми кнопку", url="https://gdz.ru/class-9/fizika/"))
    bot.send_message(call.from_user.id, 'Давай', reply_markup=btn)


@bot.callback_query_handler(func=lambda call: True)
def choose_kl(call: types.CallbackQuery):
    if call.data == "7Математика":
        bot.send_message(call.from_user.id, "Выберете тему", reply_markup=kb.math(7))
    elif call.data == "8Математика":
        bot.send_message(call.from_user.id, "Выберете тему", reply_markup=kb.math(8))
    elif call.data == "9Математика":
        bot.send_message(call.from_user.id, "Выберете тему", reply_markup=kb.math(9))
    elif call.data == "7Физика":
        bot.send_message(call.from_user.id, "Выберете тему", reply_markup=kb.physics(7))
    elif call.data == "8Физика":
        bot.send_message(call.from_user.id, "Выберете тему", reply_markup=kb.physics(8))
    elif call.data == "9Физика":
        bot.send_message(call.from_user.id, "Выберете тему", reply_markup=kb.physics(9))


def from_rus_to_eng(message):
    translator = Translator(from_lang="russian", to_lang="english")
    translation = translator.translate(message.text)
    bot.send_message(message.from_user.id, translation)


def from_eng_to_rus(message):
    translator = Translator(from_lang="english", to_lang="russian")
    translation = translator.translate(message.text)
    bot.send_message(message.from_user.id, translation)


def calculator(message):
    s = message.text
    s = re.sub(r"\s*", "", s)
    s1 = ""
    queue = []
    stack = []
    for i in range(0, len(s)):
        if (s[i].isdigit()):
            s1 = str(s1) + str(s[i])
        else:
            if (len(s1) > 0):
                queue.append(s1)
                s1 = ""
            if (len(stack) == 0 or stack[0] == "("):
                stack.insert(0, s[i])
            elif (s[i] in "*/" and stack[0] in "+-"):
                stack.insert(0, s[i])
            elif (s[i] in "+-*/" and stack[0] in "+-*/"):
                if (s[i] in "+-" and stack[0] in "*/+-"):
                    while (len(stack) > 0 and not (stack[0] in "(")):
                        queue.append(stack.pop(0))
                    stack.insert(0, s[i])
                elif (s[i] in "*/" and stack[0] in "*/"):
                    while (len(stack) > 0 and not (stack[0] in "+-(")):
                        queue.append(stack.pop(0))
                    stack.insert(0, s[i])
            elif (s[i] == "("):
                stack.insert(0, "(")
            elif (s[i] == ")"):
                while (len(stack) > 0 and stack[0] != "("):
                    queue.append(stack.pop(0))
                if (len(stack) > 0): stack.pop(0)
    if (len(s1) > 0): queue.append(s1)
    while (len(stack) > 0): queue.append(stack.pop(0))
    stack1 = []
    for i in queue:
        if (i.isdigit()):
            stack1.insert(0, i)
        elif (i in "+-*/"):
            a = int(stack1.pop(0))
            b = int(stack1.pop(0))
            res = 0
            if (i == "+"): res = b + a
            if (i == "-"): res = b - a
            if (i == "*"): res = b * a
            if (i == "/"): res = b / a
            stack1.insert(0, res)
    bot.send_message(message.chat.id, 'Ответ:')
    bot.send_message(message.chat.id, str(res), reply_markup=kb.sub())


@bot.message_handler(content_types=['text'])
def text(mess):
    if mess.text == "Я не готов к кр а она уже завтра":
        but = types.InlineKeyboardMarkup()
        but.add(types.InlineKeyboardButton("Нажми кнопку", url="https://www.youtube.com/watch?v=dQw4w9WgXcQ"))
        bot.send_message(mess.chat.id, 'Давай', reply_markup=but)
    elif mess.text == 'Математика':
        bot.send_message(mess.chat.id, "Выберете класс", reply_markup=kb.kl('Математика'))
    elif mess.text == 'Физика':
        bot.send_message(mess.chat.id, "Выберете класс", reply_markup=kb.kl('Физика'))
    elif mess.text == "Английский язык":
        bot.send_message(mess.chat.id, "Выберете перевод", reply_markup=kb.english())
    elif mess.text == "Перевод с русского на английский язык":
        sent = bot.send_message(mess.chat.id, "Введите текст")
        bot.register_next_step_handler(sent, from_rus_to_eng)
    elif mess.text == "Перевод с английского на русский язык":
        sent = bot.send_message(mess.chat.id, "Введите текст")
        bot.register_next_step_handler(sent, from_eng_to_rus)
    elif mess.text == "Вернуться к предметам":
        bot.send_message(mess.chat.id, "Выберете предмет", reply_markup=kb.sub())
    elif mess.text == 'Калькуляторчик':
        sent = bot.send_message(mess.chat.id, "Введите задачу >>")
        bot.register_next_step_handler(sent, calculator)
    else:
        bot.send_message(mess.chat.id, "не понимаю")


bot.polling(none_stop=True)
