
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

# Главное меню
main_menu = types.ReplyKeyboardMarkup(resize_keyboard=True)
main_menu.add('📍 Найти золотомат', '💰 Оценить золото', '🛒 Купить слиток', '📤 Продать слитки', '👤 Мои заявки')

# Функции обработки команд

@dp.message_handler(commands=['start'])
async def send_welcome(message: types.Message):
    await message.answer("👋 Добро пожаловать в GOLDEXROBOT!\nВыберите действие:", reply_markup=main_menu)

@dp.message_handler(lambda message: message.text == '📍 Найти золотомат')
async def find_zolotomat(message: types.Message):
    await message.answer("Перейдите по ссылке, чтобы найти золотомат: https://goldexrobot.ru/contacts")

@dp.message_handler(lambda message: message.text == '💰 Оценить золото')
async def calc_gold(message: types.Message):
    await message.answer("Перейдите по ссылке для расчёта: https://goldexrobot.ru/calc")

@dp.message_handler(lambda message: message.text == '🛒 Купить слиток')
async def buy_bullion(message: types.Message):
    await message.answer("Перейдите по ссылке для покупки: https://investingold.club/buy-bullions\n\n"
                         "Пожалуйста, оставьте свой контакт (телефон), чтобы мы могли с вами связаться.")

@dp.message_handler(lambda message: message.text == '📤 Продать слитки')
async def sell_bullion(message: types.Message):
    await message.answer("Перейдите по ссылке для продажи: https://investingold.club/buy-bullions\n\n"
                         "Пожалуйста, оставьте свой контакт (телефон), чтобы мы могли с вами связаться.")

@dp.message_handler(lambda message: message.text == '👤 Мои заявки')
async def my_requests(message: types.Message):
    await message.answer("Ваши заявки:\n\n- Заявка 1: покупка слитка\n- Заявка 2: продажа золота\n\n"
                         "Заявки отображаются по вашей сессии. Если нужно больше, пишите!")

@dp.message_handler()
async def handle_contact(message: types.Message):
    # Если это контакт для заявки, отправляем менеджеру
    if message.text:
        contact_info = message.text
        # Отправляем уведомление менеджеру
        await bot.send_message(ADMIN_CHAT_ID, f"Новая заявка от {message.from_user.full_name} ({message.from_user.id}):\n{contact_info}")
        await message.answer("Ваш контакт успешно отправлен. Менеджер свяжется с вами.")
    else:
        await message.answer("Что-то пошло не так. Попробуйте ещё раз.")

if __name__ == '__main__':
    executor.start_polling(dp, skip_updates=True)
