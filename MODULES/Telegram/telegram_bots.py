import telebot
bot = telebot.TeleBot("791446971:AAEDuNxuEQU67jbScnjLwcrOCVG57lBD5oY")
@bot.message_handler(commands=['start', 'help'])
def send_welcome(message):
	bot.reply_to(message, "Howdy, how are you doing?")

@bot.message_handler(func=lambda message: True)
def echo_all(message):
	bot.reply_to(message, message.text)

@bot.message_handler(content_types=['document'])
def handle_docs(message):
    bot.reply_to(message, "Congrat, you received a document")
    file_info = bot.get_file(message.document.file_id)
    bot.reply_to(message, file_info)
    downloaded_file = bot.download_file(file_info.file_path)
    extension = file_info.file_path.rsplit('.')[1]
    filename = file_info.file_id + "." + extension
    with open(filename, 'wb') as new_file:
        new_file.write(downloaded_file)
import pdb; pdb.set_trace()
bot.polling()
