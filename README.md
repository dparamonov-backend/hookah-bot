# Hookah Rental Telegram Bot 🚬

Telegram-бот для автоматизации услуг аренды кальянов. Проект написан на Python с использованием асинхронного фреймворка Aiogram 3.x.

## 🚀 Функционал
*   Пошаговое оформление заказа через FSM (Finite State Machine).
*   Выбор комплектации (Standard / Premium).
*   Выбор способа получения (Доставка / Самовывоз).
*   Сбор контактных данных пользователя (номер телефона).
*   Сохранение заказов в базу данных SQLite.
*   Админ панель с принятием заявок


## 🛠 Стек технологий
*   **Язык:** Python 3.x
*   **Фреймворк:** Aiogram 3.x
*   **База данных:** SQLite (с использованием чистого SQL / SQLAlchemy)
*   **Инструменты:** Git, PyCharm

## 📦 Установка и запуск

1. **Клонируйте репозиторий:**
   ```bash
   git clone https://github.com/dparamonov-backend/hookah-bot.git
   cd hookah-bot

   python -m venv venv

# Для Windows:
venv\Scripts\activate
# Для macOS/Linux:
source venv/bin/activate


Установите зависимости:

pip install -r requirements.txt


Настройте конфигурацию:

Создайте файл config.py в корне проекта.

Добавьте туда токен вашего бота, полученный от @BotFather:

api_key = "ВАШ_ТОКЕН_БОТА"

Запустите бота:

python run.py


📂 Структура проекта
run.py — точка входа, запуск бота.

config.py — файл с секретными данными (токен).

comma/ — основная папка с логикой бота (handlers, keyboards, states, db).

db.py — модуль для работы с базой данных.


🗺 Планы по развитию (Roadmap)
□ Перевод базы данных на PostgreSQL.
□ Интеграция SQLAlchemy ORM.
□ Разработка REST API на FastAPI для связи с мобильным приложением.
□ Контейнеризация проекта через Docker.


📫 Контакты
Автор: Дмитрий Парамонов

Email: dmitriy.paramonov.dev@yandex.ru





