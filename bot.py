import os
import logging
from aiogram import Bot, Dispatcher, types
from aiogram.fsm.storage.memory import MemoryStorage
from aiohttp import web

logging.basicConfig(level=logging.INFO)
logger = logging.getLogger(__name__)

API_TOKEN = os.getenv("BOT_TOKEN")
WEBHOOK_PATH = '/webhook'
WEBHOOK_SECRET = 'my_secret_key'
WEBAPP_HOST = '0.0.0.0'
WEBAPP_PORT = int(os.getenv("PORT", 10000))

bot = Bot(token=API_TOKEN)
dp = Dispatcher(storage=MemoryStorage())

@dp.message_handler(commands=['start'])
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

@dp.message_handler(lambda message: message.text == "📍 Найти золотомат")
async def find_terminal(message: types.Message):
    logger.info(f"Пользователь {message.from_user.id} выбрал 'Найти золотомат'")
    await message.answer("📍 Найти ближайший золотомат можно тут:\nhttps://goldexrobot.ru/contacts")

@dp.message_handler(lambda message: message.text == "💰 Оценить золото")
async def calc_gold(message: types.Message):
    logger.info(f"Пользователь {message.from_user.id} выбрал 'Оценить золото'")
    await message.answer("💰 Оценить своё золото можно тут:\nhttps://goldexrobot.ru/calc")

@dp.message_handler(lambda message: message.text == "🛒 Купить слиток")
async def buy_bullion(message: types.Message):
    logger.info(f"Пользователь {message.from_user.id} выбрал 'Купить слиток'")
    keyboard = types.InlineKeyboardMarkup()
    keyboard.add(types.InlineKeyboardButton("🛒 Заказать", url="https://investingold.club/buy-bullions"))
    await message.answer("Выберите действие:", reply_markup=keyboard)

@dp.message_handler(lambda message: message.text == "📤 Продать слитки")
async def sell_bullion(message: types.Message):
    logger.info(f"Пользователь {message.from_user.id} выбрал 'Продать слитки'")
    keyboard = types.InlineKeyboardMarkup()
    keyboard.add(types.InlineKeyboardButton("📤 Продать", url="https://investingold.club/buy-bullions"))
    await message.answer("Выберите действие:", reply_markup=keyboard)

async def on_startup(app):
    webhook_url = f"https://{os.getenv('RENDER_EXTERNAL_HOSTNAME')}{WEBHOOK_PATH}"
    await bot.set_webhook(webhook_url, secret_token=WEBHOOK_SECRET)
    logger.info(f"✅ Webhook установлен: {webhook_url}")

async def on_shutdown(app):
    await bot.delete_webhook()
    await bot.session.close()

async def handle_webhook(request):
    if request.headers.get("X-Telegram-Bot-Api-Secret-Token") != WEBHOOK_SECRET:
        return web.Response(status=403)
    update = await request.json()
    await dp.feed_update(bot, types.Update(**update))
    return web.Response()

def main():
    app = web.Application()
    app.router.add_post(WEBHOOK_PATH, handle_webhook)
    app.on_startup.append(on_startup)
    app.on_shutdown.append(on_shutdown)
    web.run_app(app, host=WEBAPP_HOST, port=WEBAPP_PORT)

if __name__ == '__main__':
    main()
