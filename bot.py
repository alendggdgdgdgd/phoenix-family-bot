# 🦅🔥 Phoenix Family Bot 🔥🦅
# Python 3.10 | aiogram 2.25.1 | Render Anti-Sleep

import os
import asyncio
import logging
from aiogram import Bot, Dispatcher, types
from aiogram.types import InlineKeyboardMarkup, InlineKeyboardButton, InputFile
from aiohttp import web

# ================== CONFIG ==================
BOT_TOKEN = os.getenv("BOT_TOKEN")
ADMIN_ID = int(os.getenv("ADMIN_ID"))

logging.basicConfig(level=logging.INFO)

bot = Bot(token=BOT_TOKEN, parse_mode="HTML")
dp = Dispatcher(bot)

# ================== KEYBOARDS ==================
def main_menu():
    return InlineKeyboardMarkup(row_width=1).add(
        InlineKeyboardButton("🏠 Инфо о фаме", callback_data="info"),
        InlineKeyboardButton("📢 Новости", callback_data="news"),
        InlineKeyboardButton("🔗 Наши ресурсы", callback_data="links"),
        InlineKeyboardButton("💬 Задать вопрос", callback_data="support")
    )

def back_menu():
    return InlineKeyboardMarkup().add(
        InlineKeyboardButton("⬅️ Назад", callback_data="back")
    )

# ================== START ==================
@dp.message_handler(commands=["start"])
async def start(message: types.Message):
    await message.answer(
        "🦅🔥 <b>Phoenix Family Bot</b> 🔥🦅\n\n"
        "Официальный Telegram-бот семьи <b>Phoenix Family</b> 🔥\n\n"
        "Здесь ты найдёшь:\n"
        "• 📢 новости семьи\n"
        "• 🏠 информацию о доме и автопарке\n"
        "• 🔗 официальные ресурсы\n"
        "• 💬 связь с тех. поддержкой\n\n"
        "🚀 <i>Phoenix Family — выше, сильнее, организованнее</i>",
        reply_markup=main_menu()
    )

# ================== INFO ==================
@dp.callback_query_handler(lambda c: c.data == "info")
async def info(call: types.CallbackQuery):
    kb = InlineKeyboardMarkup(row_width=1).add(
        InlineKeyboardButton("🚗 Автопарк", callback_data="cars"),
        InlineKeyboardButton("🏡 Дом", callback_data="house"),
        InlineKeyboardButton("⬅️ Назад", callback_data="back")
    )

    await call.message.edit_text(
        "🏠 <b>Информация о Phoenix Family</b>\n\n"
        "👑 <b>Лидер:</b> Kyle Morris\n"
        "🛠 <b>Тех. поддержка бота:</b> Tyler Rockwell\n"
        "🌍 <b>Сервер:</b> Online RP\n\n"
        "👇 Выбери раздел ниже",
        reply_markup=kb
    )

# ================== AUTOPARK ==================
@dp.callback_query_handler(lambda c: c.data == "cars")
async def cars(call: types.CallbackQuery):
    await call.message.answer("🚗 <b>Загружаю автопарк, подожди немного ⏳</b>")

    cars = [
        ("BMW M5 F90", "images/BMW M5 F90.jpg"),
        ("Mercedes-Benz CLS AMG", "images/Mercedes-Benz CLS AMG.jpg"),
        ("BMW M1000RR", "images/BMW M1000RR.jpg"),
        ("Lamborghini Huracan", "images/Lamborghini Huracan.jpg"),
        ("BMW X7M", "images/BMW X7M.jpg"),
    ]

    for name, path in cars:
        if os.path.exists(path):
            await bot.send_photo(
                call.from_user.id,
                InputFile(path),
                caption=f"🔥 <b>{name}</b>"
            )
            await asyncio.sleep(1.2)  # пауза между фото
        else:
            await bot.send_message(call.from_user.id, f"❌ Фото не найдено: {name}")

# ================== HOUSE ==================
@dp.callback_query_handler(lambda c: c.data == "house")
async def house(call: types.CallbackQuery):
    path = "images/house.jpg"
    if os.path.exists(path):
        await bot.send_photo(
            call.from_user.id,
            InputFile(path),
            caption="🏡 <b>Дом Phoenix Family</b>\n\n"
                    "Основная база семьи 🔥"
        )
    else:
        await bot.send_message(call.from_user.id, "❌ Фото дома не найдено")

# ================== NEWS ==================
@dp.callback_query_handler(lambda c: c.data == "news")
async def news(call: types.CallbackQuery):
    path = "images/news_opening.jpg"
    text = (
        "🔥 <b>Открытие официального Telegram-бота Phoenix Family</b> 🔥\n\n"
        "Сегодня мы делаем важный шаг вперёд — официально запущен Telegram-бот Phoenix Family.\n\n"
        "📈 Phoenix Family не стоит на месте — мы развиваемся и усиливаем структуру.\n\n"
        "💼 В боте вы сможете:\n"
        "• следить за новостями семьи\n"
        "• получать важную информацию\n"
        "• быть в курсе обновлений\n\n"
        "🚀 <i>Это только начало.</i>"
    )

    if os.path.exists(path):
        await bot.send_photo(call.from_user.id, InputFile(path), caption=text)
    else:
        await bot.send_message(call.from_user.id, text)

# ================== LINKS ==================
@dp.callback_query_handler(lambda c: c.data == "links")
async def links(call: types.CallbackQuery):
    await call.message.edit_text(
        "🔗 <b>Наши ресурсы</b>\n\n"
        "📘 <a href='https://vk.ru/phoenix_orp'>VK паблик</a>\n"
        "🧵 <a href='https://forum.gta-mobile.ru/threads/1130935/'>Форум</a>",
        reply_markup=back_menu()
    )

# ================== SUPPORT ==================
@dp.callback_query_handler(lambda c: c.data == "support")
async def support(call: types.CallbackQuery):
    await call.message.edit_text(
        "💬 <b>Задать вопрос</b>\n\n"
        "✍️ Напиши свой вопрос одним сообщением — он будет передан лидеру 👑",
        reply_markup=back_menu()
    )

@dp.message_handler()
async def support_message(message: types.Message):
    if message.text == "⬅️ Назад":
        return

    await bot.send_message(
        ADMIN_ID,
        f"📩 <b>Вопрос от игрока</b>\n"
        f"👤 @{message.from_user.username}\n\n"
        f"💬 {message.text}"
    )
    await message.answer("✅ Вопрос отправлен лидеру 👑")

# ================== BACK ==================
@dp.callback_query_handler(lambda c: c.data == "back")
async def back(call: types.CallbackQuery):
    await call.message.edit_text(
        "🏠 <b>Главное меню</b>\nВыбери раздел 👇",
        reply_markup=main_menu()
    )

# ================== ANTI-SLEEP WEB ==================
async def healthcheck(request):
    return web.Response(text="Phoenix Family Bot is alive 🔥")

async def start_web():
    app = web.Application()
    app.router.add_get("/", healthcheck)
    runner = web.AppRunner(app)
    await runner.setup()
    site = web.TCPSite(runner, "0.0.0.0", 8080)
    await site.start()

async def main():
    await start_web()
    await dp.start_polling()

if __name__ == "__main__":
    asyncio.run(main())



