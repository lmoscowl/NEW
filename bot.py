import os
from aiogram import Bot, Dispatcher, types
from aiogram.utils.executor import start_webhook

API_TOKEN = os.getenv("BOT_TOKEN")
WEBHOOK_HOST = os.getenv("WEBHOOK_HOST")  # https://твой-рендер-домен.onrender.com
WEBHOOK_PATH = f"/webhook/{API_TOKEN}"
WEBHOOK_URL = f"{WEBHOOK_HOST}{WEBHOOK_PATH}"

PORT = int(os.environ.get("PORT", 10000))

bot = Bot(token=API_TOKEN)
dp = Dispatcher(bot)


@dp.message_handler(commands=['start'])
async def cmd_start(message: types.Message):
    keyboard = types.ReplyKeyboardMarkup(resize_keyboard=True)
    buttons = ["📍 Найти золотомат", "💰 Оценить золото", 
    "🛒 Купить слиток", "📤 Продать слитки"]
    keyboard.add(*buttons)
    await message.answer("👋 Добро пожаловать в GOLDEXROBOT!!\nВыберите действие:", reply_markup=keyboard)


@dp.message_handler(lambda message: message.text == "📍 Найти золотомат")
async def find_terminal(message: types.Message):
    await message.answer("📍 Найти ближайший золотомат можно тут:\nhttps://goldexrobot.ru/contacts")


@dp.message_handler(lambda message: message.text == "💰 Оценить золото")
async def calc_gold(message: types.Message):
    await message.answer("💰 Оценить своё золото можно тут:\nhttps://goldexrobot.ru/calc")


@dp.message_handler(lambda message: message.text == "🛒 Купить слиток")
async def buy_bullion(message: types.Message):
    keyboard = types.InlineKeyboardMarkup()
    keyboard.add(types.InlineKeyboardButton("🛒 Заказать", url="https://investingold.club/buy-bullions"))
    await message.answer("Выберите действие:", reply_markup=keyboard)


@dp.message_handler(lambda message: message.text == "📤 Продать слитки")
async def sell_bullion(message: types.Message):
    keyboard = types.InlineKeyboardMarkup()
    keyboard.add(types.InlineKeyboardButton("📤 Продать", url="https://investingold.club/buy-bullions"))
    await message.answer("Выберите действие:", reply_markup=keyboard)


# Webhook startup
async def on_startup(dp):
    await bot.set_webhook(WEBHOOK_URL)


# Webhook shutdown
async def on_shutdown(dp):
    await bot.delete_webhook()


if __name__ == '__main__':
    start_webhook(
        dispatcher=dp,
        webhook_path=WEBHOOK_PATH,
        on_startup=on_startup,
        on_shutdown=on_shutdown,
        skip_updates=True,
        host='0.0.0.0',
        port=PORT,
    )
    
