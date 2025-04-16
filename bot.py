import os
import logging
from aiogram import Bot, Dispatcher, types
from aiogram.utils import executor

# Логирование
logging.basicConfig(level=logging.INFO)
logger = logging.getLogger(__name__)

# Токен бота из переменных окружения
API_TOKEN = os.getenv("BOT_TOKEN")

# Инициализация бота и диспетчера
bot = Bot(token=API_TOKEN)
dp = Dispatcher(bot)


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


if __name__ == '__main__':
    import asyncio

    async def on_startup():
        await bot.delete_webhook()
        logger.info("✅ Webhook удалён перед стартом long polling.")
        me = await bot.get_me()
        logger.info(f"🤖 Бот запущен: {me.full_name} [@{me.username}]")

    loop = asyncio.get_event_loop()
    loop.run_until_complete(on_startup())

    logger.info("🚀 Старт long polling...")
    executor.start_polling(dp, skip_updates=True)
