import os
import logging
from aiohttp import web
from aiogram import Bot, Dispatcher, types

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
dp = Dispatcher(bot)

# Команда /start
@dp.message_handler(commands=["start"])
async def cmd_start(message: types.Message):
    logger.info(f"Команда /start от пользователя {message.from_user.id}")
    keyboard = types.ReplyKeyboardMarkup(resize_keyboard=True)
    keyboard.row(
        types.KeyboardButton("📍 Найти золотомат"),
        types.KeyboardButton("💰 Оценить золото")
    )
    keyboard.row(
        types.KeyboardButton("🛒 Купить слиток"),
        types.KeyboardButton("📤 Продать слитки")
    )
    await message.answer("👋 Добро пожаловать в GOLDEX ROBOT!\nВыберите действие:", reply_markup=keyboard)

# Найти золотомат
@dp.message_handler(lambda message: message.text == "📍 Найти золотомат")
async def find_terminal(message: types.Message):
    logger.info(f"Пользователь {message.from_user.id} выбрал 'Найти золотомат'")
    await message.answer("📍 Найти ближайший золотомат можно тут:\nhttps://goldexrobot.ru/contacts")

# Оценить золото
@dp.message_handler(lambda message: message.text == "💰 Оценить золото")
async def calc_gold(message: types.Message):
    logger.info(f"Пользователь {message.from_user.id} выбрал 'Оценить золото'")
    await message.answer("💰 Оценить своё золото можно тут:\nhttps://goldexrobot.ru/calc")

# Купить слиток
@dp.message_handler(lambda message: message.text == "🛒 Купить слиток")
async def buy_bullion(message: types.Message):
    logger.info(f"Пользователь {message.from_user.id} выбрал 'Купить слиток'")
    keyboard = types.InlineKeyboardMarkup()
    keyboard.add(types.InlineKeyboardButton("🛒 Заказать", url="https://investingold.club/buy-bullions"))
    await message.answer("Выберите действие:", reply_markup=keyboard)

# Продать слитки
@dp.message_handler(lambda message: message.text == "📤 Продать слитки")
async def sell_bullion(message: types.Message):
    logger.info(f"Пользователь {message.from_user.id} выбрал 'Продать слитки'")
    keyboard = types.InlineKeyboardMarkup()
    keyboard.add(types.InlineKeyboardButton("📤 Продать", url="https://investingold.club/buy-bullions"))
    await message.answer("Выберите действие:", reply_markup=keyboard)

# Обработчик Webhook
async def handle_webhook(request):
    if request.headers.get("X-Telegram-Bot-Api-Secret-Token") != WEBHOOK_SECRET:
        return web.Response(status=403)
    update = await request.json()
    await dp.feed_update(bot, types.Update(**update))
    return web.Response()

# При старте приложения
async def on_startup(app):
    await bot.set_webhook(url=WEBHOOK_URL, secret_token=WEBHOOK_SECRET)
    me = await bot.get_me()
    logger.info(f"🤖 Бот запущен: {me.full_name} [@{me.username}] по адресу {WEBHOOK_URL}")

# При остановке приложения
async def on_shutdown(app):
    logger.info("Отключение Webhook...")
    await bot.delete_webhook()

# Создание сервера
app = web.Application()
app.router.add_post("/webhook", handle_webhook)
app.on_startup.append(on_startup)
app.on_shutdown.append(on_shutdown)

# Запуск
if __name__ == "__main__":
    web.run_app(app, port=10000)
