import os
import logging
from aiogram import Bot, Dispatcher, types
from aiogram.utils import executor

# Логирование (по желанию)
logging.basicConfig(level=logging.INFO)

API_TOKEN = os.getenv("BOT_TOKEN")
bot = Bot(token=API_TOKEN)
dp = Dispatcher(bot)

# Команда /start
@dp.message_handler(commands=['start'])
async def cmd_start(message: types.Message):
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
    await message.answer("📍 Найти ближайший золотомат можно тут:\nhttps://goldexrobot.ru/contacts")

# Оценить золото
@dp.message_handler(lambda message: message.text == "💰 Оценить золото")
async def calc_gold(message: types.Message):
    await message.answer("💰 Оценить своё золото можно тут:\nhttps://goldexrobot.ru/calc")

# Купить слиток
@dp.message_handler(lambda message: message.text == "🛒 Купить слиток")
async def buy_bullion(message: types.Message):
    keyboard = types.InlineKeyboardMarkup()
    keyboard.add(types.InlineKeyboardButton("🛒 Заказать", url="https://investingold.club/buy-bullions"))
    await message.answer("Выберите действие:", reply_markup=keyboard)

# Продать слитки
@dp.message_handler(lambda message: message.text == "📤 Продать слитки")
async def sell_bullion(message: types.Message):
    keyboard = types.InlineKeyboardMarkup()
    keyboard.add(types.InlineKeyboardButton("📤 Продать", url="https://investingold.club/buy-bullions"))
    await message.answer("Выберите действие:", reply_markup=keyboard)

# Удаление webhook перед стартом polling
async def on_startup(dp):
    await bot.delete_webhook()
    logging.info("✅ Webhook удалён, бот работает через long polling.")

if __name__ == '__main__':
    executor.start_polling(dp, skip_updates=True, on_startup=on_startup)
