import json

class CommandsManager:

    def __init__(self, filename):
        self.filename = filename


    def get_commands(self):
        with open(self.filename) as json_file:
            data = json.load(json_file)

        return data


    def get_command(self, head):
        try:
            commands = self.get_commands()
            result = commands[head]

        except KeyError:
            result = 'The command was not found'
        
        return result


    def add_command(self, command):
        commands_list = self.get_commands()
        print(command)
        commands_list.update(command)
        
        self.save_file(commands_list)

        return commands_list


    def update_command(self, old_head, new_body):
        commands_list = self.get_commands()
        command = {old_head: new_body}
        commands_list.update(command)
        self.save_file(commands_list)

        return commands_list

    
    def delete_command(self, head):
        try:
            command_list = self.get_commands()
            del(command_list[head])
            self.save_file(command_list)
            result = 'The command was successfully deleted'
        
        except KeyError:
            result =  'The command was not deleted because it was not in the list of commands'
        
        return result
        

    def save_file(self, list_commands):
        with open(self.filename, 'w') as json_file:
            json.dump(list_commands, json_file)  

        with open('app\commands_fucns.py', 'w') as f:
            for command in list_commands:
                f.write(f'def {command}(bot, update):\n\tchat_id = update.message.chat_id\n\tbot.send_message(chat_id=chat_id, text="{list_commands[command]}")\n\n')
