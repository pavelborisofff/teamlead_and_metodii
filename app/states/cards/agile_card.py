from aiogram.dispatcher.filters.state import State, StatesGroup


class AgileCardStates(StatesGroup):
    name = 'agile_card'
    start = State()
    generate_hypothesis = State()
