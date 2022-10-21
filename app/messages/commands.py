class Commands:
    @staticmethod
    def start(name: str) -> dict:
        text = f'Привет, {name}!\n\n...Тут описание бота и прочее...\n\nНажми на нужную кнопку, чтобы продолжить:'
        buttons = [
            [
                {'text': 'Карточки 🟥🟨🟦🟩', 'callback_data': 'opt_cards'},
            ],
            [
                {'text': 'Настройки ⚙️', 'callback_data': 'opt_settings'},
                {'text': 'Сброс 🔄', 'callback_data': 'opt_reset'}
            ]
        ]
        message = {
            'text': text,
            'reply_markup': {
                'inline_keyboard': buttons,
                'resize_keyboard': True,
                'remove_keyboard': True,
                'one_time_keyboard': True
            }
        }

        return message

    @staticmethod
    def options(name: str, option: str) -> dict:
        if option == 'cards':
            text = f'{name}, выбери карточку'
            buttons = [
                [
                    {'text': '🟥 Agile', 'callback_data': 'agile'},
                    {'text': '🟨 Opt2', 'callback_data': 'empty_card'},
                ],
                [
                    {'text': '🟦 Opt3', 'callback_data': 'empty_card'},
                    {'text': '🟩 Opt4', 'callback_data': 'empty_card'},
                ]
            ]
        elif option == 'settings':
            text = f'Тут будут настройки. Жми на старт, чтобы вернуться в главное меню'
            buttons = [
                [
                    # {'text': '⬅️ Назад', 'callback_data': 'start'},
                ]
            ]
        elif option == 'reset':
            text = f'Тут будет сброс прогресса или ещё что. Жми на старт, чтобы вернуться в главное меню'
            buttons = [
                [
                    # {'text': '⬅️ Назад', 'callback_data': 'start'},
                ]
            ]
        elif option == 'empty_card':
            text = f'Тут пока ничего нет. Возвращайся назад быстрей!'
            buttons = [
                [
                    {'text': '⬅️ Назад', 'callback_data': 'opt_cards'},
                ]
            ]
        else:
            text = f'Что-то пошло не так…'
            buttons = [
                [
                    {'text': '⬅️ Назад', 'callback_data': 'opt_cards'},
                ]
            ]

        message = {
            'text': text,
            'reply_markup': {
                'inline_keyboard': buttons,
                'resize_keyboard': True,
                'remove_keyboard': True,
                'one_time_keyboard': True
            }
        }

        return message

