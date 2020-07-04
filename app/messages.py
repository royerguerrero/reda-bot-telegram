import json

class MessageManager:

    def __init__(self, filename):
        self.filename = filename


    def get_messages(self):
        with open(self.filename) as json_file:
            data = json.load(json_file)

        return data


    def get_message(self, head):
        try:
            messages = self.get_messages()
            result = messages[head]

        except KeyError:
            result = 'The message was not found'
        
        return result


    def add_message(self, message):
        messages_list = self.get_messages()
        messages_list.update(message)
        
        self.save_file(messages_list)

        return messages_list


    def update_message(self, old_head, new_body):
        messages_list = self.get_messages()
        message = {old_head: new_body}
        messages_list.update(message)
        self.save_file(messages_list)

        return messages_list

    
    def delete_message(self, head):
        try:
            message_list = self.get_messages()
            del(message_list[head])
            self.save_file(message_list)
            result = 'The message was successfully deleted'
        
        except KeyError:
            result =  'The message was not deleted because it was not in the list of messages'
        
        return result
        

    def save_file(self, list_messages):
        with open(self.filename, 'w') as json_file:
            json.dump(list_messages, json_file)
            

    