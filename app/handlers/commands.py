from aiogram import Dispatcher, types
from aiogram.dispatcher import FSMContext
from aiogram.dispatcher.filters import Text

from app import logger, cards_picture
from app.messages import Commands
from app.utils import delete_markup

logger.warn(cards_picture)

START = [
    'start',
    'старт'
]
OPTIONS = [
    'options',
    'опции',
]


# any state
async def cmd_start(message: types.Message, state: FSMContext):
    await state.reset_state()
    await delete_markup(message, previous=True)

    reply = Commands.start(message.from_user.full_name)
    await message.answer(**reply)


# any state
async def cmd_options(callback: types.CallbackQuery, state: FSMContext):
    await state.reset_state()
    await callback.answer()
    await delete_markup(callback.message)

    option = callback.data.split('_')[1]
    name = callback.from_user.full_name
    reply = Commands.options(name, option)

    if option == 'cards':
        with open(cards_picture, 'rb') as photo:
            await callback.message.answer_photo(
                photo,
                caption=reply['text'],
                reply_markup=reply['reply_markup']

            )
    else:
        await callback.message.answer(**reply)


def register_handlers(dp: Dispatcher):
    dp.register_message_handler(cmd_start, commands=START, state='*')
    # dp.register_callback_query_handler(cmd_start, lambda query: query.data == 'start', state='*')
    dp.register_message_handler(cmd_start, commands=OPTIONS, state='*')
    dp.register_callback_query_handler(cmd_options, lambda query: query.data.startswith('opt_'), state='*')