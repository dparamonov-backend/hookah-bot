from aiogram.fsm.state import State, StatesGroup


class OrderStates(StatesGroup):
    choosing_kit = State()
    choosing_delivery = State()
    waiting_phone = State()
    waiting_payment = State()