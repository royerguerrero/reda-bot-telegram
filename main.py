from app.commands import CommandsManager
from app.bot import BotTelegram

def bot_telegram():
    commands_handler = CommandsManager('app\commands.json')
    commands = commands_handler.get_commands()
    bot = BotTelegram()
    bot.add_commands(commands)

if __name__ == "__main__":
    bot_telegram()