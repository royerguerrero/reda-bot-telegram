import os
from telegram.ext import Updater, CommandHandler

class BotTelegram:
    """[summary]
    """
    
    API_KEY = str(os.environ['API_KEY_TELEGRAM'])

    def __init__(self):
        """[summary]
        """
        self.updater = Updater(self.API_KEY)
        self.dispatcher = self.updater.dispatcher

    def add_commands(self, commands):
        """[summary]

        Args:
            commands ([type]): [description]
        """
        for cmd in commands:
            self.dispatcher.add_handler(
                CommandHandler(cmd, lambda bot, update: bot.send_message(chat_id=update.message.chat_id, text=commands[cmd], parse_mode='HTML'))
            )

    def __del__(self):
        """[summary]
        """
        self.updater.start_polling()