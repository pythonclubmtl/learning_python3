## Bots

Read and try the code from:
* https://chatbotslife.com/creating-a-saavn-downloader-bot-for-telegram-part-1-8365b707e3d4
Once you've tried the code and have your first bot running, move on to the documentation of pyTelegramBot and focus on the https://github.com/eternnoir/pyTelegramBotAPI#message-handlers section:
* https://github.com/eternnoir/pyTelegramBotAPI

Take a look at this issue (specifically the answer by Omid N):
* https://stackoverflow.com/questions/42796300/get-photo-in-telegram-bot-through-pytelegrambotapi

Then take a look at `telegrambot.py`, in the same folder as this file.

## Objectives
* Write a file (called `modules/bot.py`) that contains one function or several ones designed to be called sequentially in order to interact with a user (create a `\hello` command, `\about`, `\help` maybe) 
* Add a function to make the bot able to receive text files