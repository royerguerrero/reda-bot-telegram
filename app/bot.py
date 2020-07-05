import os
from app.commands_funcs import *
from telegram.ext import Updater, CommandHandler

class BotTelegram:
    
    API_KEY = str(os.environ['API_KEY_TELEGRAM'])
    

    def __init__(self):
        self.updater = Updater(self.API_KEY)
        self.dispatcher = self.updater.dispatcher

    def add_commands(self, commands):
        self.dispatcher.add_handler(CommandHandler('new_command3', new_command3))
        # for command in commands:
        #     self.dispatcher.add_handler(CommandHandler(command, command))

    def __del__(self):
        self.updater.start_polling()