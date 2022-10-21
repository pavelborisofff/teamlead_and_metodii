import aiogram
from aiogram import types


async def delete_markup(message: types.Message, previous: bool = False):
    try:
        await message.bot.edit_message_reply_markup(
            chat_id=message.chat.id,
            message_id=message.message_id - previous,
            reply_markup=None
        )
    except aiogram.utils.exceptions.MessageCantBeEdited as e:
        print(e)
        pass
