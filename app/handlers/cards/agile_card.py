from aiogram import Dispatcher, types
from aiogram.dispatcher import FSMContext

from app.messages import Commands
from app.messages.cards.agile_card import AgileCard
from app.states.cards.agile_card import AgileCardStates
from app.utils import delete_markup


async def agile_start(callback: types.CallbackQuery, state: FSMContext):
    await state.set_state(AgileCardStates.start)
    await callback.answer()
    await delete_markup(callback.message)

    # name = callback.from_user.full_name
    replies = AgileCard.start()

    for reply in replies:
        await callback.message.answer(
            reply,
            reply_markup=None,
        )


def register_handlers(dp: Dispatcher):
    dp.register_callback_query_handler(agile_start, lambda query: query.data == 'agile', state='*')