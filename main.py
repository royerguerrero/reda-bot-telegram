from app.commands import CommandsManager
from app.bot import BotTelegram

def bot_telegram():
    bot = BotTelegram()
    commands_handler = CommandsManager('app\commands.json')
    commands = commands_handler.get_commands()
    bot.add_commands(commands)

def add_command():
    pass

def update_command():
    pass

def delete_command():
    pass

def print_commands():
    pass

def commands_manager():
    while True:
        print('Welcome to Commands Manager')
        print('1. Add command')
        print('2. Update command')
        print('3. Delete command')
        print('4. Print all command')
        print('9. Return')
        print('0. Exit')
        option = int(input('Choose a option: '))
        print('--- ' * 5)

        if option == 1:
            add_command()
        elif option == 2:
            update_command()
        elif option == 3:
            delete_command()
        elif option == 4:
            print_commands()
        elif option == 9:
            main()
        elif option == 0:
            break


def main():
    while True:
        print('Hi friend, what you want to do? ')
        print('1. Execute bot')
        print('2. Commands manager menu')
        print('0. Exit')
        option = int(input('Choose a option: '))
        print('--- ' * 5)

        if option == 1:
            bot_telegram()
        elif option == 2:
            commands_manager()
        elif option == 0:
            break


if __name__ == "__main__":
    print(""" 
        ______    __                        ___       __ 
       /_  __/__ / /__ ___ ________ ___ _  / _ )___  / /_
        / / / -_) / -_) _ `/ __/ _ `/  ' \/ _  / _ \/ __/
       /_/  \__/_/\__/\_, /_/  \_,_/_/_/_/____/\___/\__/ 
                     /___/                               
                        - REDA CHANEL -
    """)
    main()