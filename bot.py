import os
from aiogram import Bot, Dispatcher, types
from aiogram.utils import executor

API_TOKEN = os.getenv("BOT_TOKEN")

bot = Bot(token=API_TOKEN)
dp = Dispatcher(bot)

# Полный список золотоматов
zolotomats = [
    {
        "address": "Москва, ТРЦ Афимолл Сити, Пресненская наб., 2",
        "hours": "10:00–22:00",
        "map_link": "https://yandex.ru/maps/-/CDaXq04R"
    },
    {
        "address": "Москва, ТРЦ Авиапарк, Ходынский б-р, 4",
        "hours": "10:00–22:00",
        "map_link": "https://yandex.ru/maps/-/CDaXq0TY"
    },
    {
        "address": "Москва, ТЦ Европейский, пл. Киевского вокзала, 2",
        "hours": "10:00–22:00",
        "map_link": "https://yandex.ru/maps/-/CDaXq0E8"
    },
    # 19 остальных
    {
        "address": "Москва, ТЦ Метрополис, Ленинградское ш., 16А, стр. 4",
        "hours": "10:00–22:00",
        "map_link": "https://yandex.ru/maps/-/CDaXq0HT"
    },
    {
        "address": "Санкт-Петербург, ТРЦ Галерея, Лиговский пр., 30А",
        "hours": "10:00–22:00",
        "map_link": "https://yandex.ru/maps/-/CDaXq0PG"
    },
    {
        "address": "Санкт-Петербург, ТРЦ Невский центр, Невский пр., 114-116",
        "hours": "10:00–22:00",
        "map_link": "https://yandex.ru/maps/-/CDaXq0g3"
    },
    {
        "address": "Казань, ТЦ Кольцо, ул. Петербургская, 1",
        "hours": "10:00–22:00",
        "map_link": "https://yandex.ru/maps/-/CDaXq01v"
    },
    {
        "address": "Казань, ТРЦ Мега, Проспект Победы, 141",
        "hours": "10:00–22:00",
        "map_link": "https://yandex.ru/maps/-/CDaXq0oR"
    },
    {
        "address": "Екатеринбург, ТРЦ Гринвич, ул. 8 Марта, 46",
        "hours": "10:00–22:00",
        "map_link": "https://yandex.ru/maps/-/CDaXq0vU"
    },
    {
        "address": "Екатеринбург, ТЦ Пассаж, ул. Вайнера, 9",
        "hours": "10:00–22:00",
        "map_link": "https://yandex.ru/maps/-/CDaXq05L"
    },
    {
        "address": "Ростов-на-Дону, ТРЦ Горизонт, пр. Михаила Нагибина, 32/2",
        "hours": "10:00–22:00",
        "map_link": "https://yandex.ru/maps/-/CDaXq0Bo"
    },
    {
        "address": "Новосибирск, ТРЦ Галерея Новосибирск, ул. Военная, 5",
        "hours": "10:00–22:00",
        "map_link": "https://yandex.ru/maps/-/CDaXq0A4"
    },
    {
        "address": "Краснодар, ТРЦ Красная Площадь, ул. Уральская, 79/1",
        "hours": "10:00–22:00",
        "map_link": "https://yandex.ru/maps/-/CDaXq0dS"
    },
    {
        "address": "Красноярск, ТРЦ Планета, ул. 9 Мая, 77",
        "hours": "10:00–22:00",
        "map_link": "https://yandex.ru/maps/-/CDaXq0bV"
    },
    {
        "address": "Воронеж, ТРЦ Галерея Чижова, ул. Куцыгина, 5А",
        "hours": "10:00–22:00",
        "map_link": "https://yandex.ru/maps/-/CDaXq0wW"
    },
    {
        "address": "Уфа, ТРЦ Планета, ул. Энтузиастов, 20",
        "hours": "10:00–22:00",
        "map_link": "https://yandex.ru/maps/-/CDaXq0lp"
    },
    {
        "address": "Самара, ТРЦ Мега, Московское ш., 108 км",
        "hours": "10:00–22:00",
        "map_link": "https://yandex.ru/maps/-/CDaXq0rP"
    },
    {
        "address": "Пермь, ТРЦ Семья, ул. Революции, 13",
        "hours": "10:00–22:00",
        "map_link": "https://yandex.ru/maps/-/CDaXq00b"
    },
    {
        "address": "Челябинск, ТРЦ Горки, ул. Артиллерийская, 136",
        "hours": "10:00–22:00",
        "map_link": "https://yandex.ru/maps/-/CDaXq0YL"
    },
    {
        "address": "Иркутск, ТРЦ Модный Квартал, ул. 3 Июля, 25",
        "hours": "10:00–22:00",
        "map_link": "https://yandex.ru/maps/-/CDaXq0T9"
    },
    {
        "address": "Тюмень, ТРЦ Кристалл, ул. Мельникайте, 137",
        "hours": "10:00–22:00",
        "map_link": "https://yandex.ru/maps/-/CDaXq0NC"
    },
    {
        "address": "Омск, ТРЦ Мега, пр. Королева, 1",
        "hours": "10:00–22:00",
        "map_link": "https://yandex.ru/maps/-/CDaXq09X"
    }
]


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
    await message.answer("👋 Добро пожаловать!\nВыберите действие:", reply_markup=keyboard)


@dp.message_handler(lambda message: message.text == "📍 Найти золотомат")
async def find_terminal(message: types.Message):
    for z in zolotomats:
        keyboard = types.InlineKeyboardMarkup()
        keyboard.add(types.InlineKeyboardButton("📍 Показать на карте", url=z["map_link"]))
        await message.answer(f"<b>📍 {z['address']}</b>\n🕑 {z['hours']}", reply_markup=keyboard, parse_mode="HTML")


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


if __name__ == '__main__':
    executor.start_polling(dp, skip_updates=True)
