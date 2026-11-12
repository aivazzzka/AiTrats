# Публикация AiTrats (PWA, GitHub Pages / статический хостинг)

AiTrats разворачивается как статический сайт через GitHub-репозиторий. Фронтенд публикуется на **GitHub Pages** (или другом статическом хостинге без привязки к Netlify). Бэкенд-бот (Telegram) разворачивается и управляется отдельно.

`index.html`, `manifest.json`, `sw.js`, папка `icons/` используют относительные пути (`./`), Service Worker регистрируется как `./sw.js` и работает в HTTPS-окружении (например, GitHub Pages).

> Для веб/PWA нужны файлы фронтенда из этой папки. `FinanceDashboard.exe` — отдельная десктоп-версия для Windows, на статический хостинг его выкладывать не обязательно.

## GitHub Pages (через GitHub-репозиторий)
1. Создайте репозиторий на GitHub и загрузите содержимое фронтенда (в корне публикации должны быть `index.html`, `manifest.json`, `sw.js`, `icons/`, `.nojekyll` и при необходимости `DEPLOY.md`):
   ```bash
   git init
   git add index.html manifest.json sw.js icons .nojekyll DEPLOY.md
   git commit -m "Deploy Finance Tracker PWA"
   git branch -M main
   git remote add origin https://github.com/<USER>/<REPO>.git
   git push -u origin main
   ```
2. В GitHub: **Settings → Pages → Build and deployment** → Source: *Deploy from a branch*, Branch: `main` / `/ (root)` → Save.
3. После публикации сайт будет доступен по HTTPS: `https://<USER>.github.io/<REPO>/`
4. Откройте ссылку на iPhone/ПК. На iPhone: Safari → «Поделиться» → «На экран „Домой“».

Данные хранятся локально в браузере каждого устройства; для переноса используйте **Экспорт/Импорт (JSON)** в «Настройках» (и/или облачную синхронизацию Supabase, если настроена).

## Telegram Web App
- Укажите URL опубликованного фронтенда (GitHub Pages) в `WEBAPP_URL` для Telegram-бота (`telegram-bot/bot.py`, переменная окружения).
- Для кнопки Telegram Web App требуется действительная HTTPS-ссылка.

## Проверка PWA
- DevTools → Application: **Manifest** и **Service Worker** определяются без ошибок (на HTTPS).
- После первой загрузки ресурсы кэшируются SW — приложение открывается офлайн. При обновлении файлов меняйте версию `CACHE_NAME` в `sw.js`, чтобы клиенты получили новый кэш.
- Установка на iPhone: через Safari → «Поделиться» → «На экран „Домой“».
- Пути к файлам и иконкам относительные (`./`, `icons/...`), регистрация SW — `./sw.js`, поэтому публикация работает и в корне домена, и в подпапке (GitHub Pages project site).
