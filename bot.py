# 🔥 Phoenix Family Bot
# Python 3.10 | aiogram 2.25.1

import logging
import json
import os
import asyncio
from aiogram import Bot, Dispatcher, executor, types
from aiogram.types import ReplyKeyboardMarkup, KeyboardButton, InputFile

# ================== CONFIG ==================
BOT_TOKEN = "7717452722:AAHqnnuLbP2ptK7I_WWPVHkDQv650uQlfe8"
ADMIN_ID = 5239669503

DATA_DIR = "data"
IMAGES_DIR = "images"
NEWS_FILE = f"{DATA_DIR}/news.json"

os.makedirs(DATA_DIR, exist_ok=True)
os.makedirs(IMAGES_DIR, exist_ok=True)

if not os.path.exists(NEWS_FILE):
    with open(NEWS_FILE, "w", encoding="utf-8") as f:
        json.dump([], f)

# ================== BOT INIT ==================
logging.basicConfig(level=logging.INFO)
bot = Bot(token=BOT_TOKEN, parse_mode="HTML")
dp = Dispatcher(bot)

# ================== KEYBOARDS ==================
def main_menu():
    kb = ReplyKeyboardMarkup(resize_keyboard=True)
    kb.add(
        KeyboardButton("🏠 Инфо о фаме"),
        KeyboardButton("📢 Новости"),
    )
    kb.add(
        KeyboardButton("🔗 Наши ресурсы"),
        KeyboardButton("💬 Support"),
    )
    return kb


def info_menu():
    kb = ReplyKeyboardMarkup(resize_keyboard=True)
    kb.add(
        KeyboardButton("🚗 Автопарк"),
        KeyboardButton("🏡 Дом"),
    )
    kb.add(
        KeyboardButton("⬅️ Назад"),
    )
    return kb

# ================== START ==================
@dp.message_handler(commands=["start"])
async def start(message: types.Message):
    await message.answer(
        "🦅🔥 <b>Phoenix Family Bot</b> 🔥🦅\n\n"
        "Официальный Telegram-бот семьи <b>Phoenix Family</b>\n"
        "Используй кнопки внизу 👇",
        reply_markup=main_menu()
    )

# ================== INFO ==================
@dp.message_handler(lambda m: m.text == "🏠 Инфо о фаме")
async def info(message: types.Message):
    await message.answer(
        "🦅🔥 <b>Phoenix Family</b> 🔥🦅\n\n"
        "👑 <b>Лидер:</b> Kyle Morris\n"
        "🛠 <b>Тех. поддержка бота:</b> Tyler Rockwell\n\n"
        "🌳 <b>Парк:</b> Присутствует\n"
        "📌 <b>Статус:</b> RP Family\n\n"
        "Выбери пункт ниже 👇",
        reply_markup=info_menu()
    )

# ================== HOUSE ==================
@dp.message_handler(lambda m: m.text == "🏡 Дом")
async def house(message: types.Message):
    path = "images/house.jpg"
    if os.path.exists(path):
        await message.answer_photo(
            InputFile(path),
            caption=(
                "🏡 <b>Дом Phoenix Family</b>\n\n"
                "📍 Локация: Los Santos\n"
                "🔐 Закрытая территория семьи\n"
                "🦅 Только для участников Phoenix Family"
            ),
            reply_markup=info_menu()
        )
    else:
        await message.answer(
            "❌ Фото дома не найдено",
            reply_markup=info_menu()
        )

# ================== CARS ==================
@dp.message_handler(lambda m: m.text == "🚗 Автопарк")
async def cars(message: types.Message):
    await message.answer("🚗 Загружаю автопарк, подожди немного ⏳")

    cars_data = [
        ("BMW M5 F90", "images/BMW M5 F90.jpg"),
        ("Mercedes-Benz CLS AMG", "images/Mercedes-Benz CLS AMG.jpg"),
        ("BMW M1000RR", "images/BMW M1000RR.jpg"),
        ("Lamborghini Huracan", "images/Lamborghini Huracan.jpg"),
        ("BMW X7M", "images/BMW X7M.jpg"),
    ]

    for name, path in cars_data:
        if os.path.exists(path):
            await message.answer_photo(
                InputFile(path),
                caption=f"🔥 <b>{name}</b>"
            )
            await asyncio.sleep(1.2)  # ⬅️ ПАУЗА
        else:
            await message.answer(f"❌ Фото не найдено: {name}")

# ================== NEWS ==================
@dp.message_handler(lambda m: m.text == "📢 Новости")
async def news(message: types.Message):
    text = (
        "🔥 <b>Открытие официального Telegram-бота Phoenix Family</b> 🔥\n\n"
        "Сегодня мы делаем важный шаг вперёд — официально запущен Telegram-бот "
        "<b>Phoenix Family</b>.\n\n"
        "📈 Phoenix Family уверенно развивается, усиливает структуру и "
        "расширяет возможности для каждого участника.\n\n"
        "💼 В боте вы сможете:\n"
        "• следить за новостями семьи\n"
        "• получать важную информацию\n"
        "• быть в курсе всех обновлений\n\n"
        "🚀 Phoenix Family — выше, сильнее, организованнее."
    )

    img = "images/news_opening.jpg"
    if os.path.exists(img):
        await message.answer_photo(
            InputFile(img),
            caption=text,
            reply_markup=main_menu()
        )
    else:
        await message.answer(text, reply_markup=main_menu())

# ================== LINKS ==================
@dp.message_handler(lambda m: m.text == "🔗 Наши ресурсы")
async def links(message: types.Message):
    await message.answer(
        "🔗 <b>Ресурсы Phoenix Family</b>\n\n"
        "📘 VK паблик:\nhttps://vk.ru/phoenix_orp\n\n"
        "🧵 Форум:\nhttps://forum.gta-mobile.ru/threads/1130935/",
        reply_markup=main_menu()
    )

# ================== SUPPORT ==================
@dp.message_handler(lambda m: m.text == "💬 Support")
async def support(message: types.Message):
    await message.answer(
        "💬 Напиши свой вопрос одним сообщением.\n"
        "Он будет передан тех. поддержке 👑",
        reply_markup=main_menu()
    )

@dp.message_handler(lambda m: m.text not in [
    "🏠 Инфо о фаме",
    "🚗 Автопарк",
    "🏡 Дом",
    "📢 Новости",
    "🔗 Наши ресурсы",
    "💬 Support",
    "⬅️ Назад"
] and not m.text.startswith("/"))
async def handle_support(message: types.Message):
    await bot.send_message(
        ADMIN_ID,
        f"📩 <b>Вопрос от игрока</b>\n"
        f"👤 @{message.from_user.username}\n\n"
        f"💬 {message.text}"
    )
    await message.answer("✅ Вопрос отправлен 👑", reply_markup=main_menu())

# ================== BACK ==================
@dp.message_handler(lambda m: m.text == "⬅️ Назад")
async def back(message: types.Message):
    await message.answer(
        "🏠 <b>Главное меню</b>",
        reply_markup=main_menu()
    )

# ================== RUN ==================
if __name__ == "__main__":
    executor.start_polling(dp, skip_updates=True)

