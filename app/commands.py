import json

class CommandsManager:
    """[summary]
    """

    def __init__(self, filename):
        """[summary]

        Args:
            filename ([type]): [description]
        """
        self.filename = filename


    def get_commands(self):
        """[summary]

        Returns:
            [type]: [description]
        """
        with open(self.filename) as json_file:
            data = json.load(json_file)

        return data


    def get_command(self, head):
        """[summary]

        Args:
            head ([type]): [description]

        Returns:
            [type]: [description]
        """
        try:
            commands = self.get_commands()
            result = commands[head]

        except KeyError:
            result = 'The command was not found'
        
        return result


    def add_command(self, command):
        """[summary]

        Args:
            command ([type]): [description]

        Returns:
            [type]: [description]
        """
        try:
            commands_list = self.get_commands()
            commands_list.update(command)
        
            self.save_file(commands_list)
            result = 'The command was successfully added'
        except KeyError:
            result = 'Error: probably the command already exists, use another name'

        return result


    def update_command(self, old_head, new_body):
        """[summary]

        Args:
            old_head ([type]): [description]
            new_body ([type]): [description]

        Returns:
            [type]: [description]
        """
        try:
            commands_list = self.get_commands()
            command = {old_head: new_body}
            commands_list.update(command)
            self.save_file(commands_list)
            result = 'The command has been successfully updated'
        except KeyError:
            result = 'Problem is the command name doesn\'t exist, check it and try again'

        return result

    
    def delete_command(self, head):
        """[summary]

        Args:
            head ([type]): [description]

        Returns:
            [type]: [description]
        """
        try:
            command_list = self.get_commands()
            del(command_list[head])
            self.save_file(command_list)
            result = 'The command was successfully deleted'
        
        except KeyError:
            result =  'The command was not deleted because it was not in the list of commands'
        
        return result
        

    def save_file(self, list_commands):
        """[summary]

        Args:
            list_commands ([type]): [description]
        """
        with open(self.filename, 'w') as json_file:
            json.dump(list_commands, json_file)  