# Telegram-бот AiTrats (aiogram)

Простой бот, который по команде `/start` отправляет приветствие и кнопку **«Открыть AiTrats»** (Telegram Web App).

## Файлы
- `bot.py` — код бота
- `requirements.txt` — зависимости

## Переменные окружения
- `BOT_TOKEN` — токен Telegram-бота (от @BotFather) **обязательно**
- `WEBAPP_URL` — HTTPS-ссылка на опубликованный веб-интерфейс (например, GitHub Pages), по умолчанию `https://<username>.github.io/<repo>/`

> Для Telegram Web App кнопки требуется действительная HTTPS-ссылка на фронтенд.

## Локальный запуск
```bash
python -m venv .venv
# Windows: .venv\Scripts\activate
# Linux/macOS: source .venv/bin/activate
pip install -r requirements.txt

# Windows (PowerShell)
$env:BOT_TOKEN="YOUR_TELEGRAM_BOT_TOKEN"
$env:WEBAPP_URL="https://<username>.github.io/<repo>/"
python bot.py

# Linux/macOS
export BOT_TOKEN="YOUR_TELEGRAM_BOT_TOKEN"
export WEBAPP_URL="https://<username>.github.io/<repo>/"
python bot.py
```

## Деплой (Render / Railway)
1. Загрузите папку проекта в репозиторий или подключите её к сервису.
2. Укажите команду запуска: `python bot.py` (Worker/Background Service).
3. Установите зависимости: `pip install -r requirements.txt`.
4. Добавьте переменные окружения `BOT_TOKEN` и `WEBAPP_URL`.

Бот использует long polling (`start_polling`), отдельный веб-сервер не требуется.
