### Basic Slackbot

Slack is a popular tool for teams to communicate, store data, manage projects, etc ... It is a very useful tool, but is quite expensive. There are powerful open-source alternative with even more features (Rocket.chat, Mattermost) but we will consider Slack in this tutorial as it is the most popular one.
Slack has grown to include plugins for widely used tools (Google Drive, Google Calendar, todo tool, ...)  that interact with it as "bots" or "slackbots". In this tutorial, we are going to build our own, very basic, bot for Slack.

##### Requirements (pip)

In order to interact with Slack, you will need the `slackclient` python package. Python packages can easily be installed using `pip` (Python Installs Packages). The first thing we are going to do is to install `pip` for python.

First, let's check if you have `pip` already installed on your machine. Open a terminal and input:

```
pip3 --version
```
If you get something like:
```
ilyass@tx1:~/Repositories/Temp$ pip3 --version
pip 19.0.2 from /home/ilyass/Repositories/Temp/.slack/lib/python3.6/site-packages/pip (python 3.6)
```
Then you already have `pip` and you can move on to the next section, otherwise, input:

```
sudo apt update
```

* `sudo` : This command activates admin privileges, which will allow us to install new software on the machine.
* `apt` is a software that connects you to online repositories that contain software for Ubuntu, it will also manage your software, meaning that it can install, uninstall packages for you and manage dependencies between packages.
* `update` : We are here using the update function of apt, which will download information about the software available right now on the Ubuntu online repositories.

Then, input:
```
sudo apt install python3-pip
```
This time we are using the install function from apt, and we want to install the `python3-pip` software.
Press `Y` then `Enter` when `apt` asks for your authorization, and wait for apt to finish downloading and installing `python3-pip` for you.

Check that you now have pip using `pip3 --version`.

You can now install `slackclient` package for python3 using:
```
pip3 install slackclient
```
Once pip finishes installing the package for you, you can check that everything is working fine by opening the python console (`python3` in the terminal) and input:
```python
>>> import slackclient

```
If you don't get an error message, then you're good to go.

## Slack Apps: tokens

There are two ways to go about creating your slackbot: standalone bots, or Slack apps. Apps are more flexible and is Slack’s recommended route for creating a bot user, so that's what we'll try to do.

You should have a slack tram to test your apps, do not test it on an existing and active Slack team. You can create a new Slack team here: https://slack.com/get-started

Then, go to https://api.slack.com/apps and click on `Create an App`. Name it as you wish, and select your training workspace. The first thing we will need is our bot's token. A token is a long sequence of characters that is unique.  The token is used by Slack to verify that you, the bot owner, are the one connecting a python script to your bot, otherwise, anyone could take over your bot.  Click on `OAuth & Permissions` in the `Features` menu.

Then go to the `Scopes` section, and select `Send messages as user chat:write:user ` (you will need to adjust permissions before deploying your bot to a functional Slack Team). Press `Save changes` and scroll up to the `OAuth Tokens & Redirect URLs`.  
Click on `Install App to Workspace` and select your testing workspace. Authorize the bot to be an admin of the workspace and for `chat:write`, which will allow it to send messages.

The `OAuth Tokens & Redirect URLs` will now display an `OAuth Access Token` (starts by `xox`), copy it and store it somewhere safe, we will need it later.
We are also going to need the `Verification token` which is available in `Basic Information` in the `Settings` section. Store the `Verification token` with your `OAuth Access Token`.

We now have all the necessary information to be able to control our bot from `python`.

## Programming the bot

For this tutorial, we are going to create a bot that sends a message every X seconds/minutes/days (a scheduled message). Let's go ahead and build our script.

We are going to need the `SlackClient` package that we previously installed, we will need in our imports. We will also need to make the bot wait until its scheduled time arrives, so we will also need the `time` pacakge.

```python
from slackclient import SlackClient
import time
```

Then, the first thing we will have to do is provide `SlackClient` with our OAuth Access Token. `SlackClient`'s project page (https://github.com/slackapi/python-slackclient) provides an example to send messages, we will use something similar. The `SlackClient` class from the `SlackClient` package needs your token as an input:
```python
SLACK_BOT_TOKEN = "xoxp-547704002851-547209488609-548029262341-cXXXXXXXXXXXXXXXXXXXXXXX"
slack_client = SlackClient(SLACK_BOT_TOKEN)
```

