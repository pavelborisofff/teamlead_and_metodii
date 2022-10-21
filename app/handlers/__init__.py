from aiogram import Dispatcher

from app.handlers.commands import register_handlers as handlers_commands
from app.handlers.cards import handlers_agile_card as handlers_cards


class Handlers:
    def __init__(self, dp: Dispatcher):
        self.dp = dp

    def register(self):
        handlers_commands(self.dp)
        handlers_cards(self.dp)

    def unregister(self):
        pass
        # self.dp.message_handlers.unregister_all()

    def reset(self):
        self.unregister()
        self.register()

    def __call__(self, *args, **kwargs):
        self.register()


