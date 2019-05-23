#Importing the telebot module
import telebot

import logging

#logger = telebot.logger
#telebot.logger.setLevel(logging.DEBUG) # Outputs debug messages to console.
#Call the Telebot created in telegrm thanks to its TOKEN
bot = telebot.TeleBot("791446971:AAEDuNxuEQU67jbScnjLwcrOCVG57lBD5oY")
tb = telebot.TeleBot("791446971:AAEDuNxuEQU67jbScnjLwcrOCVG57lBD5oY")

bot.send_message(chat_id = "-1001386026536", text = "hi" )

#This function will accept documents like PDF articles
@bot.message_handler(content_types=['document'])
#The message from telegram is always considered in the variable message
def handle_docs(message):
#store the informations of the document in the file_info variable. It is a list that contains a file_id, the file_zize and the file_path. The file_path is written like 'document type/.../file extension'
	file_info = bot.get_file(message.document.file_id)
#Write the document in the hard drive disk, in the foler where the script is running
	downloaded_file = bot.download_file(file_info.file_path)
#take the extension from the file_info using rsplit function. This will be used for the downloading in the same document type as the original one.
	extension = file_info.file_path.rsplit('.')[1]
#Define the path where the file will be downloaded
	src = './biblios/'
#Choose the file name as "File_id.extension". If you find a better way to name the file, please feel free to modify the "file_info.file_id" name.
	filename = src + message.chat.first_name + "." + extension
	with open(filename, 'wb') as new_file:
		new_file.write(downloaded_file)

#This function answer to questions asked in the telegrambot
@bot.message_handler(commands=['start', 'help'])
def send_welcome(message):
	#Answer to the question with the description of the purpose of this bot
	bot.reply_to(message, "I'm the bot who will make your research easier")

#Answer to any other questions with the only solutions available
@bot.message_handler(commands=['Dearbot'])
def echo_all(message):
	bot.reply_to(message, "Yes sir I'm here, what do you need ?")

#if
	tb.send_message(-326067236, URL)

bot.polling()