Let's first test our bot by sending a single message using the `updateMsg` function from `SlackClient`. 
The `updateMsg` function takes 3 arguments:
* The kind of action we are doing, in our case: `chat.postMessage`
* The channel we will be sending a message to `channel=`, we will be using `#general` for now
* And the message itself `text=`
  
Let's write the section to send a message:
```python
msg = "Hello Slack!"

updateMsg = slack_client.api_call(
    "chat.postMessage",
    channel='#general',
    text=msg
)
```

Now if we put everything together, your script should be similar to this:
```python
from slackclient import SlackClient
import time

SLACK_BOT_TOKEN = "xoxp-547704002851-547209488609-548029262341-cXXXXXXXXXXXXXXXXXXXXXXX"
slack_client = SlackClient(SLACK_BOT_TOKEN)

msg = "Hello Slack!"

updateMsg = slack_client.api_call(
    "chat.postMessage",
    channel='#general',
    text=msg
)
```

Go ahead, save your script somewhere (I recommend creating a folder for the slackbot project) and execute it using python. If everything worked fine, you should receive a `Hello slack!` message in the `#general` channel of the Slack Team you used. 


### Scheduling messages

In order to schedule messages, we need to keep our script running constantly. Every X seconds/minutes/hours, our script will execute a function which sends a specific message. To do so, we will use a `while` loop.

A `while` loop is actually very similar to a `for` loop, except that it will run until a certain condition is met. A `for` loop will run until a certain count is reached.

Let's try a simple `while` loop example (you can try this using a script or directly in the python console):
```python
count = 0
while (count < 9):
   print 'The count is:', count
   count = count + 1
```
This `while` loop could be easily replaced by a `for` loop. In this case, the loop will print:
```
The count is: 0
The count is: 1
The count is: 2
The count is: 3
The count is: 4
The count is: 5
The count is: 6
The count is: 7
The count is: 8
```
And then break the loop as the condition `count < 9` is not `True` anymore. `While` loops are convenient because they can easily be transformed into `forever` loops. We can write a very simple condition that will never not be met: `while True is True`. This simple statement means that while `True` is `True` (which is always True) something will happen. In other words, the something will keep happening forever.
You can try it in your python console:
```python
while True is True:
    print("Yup, True is still True")
```
As you guessed, the loop will never end so you will have to break it using `Ctrl+C`.
The `while True is True` statement is usually simplified by simple writing `while True`. Python will understand that you mean `while True is True`.

Let's now use a `while True` loop to print a message every 10 seconds in our python console. We are going to use a function that you might have already used: `sleep()` from the time package, try it:
```python
while True:
    print("I'll send a message in 10 seconds")
    time.sleep(10)
```
You can now use this command to schedule a message every 10 seconds on Slack:
```python
from slackclient import SlackClient
import time

SLACK_BOT_TOKEN = "xoxp-547704002851-547209488609-548029262341-c87b58015dc71f15705b74fbc2cd5d6a"
slack_client = SlackClient(SLACK_BOT_TOKEN)

msg = "Hello Slack!"

while True:
    updateMsg = slack_client.api_call(
        "chat.postMessage",
        channel='#general',
        text=msg
    )
    time.sleep(10)
```

### Exercises

1. Create a bot that sends a message every Monday morning at 9AM (you might want to take a look at `ex_mondaycheck.py` in `learning_python3/examples`)
2. Create a bot that sends a different quote (https://www.goodreads.com/quotes) from a list every hour
    * Create a list and fill it with a few quotes or put quotes in a CSV file and import them 
3. Create a bot that sends Fibonacci sequence numbers one after the other only if the last number of the minutes in the hours is the same as the last number of the next Fibonacci sequence
    * The first number is 1, it can only be sent if it XX:01 or XX:11 or XX:21 ... If it is for example XX:06 when you start your script, the script will wait until XX:11 to send "1". The second number is a 1 too.
    * The third number, 2, can only be sent at XX:02 or XX:12 or XX:22 ...
    * And so on
