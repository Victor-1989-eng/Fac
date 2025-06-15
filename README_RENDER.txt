🔧 Как развернуть бот на Render без GitHub:

1. Перейди на https://render.com
2. Войди или зарегистрируйся
3. Нажми «New» → «Web Service»
4. Внизу найди ссылку "Deploy an empty web service" — нажми
5. Назови сервис как хочешь, выбери Python
6. Выбери ZIP-файл telegram_post_bot_for_render.zip и загрузи
7. Введи команды:
   - Build Command: pip install -r requirements.txt
   - Start Command: python main.py
8. Внизу добавь переменные:
   - TELEGRAM_TOKEN = токен от @BotFather
   - CHANNEL_ID = @твой_канал

9. Нажми «Create Web Service»
Готово! Бот будет публиковать пост в 07:00 утра по Киеву каждый день.
