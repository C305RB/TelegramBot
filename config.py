import aiosqlite
import asyncio
import logging
from aiogram import Bot, Dispatcher, types
from aiogram.filters.command import Command
from aiogram.utils.keyboard import InlineKeyboardBuilder, ReplyKeyboardBuilder
from aiogram import F

# Включаем логирование, чтобы не пропустить важные сообщения
logging.basicConfig(level=logging.INFO)

# Замените "YOUR_BOT_TOKEN" на токен, который вы получили от BotFather
API_TOKEN = '7276685212:AAFr8N760J_4z-_iK4OwOexFf6faOkcSOEY'

# Объект бота
bot = Bot(token=API_TOKEN)
# Диспетчер
dp = Dispatcher()

# Зададим имя базы данных
DB_NAME = 'quiz_bot.db'

quiz_data = [
    {
        'question': 'Что такое Python?',
        'options': ['Язык программирования', 'Тип данных', 'Музыкальный инструмент', 'Змея на английском'],
        'correct_option': 0
    },
    {
        'question': 'Какой тип данных используется для хранения целых чисел?',
        'options': ['int', 'float', 'str', 'natural'],
        'correct_option': 0
    },
    {
        'question': 'Что из перечисленного не является оператором в Python?',
        'options': ['if', 'else', 'while', 'print'],
        'correct_option': 3
    },
    {
        'question': 'Как называется функция, которая возвращает значение без изменения состояния программы?',
        'options': ['чистая функция', 'нечистая функция', 'чистая процедура', 'нечистая процедура'],
        'correct_option': 0
    },
    {
        'question': 'Какая команда используется для создания пустого списка в Python?',
        'options': ['list()', 'empty_list = []', 'empty_list = list()', 'empty_list = {}'],
        'correct_option': 2
    },
    {
        'question': 'Какое ключевое слово используется для объявления функции в Python?',
        'options': ['def', 'function', 'create', 'define'],
        'correct_option': 0
    },
    {
        'question': 'Какой оператор используется для сравнения двух значений в Python?',
        'options': ['==', '=', '>', '<'],
        'correct_option': 0
    },
    {
        'question': 'Какой метод используется для добавления элемента в конец списка в Python?',
        'options': ['append()', 'add()', 'append()', 'extend()'],
        'correct_option': 0
    },
    {
        'question': 'Какой цикл используется для перебора элементов списка в Python?',
        'options': ['for', 'while', 'repeat', 'loop'],
        'correct_option': 0
    },
    {
        'question': 'Какой модуль используется для работы с файлами в Python?',
        'options': ['file', 'io', 'os', 'sys'],
        'correct_option': 3
    },
    # Добавьте другие вопросы
]

async def create_table():
    # Создаем соединение с базой данных (если она не существует, она будет создана)
    async with aiosqlite.connect(DB_NAME) as db:
        # Создаем таблицу
        await db.execute('''CREATE TABLE IF NOT EXISTS quiz_state (user_id INTEGER PRIMARY KEY, question_index INTEGER)''')
        # Сохраняем изменения
        await db.commit()