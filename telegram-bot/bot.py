import asyncio
import logging
import os

from aiogram import Bot, Dispatcher, F
from aiogram.filters import CommandStart
from aiogram.types import InlineKeyboardButton, InlineKeyboardMarkup, Message, WebAppInfo

logging.basicConfig(level=logging.INFO)

BOT_TOKEN = os.getenv("BOT_TOKEN", "").strip()
WEBAPP_URL = os.getenv("WEBAPP_URL", "https://<username>.github.io/<repo>/").strip()


def get_webapp_keyboard() -> InlineKeyboardMarkup:
    return InlineKeyboardMarkup(
        inline_keyboard=[
            [
                InlineKeyboardButton(
                    text="Открыть AiTrats",
                    web_app=WebAppInfo(url=WEBAPP_URL),
                )
            ]
        ]
    )


dp = Dispatcher()


@dp.message(CommandStart())
async def cmd_start(message: Message) -> None:
    await message.answer(
        "Привет! 👋\n\n"
        "Это бот AiTrats. Нажмите кнопку ниже, чтобы открыть веб-интерфейс.",
        reply_markup=get_webapp_keyboard(),
    )


@dp.message(F.web_app_data)
async def handle_webapp_data(message: Message) -> None:
    # Зарезервировано для обработки данных, отправленных из Web App (если потребуется).
    await message.answer("Данные из приложения получены.")


async def main() -> None:
    if not BOT_TOKEN:
        raise RuntimeError(
            "Не задан BOT_TOKEN. Укажите токен бота в переменной окружения BOT_TOKEN."
        )
    if not WEBAPP_URL.startswith(("https://", "http://")):
        raise RuntimeError(
            "Некорректный WEBAPP_URL. Укажите ссылку на веб-интерфейс (GitHub Pages/статический хостинг)."
        )

    bot = Bot(token=BOT_TOKEN)
    await dp.start_polling(bot)


if __name__ == "__main__":
    asyncio.run(main())
