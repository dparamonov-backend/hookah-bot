from aiogram.types import (
    InlineKeyboardMarkup, InlineKeyboardButton,
    ReplyKeyboardMarkup, KeyboardButton,
)


# ── Большие описания ──

menu = """🔥 Добро пожаловать в наш кальянный магазин!

У нас ты найдёшь всё для идеального вечера:
🌿 Табаки премиум-класса
🔥 Кокосовые и натуральные угли
💨 Готовые сборки от наших мастеров
🎁 Приятные бонусы постоянным клиентам

Что тебя интересует сегодня? 👇
"""

standart = """🥉 Кальян Standart
Цена: 1990 RUB
Срок: готов к выдаче сегодня

Что входит:
🔥 Кальян в сборе
🌿 Табак на выбор (2 вкуса)
💨 Угли на одну заправку
📦 Чистые шланги и мундштуки

Отличный выбор для уютного вечера с друзьями.
Ничего не нужно докупать — просто забирай и кури 👇
"""

premium = """👑 Кальян Premium
Цена: 2390 RUB
Срок: готов к выдаче сегодня

Что входит:
🔥 Кальян премиум-класса в сборе
🌿 Табак премиум-сегмента (3 вкуса на выбор)
💨 Кокосовые угли премиум
📦 Полный набор аксессуаров
🎁 Приятный бонус от заведения

Для тех, кто ценит качество и плотный, насыщенный дым.
Идеально для особого вечера 👇
"""

dostavka = """🚚 Доставка

Курьер привезёт заказ прямо к твоей двери.

⏱ Время: 40–60 минут
📍 Зона: в пределах города
💳 Оплата: при получении или онлайн

Укажи номер телефона — и мы свяжемся для уточнения деталей 👇
"""

samovyvoz = """🏠 Самовывоз

Забери заказ сам в удобное время.

📍 Адрес: ул. Примерная, 15
⏱ Работаем: с 12:00 до 23:00
💳 Оплата: на месте или онлайн

Оставь номер телефона — мы подтвердим, что всё готово 👇
"""

phone_text = """📞 Остался последний шаг!

Поделись номером телефона, чтобы мы могли:
✅ подтвердить заказ
✅ согласовать время и место
✅ связаться при необходимости

Нажми кнопку ниже или введи номер вручную 👇
"""

confirm_text = """Проверь заказ 🔍

Сейчас всё выглядит так:

📦 Комплект: {kit}
🚚 Способ: {delivery}
📞 Телефон: {phone}
💰 Итого: {total} ₽

Всё верно? Жми «Оплатить» 👇
"""

pay_text = """💳 Реквизиты для оплаты

Способ: СБП
Сумма: {total} RUB
Номер: 8 800 555 35 35
Банк: Сбербанк
ФИО: Дмитрий Шилло

После перевода нажми «Я оплатил» 👇
"""

paid_text = """🎉 Принято! Спасибо за заказ.

Менеджер свяжется с тобой в ближайшее время, чтобы подтвердить детали.

А пока — заваривай чай, мы всё привезём ☕🔥
"""

cancel_text = """Заказ отменён ✖️

Напиши /start, чтобы начать заново.
"""


# ── Инлайн-кнопки ──

start = InlineKeyboardMarkup(
    inline_keyboard=[
        [InlineKeyboardButton(text="🥉 Standart — 1990 ₽", callback_data="kit:standart")],
        [InlineKeyboardButton(text="👑 Premium — 2390 ₽",  callback_data="kit:premium")],
    ]
)

delivery = InlineKeyboardMarkup(
    inline_keyboard=[
        [InlineKeyboardButton(text="🚚 Доставка",  callback_data="delivery:1")],
        [InlineKeyboardButton(text="🏠 Самовывоз", callback_data="delivery:0")],
    ]
)

confirm = InlineKeyboardMarkup(
    inline_keyboard=[
        [InlineKeyboardButton(text="💳 Оплатить", callback_data="pay")],
        [InlineKeyboardButton(text="✖️ Отменить", callback_data="cancel")],
    ]
)

paid = InlineKeyboardMarkup(
    inline_keyboard=[
        [InlineKeyboardButton(text="✅ Я оплатил", callback_data="paid")],
        [InlineKeyboardButton(text="✖️ Отменить",  callback_data="cancel")],
    ]
)


# ── Reply-клавиатура ──

phone = ReplyKeyboardMarkup(
    keyboard=[[KeyboardButton(text="📱 Поделиться номером", request_contact=True)]],
    resize_keyboard=True,
    one_time_keyboard=True,
)