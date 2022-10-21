from aiogram import Dispatcher, types
from aiogram.dispatcher import FSMContext

from app.messages import Commands
from app.utils import delete_markup


async def empty_card(callback: types.CallbackQuery, state: FSMContext):
    await state.reset_state()
    await callback.answer()
    await delete_markup(callback.message)

    name = callback.from_user.full_name
    reply = Commands.options(name, callback.data)
    await callback.message.answer(**reply)


def register_handlers(dp: Dispatcher):
    dp.register_callback_query_handler(empty_card, lambda query: query.data == 'empty_card', state='*')
