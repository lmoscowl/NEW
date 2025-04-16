import os
import logging
from aiohttp import web
from aiogram import Bot, Dispatcher, types
from aiogram.filters import CommandStart
from aiogram.types import ReplyKeyboardMarkup, KeyboardButton, InlineKeyboardMarkup, InlineKeyboardButton
from aiogram.webhook.aiohttp_server import SimpleRequestHandler, setup_application

# Логирование
logging.basicConfig(level=logging.INFO)
logger = logging.getLogger(__name__)

# Переменные окружения
API_TOKEN = os.getenv("BOT_TOKEN")
WEBHOOK_HOST = os.getenv("WEBHOOK_HOST")
WEBHOOK_SECRET = os.getenv("WEBHOOK_SECRET_TOKEN")
WEBHOOK_PATH = f"/webhook"
WEBHOOK_URL = f"{WEBHOOK_HOST}{WEBHOOK_PATH}"

# Инициализация бота и диспетчера
bot = Bot(token=API_TOKEN)
dp = Dispatcher()

# /start
@dp.message(CommandStart())
async def cmd_start(message: types.Message):
    keyboard = ReplyKeyboardMarkup(resize_keyboard=True, keyboard=[
        [KeyboardButton(text="📍 Найти золотомат"), KeyboardButton(text="💰 Оценить золото")],
        [KeyboardButton(text="🛒 Купить слиток"), KeyboardButton(text="📤 Продать слитки")]
    ])
    await message.answer("👋 Добро пожаловать в GOLDEX ROBOT!\nВыберите действие:", reply_markup=keyboard)

# Найти золотомат
@dp.message(lambda message: message.text == "📍 Найти золотомат")
async def find_terminal(message: types.Message):
    await message.answer("📍 Найти ближайший золотомат можно тут:\nhttps://goldexrobot.ru/contacts")

# Оценить золото
@dp.message(lambda message: message.text == "💰 Оценить золото")
async def calc_gold(message: types.Message):
    await message.answer("💰 Оценить своё золото можно тут:\nhttps://goldexrobot.ru/calc")

# Купить слиток
@dp.message(lambda message: message.text == "🛒 Купить слиток")
async def buy_bullion(message: types.Message):
    keyboard = InlineKeyboardMarkup(inline_keyboard=[
        [InlineKeyboardButton(text="🛒 Заказать", url="https://investingold.club/buy-bullions")]
    ])
    await message.answer("Выберите действие:", reply_markup=keyboard)

# Продать слитки
@dp.message(lambda message: message.text == "📤 Продать слитки")
async def sell_bullion(message: types.Message):
    keyboard = InlineKeyboardMarkup(inline_keyboard=[
        [InlineKeyboardButton(text="📤 Продать", url="https://investingold.club/buy-bullions")]
    ])
    await message.answer("Выберите действие:", reply_markup=keyboard)

# Startup: установка webhook
async def on_startup(bot):
    await bot.set_webhook(WEBHOOK_URL, secret_token=WEBHOOK_SECRET)
    me = await bot.get_me()
    logger.info(f"🤖 Бот запущен: {me.full_name} [@{me.username}] по адресу {WEBHOOK_URL}")

# Shutdown: удаление webhook
async def on_shutdown(bot):
    await bot.delete_webhook()
    logger.info("Webhook удалён")

# Создание и запуск aiohttp сервера
def main():
    app = web.Application()
    dp.startup.register(on_startup)
    dp.shutdown.register(on_shutdown)
    SimpleRequestHandler(dispatcher=dp, bot=bot, secret_token=WEBHOOK_SECRET).register(app, path=WEBHOOK_PATH)
    setup_application(app, dp, bot=bot)
    web.run_app(app, port=10000)

if __name__ == "__main__":
    main()
