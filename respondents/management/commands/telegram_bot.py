from django.core.management.base import BaseCommand
from telebot import TeleBot, types

from respondents.models import Respondent
from config import settings
from surveys.models import Survey

bot = TeleBot(token=settings.TELEGRAM_BOT_TOKEN)


@bot.message_handler(commands=['start'])
def start(message):
    '''Приветствие'''
    markup = types.ReplyKeyboardMarkup(resize_keyboard=True)
    btn1 = types.KeyboardButton("Представиться")
    btn2 = types.KeyboardButton("Обо мне")
    markup.add(btn1, btn2)
    hello_text = f'Добро пожаловать в "Трекер настроения"! \nДавайте познакомимся!'
    bot.send_message(message.chat.id, hello_text.format(message.from_user), reply_markup=markup)


@bot.message_handler(content_types=['text'])
def func(message):
    if message.text == "Представиться":
        bot.register_next_step_handler(message, get_name)
    elif message.text == "Обо мне":
        markup = types.ReplyKeyboardMarkup(resize_keyboard=True)
        back = types.KeyboardButton("Вернуться в главное меню")
        markup.add(back)
        about_me = f'Я собираю данные по оценке твоего настроения и энергии, обрабатываю их и отправляю тебе отчет.'
        bot.send_message(message.chat.id, text=about_me)
    elif message.text == "Вернуться в главное меню":
        markup = types.ReplyKeyboardMarkup(resize_keyboard=True)
        btn1 = types.KeyboardButton("Представиться")
        btn2 = types.KeyboardButton("Обо мне")
        markup.add(btn1, btn2)
        bot.send_message(message.chat.id, text="Вы вернулись в главное меню", reply_markup=markup)
    else:
        bot.send_message(message.from_user.id, 'На такую команду я не запрограммирован')


def get_name(message):
    '''Получить имя от клиента'''
    first_name = message.text
    bot.send_message(message.from_user.id, 'Напишите ваше Имя')
    bot.register_next_step_handler(message, get_surname, first_name)


def get_surname(message, first_name):
    '''Получить фамилию от клиента'''
    last_name = message.text
    bot.send_message(message.from_user.id, 'Напишите вашу Фамилию')

    '''Получаем и обрабатываем данные из сообщения'''
    chat_id = message.chat.id
    respondent_tg_id = message.from_user.id

    '''Проверяем, существует ли клиент в базе данных'''
    respondent, created = Respondent.objects.get_or_create(respondent_tg_id=respondent_tg_id)
    if created:
        '''Если клиент был создан впервые, заполняем его данные'''
        respondent.first_name = first_name
        respondent.last_name = last_name
        respondent.chat_tg_id = chat_id
        respondent.save()
    else:
        '''Если клиент уже существует, обновляем его данные'''
        respondent.first_name = first_name
        respondent.last_name = last_name
        respondent.chat_tg_id = chat_id
        respondent.save()

    '''Отправляем подтверждение клиенту'''
    bot.send_message(message.from_user.id, "Ваши данные были сохранены!")


def ask_mood(respondent_tg_id):
    '''Задать вопрос об оценке настроения'''
    markup = types.ReplyKeyboardMarkup(resize_keyboard=True)
    btn1 = types.KeyboardButton("1")
    btn2 = types.KeyboardButton("2")
    btn3 = types.KeyboardButton("3")
    btn4 = types.KeyboardButton("4")
    btn5 = types.KeyboardButton("5")
    markup.add(btn1, btn2, btn3, btn4, btn5)
    bot.send_message(respondent_tg_id, "Оцените свое настроение от 1 до 5:", reply_markup=markup)
    bot.register_next_step_handler_by_chat_id(respondent_tg_id, save_mood)


def save_mood(message):
    '''Сохранить оценку настроения и задать вопрос об оценке энергии'''
    mood = int(message.text)
    respondent_tg_id = message.chat.id
    respondent = Respondent.objects.get(respondent_tg_id=respondent_tg_id)
    survey = Survey.objects.create(respondent=respondent, mood=mood)
    survey.save()

    ask_energy(respondent_tg_id)  # Задаем вопрос об оценке энергии


def ask_energy(respondent_tg_id):
    '''Задать вопрос об оценке энергии'''
    markup = types.ReplyKeyboardMarkup(resize_keyboard=True)
    btn1 = types.KeyboardButton("1")
    btn2 = types.KeyboardButton("2")
    btn3 = types.KeyboardButton("3")
    btn4 = types.KeyboardButton("4")
    btn5 = types.KeyboardButton("5")
    markup.add(btn1, btn2, btn3, btn4, btn5)
    bot.send_message(respondent_tg_id, "Оцените свою энергию от 1 до 5:", reply_markup=markup)
    bot.register_next_step_handler_by_chat_id(respondent_tg_id, save_energy)


def save_energy(message):
    '''Сохранить оценку энергии'''
    energy = int(message.text)
    respondent_tg_id = message.chat.id

    respondent = Respondent.objects.get(respondent_tg_id=respondent_tg_id)
    survey = Survey.objects.create(respondent=respondent, energy=energy)
    survey.save()

    bot.send_message(respondent_tg_id, "Спасибо! Ваша оценка сохранена.")  # Завершаем опрос и отправляем подтверждение


class Command(BaseCommand):
    '''Запуск Телеграмм бота'''
    def handle(self, *args, **kwargs):
        bot.enable_save_next_step_handlers(delay=2)  # Сохранение обработчиков
        bot.load_next_step_handlers()  # Загрузка обработчиков
        bot.infinity_polling()  # Бесконечный цикл бота
