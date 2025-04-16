import os
import logging
from aiogram import Bot, Dispatcher, types, F
from aiogram.fsm.storage.memory import MemoryStorage
from aiogram.types import ReplyKeyboardMarkup, KeyboardButton, InlineKeyboardMarkup, InlineKeyboardButton
from aiogram import Router
from aiohttp import web

# Логирование
logging.basicConfig(level=logging.INFO)
logger = logging.getLogger(__name__)

# Конфиг
API_TOKEN = os.getenv("BOT_TOKEN")
WEBHOOK_PATH = '/webhook'
WEBHOOK_SECRET = 'my_secret_key'
WEBAPP_HOST = '0.0.0.0'
WEBAPP_PORT = int(os.getenv("PORT", 10000))

# Бот и Диспетчер
bot = Bot(token=API_TOKEN)
dp = Dispatcher(storage=MemoryStorage())
router = Router()
dp.include_router(router)

# Хендлеры
@router.message(F.text == "/start")
async def cmd_start(message: types.Message):
    logger.info(f"Команда /start от пользователя {message.from_user.id}")
    keyboard = ReplyKeyboardMarkup(resize_keyboard=True)
    keyboard.row(
        KeyboardButton("📍 Найти золотомат"),
        KeyboardButton("💰 Оценить золото")
    )
    keyboard.row(
        KeyboardButton("🛒 Купить слиток"),
        KeyboardButton("📤 Продать слитки")
    )
    await message.answer("👋 Добро пожаловать в GOLDEX ROBOT!\nВыберите действие:", reply_markup=keyboard)

@router.message(F.text == "📍 Найти золотомат")
async def find_terminal(message: types.Message):
    logger.info(f"Пользователь {message.from_user.id} выбрал 'Найти золотомат'")
    await message.answer("📍 Найти ближайший золотомат можно тут:\nhttps://goldexrobot.ru/contacts")

@router.message(F.text == "💰 Оценить золото")
async def calc_gold(message: types.Message):
    logger.info(f"Пользователь {message.from_user.id} выбрал 'Оценить золото'")
    await message.answer("💰 Оценить своё золото можно тут:\nhttps://goldexrobot.ru/calc")

@router.message(F.text == "🛒 Купить слиток")
async def buy_bullion(message: types.Message):
    logger.info(f"Пользователь {message.from_user.id} выбрал 'Купить слиток'")
    keyboard = InlineKeyboardMarkup(inline_keyboard=[
        [InlineKeyboardButton(text="🛒 Заказать", url="https://investingold.club/buy-bullions")]
    ])
    await
