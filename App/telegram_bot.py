#Importing the telebot module
import telebot
import ml_functions as functions
import logging
import os
import re

#logger = telebot.logger
#telebot.logger.setLevel(logging.DEBUG) # Outputs debug messages to console.
#Call the Telebot created in telegrm thanks to its TOKEN
bot = telebot.TeleBot("894655366:AAFInIq1yC9bBKrbaCr6Lgx1Es-Geio4syk")
# bot = telebot.TeleBot("791446971:AAEDuNxuEQU67jbScnjLwcrOCVG57lBD5oY")
chatid="159777457"

bot.send_message(chat_id=chatid, text = "hi" )

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

	src = os.getcwd()+'/bib_files/'
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
	# bot.send_message(-326067236, URL)


@bot.message_handler(commands=['train'])
def trainer_tester(message):
	(abstracts_bib, label_bib, files_list_bib)=functions.bib_reader()
	(abstracts_csv, label_csv, files_list_csv)=functions.csv_reader()
	label=label_bib+label_csv
	abstracts= abstracts_csv+abstracts_bib
	trained_vectorizer=functions.my_vectorizer(abstracts)

	# ================================================================================================================================
	# This part uses my_classifier function from my_functions file to split, train, and test the vectorized abstracts and reports the
	# my_score which is the % of success. In the end it writes that it is trained and then introduces the classes in the database.
	# ================================================================================================================================
	(X_train, X_test, y_train, y_test, clf)=functions.my_classifier(abstracts, label, trained_vectorizer)

	score=functions.my_score(X_test, y_test, clf)
	round_score = round(score)
	(predicted_category1, predicted_proba1, classes)=functions.my_predict('')
	reply_text = "Trained!\n"+str(round_score)+"% Success over tested dataset! \n"+"These are the classes: \n"+str(classes)+"Now you can try the prediction by copy/pasting an abstract infront of /predict (/predict abstract text)"
	bot.send_message(chat_id=chatid, text = reply_text)


# ================================================================================================================================
# This part gets a file or text of an abstract for prediction of its class; then predicts the class and prints all the classes, the predicted class related
# to the abstract, and the probability values (range:0-1) corresponding to each class.
# ================================================================================================================================
@bot.message_handler(commands=['predict'])
def predict(message):
	abstract=re.sub('/predict', '', message.text)
	(predicted_category1, predicted_proba1, classes)=functions.my_predict(abstract)
	reply_text = "Prediction completed!\n the class is:\n"+str(predicted_category1)
	bot.send_message(chat_id=chatid, text = reply_text)
	    
bot.polling()
