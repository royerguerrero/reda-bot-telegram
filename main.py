from app.messages import MessageManager

def bot_telegram():
    bot = MessageManager('app/message.json')
    print(bot.get_messages())
    message = {'other message': 'test'}
    bot.add_message(message)
    print(bot.update_message('other message', 'Update message'))
    

if __name__ == "__main__":
    bot_telegram()