import logging
from aiogram import Bot, Dispatcher, types
from aiogram.types import ParseMode
from aiogram.utils import executor
import requests

API_TOKEN = '7931009664:AAHwqyiEOSkuGEvCZ1iSCUtUiELBMT9Po7Q'  # Замените на ваш API токен бота
ADMIN_CHAT_ID = '@lmoscowl77'  # Чат для уведомлений

logging.basicConfig(level=logging.INFO)
bot = Bot(token=API_TOKEN)
dp = Dispatcher(bot)

# Главное меню без "Мои заявки"
main_menu = types.ReplyKeyboardMarkup(resize_keyboard=True)
main_menu.add('📍 Найти золотомат', '💰 Оценить золото')
main_menu.add('🛒 Купить слиток', '📤 Продать слитки')

# Функции обработки команд

@dp.message_handler(commands=['start'])
async def send_welcome(message: types.Message):
    await message.answer("👋 Добро пожаловать!\nВыберите действие:", reply_markup=main_menu)

@dp.message_handler(lambda message: message.text == '📍 Найти золотомат')
async def find_zolotomat(message: types.Message):
    await message.answer("Перейдите по ссылке, чтобы найти золотомат: https://goldexrobot.ru/contacts")

@dp.message_handler(lambda message: message.text == '💰 Оценить золото')
async def calc_gold(message: types.Message):
    await message.answer("Перейдите по ссылке для расчёта: https://goldexrobot.ru/calc")

@dp.message_handler(lambda message: message.text == '🛒 Купить слиток')
async def buy_bullion(message: types.Message):
    await message.answer("Перейдите по ссылке для покупки: https://investingold.club/buy-bullions\n\n"
                         "Пожалуйста, напишите сюда ваш контакт (телефон или имя), чтобы мы могли связаться.")

@dp.message_handler(lambda message: message.text == '📤 Продать слитки')
async def sell_bullion(message: types.Message):
    await message.answer("Перейдите по ссылке для продажи: https://investingold.club/buy-bullions\n\n"
                         "Пожалуйста, напишите сюда ваш контакт (телефон или имя), чтобы мы могли связаться.")

@dp.message_handler()
async def handle_contact(message: types.Message):
    # Любое сообщение пользователя считается заявкой
    if message.text:
        contact_info = message.text
        await bot.send_message(ADMIN_CHAT_ID, f"Новая заявка от {message.from_user.full_name} ({message.from_user.id}):\n{contact_info}")
        await message.answer("Спасибо! Ваш контакт отправлен менеджеру.")
    else:
        await message.answer("Что-то пошло не так. Попробуйте ещё раз.")

if __name__ == '__main__':
    executor.start_polling(dp, skip_updates=True)
