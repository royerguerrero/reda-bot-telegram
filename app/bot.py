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

    def add_command(self, command_name, function):
        dp = self.dispatcher
        dp.add_handler(CommandHandler(command_name, function))

    def rules(self, bot, update):
        chat_id = update.message.chat_id
        bot.send_message(chat_id=chat_id, text='<b>All Rules</b>', parse_mode='HTML')

    def __del__(self):
        """[summary]
        """
        self.add_command('rules', self.rules)
        self.updater.start_polling()