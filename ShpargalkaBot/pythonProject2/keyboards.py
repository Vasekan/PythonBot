import telebot
from telebot import types


def sub():
    subjects = types.ReplyKeyboardMarkup(resize_keyboard=True)
    math = types.KeyboardButton('Математика')
    physics = types.KeyboardButton('Физика')
    english = types.KeyboardButton('Английский язык')
    calc = types.KeyboardButton('Калькуляторчик')

    subjects.add(math)
    subjects.add(physics)
    subjects.add(english)
    subjects.add(calc)
    return subjects


def kl(sub):
    math = types.InlineKeyboardMarkup()
    seven = types.InlineKeyboardButton("7 класс (" + sub + ")", callback_data='7' + sub)
    eight = types.InlineKeyboardButton("8 класс (" + sub + ")", callback_data='8' + sub)
    nine = types.InlineKeyboardButton("9 класс (" + sub + ")", callback_data='9' + sub)

    math.add(seven)
    math.add(eight)
    math.add(nine)
    return math


def math(kl):
    if kl == 7:
        math = types.InlineKeyboardMarkup()
        btn1_7math = types.InlineKeyboardButton("Свойства степеней", callback_data='btn1_7math')
        btn2_7math = types.InlineKeyboardButton("Формулы сокращённого умножения", callback_data='btn2_7math')
        btn3_7math = types.InlineKeyboardButton("Графики", callback_data='btn3_7math')
        btn4_7math = types.InlineKeyboardButton("Гдз по математике 7 класс", callback_data='btn4_7math')

        math.add(btn1_7math)
        math.add(btn2_7math)
        math.add(btn3_7math)
        math.add(btn4_7math)
    elif kl == 8:
        math = types.InlineKeyboardMarkup()
        btn1_8math = types.InlineKeyboardButton("Квадратные корни", callback_data='btn1_8math')
        btn2_8math = types.InlineKeyboardButton("Формулы сокращённого умножения", callback_data='btn2_8math')
        btn3_8math = types.InlineKeyboardButton('Дискриминант', callback_data='btn3_8math')
        btn4_8math = types.InlineKeyboardButton("Таблица квадратов", callback_data='btn4_8math')
        btn5_8math = types.InlineKeyboardButton("Гдз по математике 8 класс", callback_data='btn5_8math')

        math.add(btn1_8math)
        math.add(btn2_8math)
        math.add(btn3_8math)
        math.add(btn4_8math)
        math.add(btn5_8math)
    elif kl == 9:
        math = types.InlineKeyboardMarkup()
        btn1_9math = types.InlineKeyboardButton('Дискриминант', callback_data='btn1_9math')
        btn2_9math = types.InlineKeyboardButton("Квадратные неравенства", callback_data='btn2_9math')
        btn3_9math = types.InlineKeyboardButton("Прогрессия", callback_data='btn3_9math')
        btn4_9math = types.InlineKeyboardButton("Теория вероятностей", callback_data='btn4_9math')
        btn5_9math = types.InlineKeyboardButton("Таблица квадратов", callback_data='btn5_9math')
        btn6_9math = types.InlineKeyboardButton("Гдз по математике 9 класс", callback_data='btn6_9math')

        math.add(btn1_9math)
        math.add(btn2_9math)
        math.add(btn3_9math)
        math.add(btn4_9math)
        math.add(btn5_9math)
        math.add(btn6_9math)
    return math


def physics(kl):
    if kl == 7:
        physics = types.InlineKeyboardMarkup()
        btn1_7physics = types.InlineKeyboardButton("Взаимодействие тел", callback_data='btn1_7physics')
        btn2_7physics = types.InlineKeyboardButton("Давление твёрдых тел и тд",
                                                   callback_data='btn2_7physics')
        btn3_7physics = types.InlineKeyboardButton("Работа, мощность и энергия", callback_data='btn3_7physics')
        btn4_7physics = types.InlineKeyboardButton("Гдз по физике 7 класс", callback_data='btn4_7physics')

        physics.add(btn1_7physics)
        physics.add(btn2_7physics)
        physics.add(btn3_7physics)
        physics.add(btn4_7physics)
    elif kl == 8:
        physics = types.InlineKeyboardMarkup()
        btn1_8physics = types.InlineKeyboardButton("Тепловые явления", callback_data='btn1_8physics')
        btn2_8physics = types.InlineKeyboardButton("Электрические явления", callback_data='btn2_8physics')
        btn3_8physics = types.InlineKeyboardButton("Электромагнитные явления", callback_data='btn3_8physics')
        btn4_8physics = types.InlineKeyboardButton("Световые явления", callback_data='btn4_8physics')
        btn5_8physics = types.InlineKeyboardButton("Гдз по физике 8 класс", callback_data='btn5_8physics')

        physics.add(btn1_8physics)
        physics.add(btn2_8physics)
        physics.add(btn3_8physics)
        physics.add(btn4_8physics)
        physics.add(btn5_8physics)
    elif kl == 9:
        physics = types.InlineKeyboardMarkup()
        btn1_9physics = types.InlineKeyboardButton("Законы взаимодействия и движения тел",
                                                   callback_data='btn1_9physics')
        btn2_9physics = types.InlineKeyboardButton("Механические колебания и волны, звук",
                                                   callback_data='btn2_9physics')
        btn3_9physics = types.InlineKeyboardButton("Электромагнитные волны", callback_data='btn3_9physics')
        btn4_9physics = types.InlineKeyboardButton("Гдз по физике 9 класс", callback_data='btn4_9physics')

        physics.add(btn1_9physics)
        physics.add(btn2_9physics)
        physics.add(btn3_9physics)
        physics.add(btn4_9physics)
    return physics


def english():
    english = types.ReplyKeyboardMarkup()
    re = types.KeyboardButton("Перевод с русского на английский язык")
    er = types.KeyboardButton("Перевод с английского на русский язык")
    ret = types.KeyboardButton("Вернуться к предметам")

    english.add(re)
    english.add(er)
    english.add(ret)
    return english
