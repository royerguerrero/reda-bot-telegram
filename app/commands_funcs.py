def new_command3(bot, update):
	chat_id = update.message.chat_id
	bot.send_message(chat_id=chat_id, text="content to test")

