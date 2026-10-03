import logging
from pathlib import Path

from aiogram import F, Router, Bot
from aiogram.filters import CommandStart
from aiogram.fsm.context import FSMContext
from aiogram.types import Message, CallbackQuery, FSInputFile, ReplyKeyboardRemove

import comma.keyboard as kb
import comma.money as money
from comma.states import OrderStates
from config import ADMIN_ID


logger = logging.getLogger(__name__)
router = Router()
BASE_DIR = Path(__file__).parent


def find_photo(name: str) -> Path | None:
    for path in BASE_DIR.glob(name):
        return path
    return None


# ── /start ──

@router.message(CommandStart())
async def cmd_start(message: Message, state: FSMContext):
    await state.clear()
    photo_path = find_photo("start_photo.jpg")

    if photo_path:
        await message.answer_photo(
            photo=FSInputFile(photo_path),
            caption=kb.menu,
            reply_markup=kb.start,
        )
    else:
        await message.answer(kb.menu, reply_markup=kb.start)

    await state.set_state(OrderStates.choosing_kit)


# ── Шаг 1: комплект ──

@router.callback_query(OrderStates.choosing_kit, F.data.startswith("kit:"))
async def choose_kit(callback: CallbackQuery, state: FSMContext):
    kit = callback.data.split(":")[1]
    await state.update_data(kit=kit, total=money.PRICES[kit])

    text = kb.standart if kit == "standart" else kb.premium

    if callback.message.photo:
        await callback.message.edit_caption(caption=text, reply_markup=kb.delivery)
    else:
        await callback.message.edit_text(text=text, reply_markup=kb.delivery)

    await state.set_state(OrderStates.choosing_delivery)
    await callback.answer()


# ── Шаг 2: способ получения ──

@router.callback_query(OrderStates.choosing_delivery, F.data.startswith("delivery:"))
async def choose_delivery(callback: CallbackQuery, state: FSMContext):
    delivery = callback.data.split(":")[1] == "1"
    await state.update_data(delivery=delivery)

    text = kb.dostavka if delivery else kb.samovyvoz

    if callback.message.photo:
        await callback.message.edit_caption(caption=text, reply_markup=None)
    else:
        await callback.message.edit_text(text=text, reply_markup=None)

    await callback.message.answer(kb.phone_text, reply_markup=kb.phone)
    await state.set_state(OrderStates.waiting_phone)
    await callback.answer()


# ── Шаг 3: телефон кнопкой ──

@router.message(OrderStates.waiting_phone, F.contact)
async def get_phone_contact(message: Message, state: FSMContext):
    await state.update_data(phone=message.contact.phone_number)
    await _show_confirm(message, state)


# ── Шаг 3: телефон текстом ──

@router.message(OrderStates.waiting_phone, F.text)
async def get_phone_text(message: Message, state: FSMContext):
    phone = message.text.strip()
    cleaned = (
        phone.replace("+", "").replace("-", "").replace(" ", "")
        .replace("(", "").replace(")", "")
    )

    if not cleaned.isdigit() or len(cleaned) < 10:
        await message.answer("Похоже, это не номер. Введи ещё раз или нажми кнопку 👇")
        return

    await state.update_data(phone=phone)
    await _show_confirm(message, state)


async def _show_confirm(message: Message, state: FSMContext):
    data = await state.get_data()
    text = kb.confirm_text.format(
        kit=money.NAMES[data["kit"]],
        delivery="доставка" if data["delivery"] else "самовывоз",
        phone=data["phone"],
        total=data["total"],
    )

    await message.answer(
        text,
        reply_markup=ReplyKeyboardRemove(),
    )
    await message.answer("👇", reply_markup=kb.confirm)
    await state.set_state(OrderStates.waiting_payment)


# ── Шаг 4: оплата ──

@router.callback_query(OrderStates.waiting_payment, F.data == "pay")
async def cmd_pay(callback: CallbackQuery, state: FSMContext):
    data = await state.get_data()
    text = kb.pay_text.format(total=data["total"])
    await callback.message.edit_text(text, reply_markup=kb.paid)
    await callback.answer()


# ── Шаг 5: подтверждение ──

@router.callback_query(OrderStates.waiting_payment, F.data == "paid")
async def cmd_paid(callback: CallbackQuery, state: FSMContext, bot: Bot):
    data = await state.get_data()
    kit = data.get("kit", "?")
    delivery = data.get("delivery", False)
    total = data.get("total", "?")
    phone = data.get("phone", "не указан")

    user = callback.from_user
    logger.info(f"Заказ от {user.id} ({user.username}): {kit}, {total} ₽, {phone}")

    await callback.message.edit_text(kb.paid_text)

    try:
        await bot.send_message(
            ADMIN_ID,
            f"🔔 <b>Новый заказ</b>\n\n"
            f"👤 @{user.username or '—'} (id <code>{user.id}</code>)\n"
            f"📞 Телефон: <code>{phone}</code>\n"
            f"📦 Комплект: {money.NAMES.get(kit, kit)}\n"
            f"🚚 Способ: {'доставка' if delivery else 'самовывоз'}\n"
            f"💰 Сумма: <b>{total} ₽</b>",
            parse_mode="HTML",
        )
    except Exception:
        logger.exception("Не удалось отправить админу")

    await state.clear()
    await callback.answer("Готово ✅")


# ── Отмена ──

@router.callback_query(F.data == "cancel")
async def cmd_cancel(callback: CallbackQuery, state: FSMContext):
    await state.clear()
    try:
        await callback.message.edit_text(kb.cancel_text)
    except Exception:
        await callback.message.answer(kb.cancel_text)
    await callback.answer()


# ── фолбэк ──

@router.message(F.text)
async def unknown_command(message: Message):
    await message.answer("Таких команд я не знаю\nНапиши /start и я покажу, что я могу")