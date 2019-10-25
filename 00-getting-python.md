# Python

<img src="assets/pseudowrong.jpg" alt="drawing" width="550"/>

Python is a general purpose and high level programming language. It is not a compiled language. It favors stuctured programming based on scripts, functional programming and objet oriented programming.

# Ideal Python Learning Environment

These workshops are mainly aimed at learning about python, however, they could also be the perfect opportunity to also learn about `Linux`. Experience shows that running development environments on a Linux system is generally easier than on any other OS, as it is one of the prefered OS of developers due to its ability to compile code for almost amy platform. In addition, the Linux environments makes it easy to plug together completely different pieces of software within the same session, which remains challenging on Windows. 

[<img src="https://revolution-computing.typepad.com/.a/6a010534b1db25970b022ad37abd9b200d-pi">](https://blog.revolutionanalytics.com/2018/06/pypl-programming-language-trends.html)

Linux is also the most common OS used on servers, and most specifically on servers designed for highly computational usages. For example, Calcul Canada and Quebec's servers, if you were to ever need them, run Linux. The vast majority of websites and services you interact with everyday have a Linux OS running them in the background. Take a look at this webpage if you would like to learn more about Linux: https://www.linux.com/what-is-linux/ 

During these workshops, you can decide to either:
1. Run and use Python from your current OS
2. Run and use Python from a Linux Virtual Machine

The first solution will allow you to immediately get started with basic Python coding while staying within the comfort of the OS you know and are familiar with; however, you might encounter some unexpected issues that are specific to your OS and version of the Python container you are using. These unexpected issues might slow down your Python learning experience.
You might also encounter some limitations when we will need to start connecting code from different sources together or when we'll need to connect data from different software sources together, these limitations are often hard to solve and require specific patches for each OS.

For these reasons, an ideal Python learning experience would be within the Linux OS. But your PC is probably on another OS. Well that's not really a problem: Virtual Machines.

### Virtual Machines

<img src="assets/win-in-win.jpg" alt="drawing" width="550"/>

It is actually quite easy to run a "computer within your computer", a virtual computer that is being emulated by the hardware that you have on your computer. Virtual Machine allow you to conviently run a Mac OS Virtual Machine on your Windows machine or a Windows machine on a Linux host. 
Virtual Box (https://www.virtualbox.org/) is a virtualization (open source software), basically, it can run a virtual Linux computer in a window of your computer, allowing you to minimize your browser or music in the background while you are working on your Python code.
Once you are within your Linux machine, you will (virtually) be running the exact same computer as any other person in the room. You should encounter the exact same errors, bugs and unexpected problems as everybody else. This will help us save a tremendous amount of time that we will use to better focus on Python instead of spending time solving  OS or software related issues. 

However, since installing and setting up a Virtual Machine will also slow down your learning experience, since you might also enounter some bugs related to your current OS, we actually recommend that your first get started with a Python distribution adapted for your OS in order to go through the 3 first sessions. You would ideally switch to your Linux Virtual Machine, that will be ready to use by then, when you will start the fourth session: Lists and Dictionaries.

### The Python(s)

[<img src="https://i.stack.imgur.com/Jqi6q.png">](Python2Python3)


Before we move on to the software you can use to get started with Python, we are going to avoid any confusions by specifying know that there actually *two* Pythons.

The first stable versions of Python were available at the end of the eighties by Guido Van Rossum, its main developer and "benevolent leader", a position from which he stepped down in 2018. When Python was getting structured in the ninties, the team at the time could not foresee all the possible applications and issues their software will face in the future. In 2000, they were able to implement a major update that fixed most of the issues Python was facing, the Python 2.0. However, they already knew at the time that there were still a a bunch of other core improvements that could be made, but that they did not dare implement yet, as those changes would make it impossible to run python files written in the language of the old version with the new application and vice versa. Python was already widely spread at the time, already included and a vital part of various embedded systems, industrial applications and others which made it hard for the team to force the whole community to abandon all their libraries of code and restart from scratch with a better Python. For these reasons, the team decided to maintain Python 2 from 2000 until 2020, while simultaneously releasing Python 3.0 in 2008.

[<img src="http://www.randalolson.com/wp-content/uploads/python-survey-2014-python3-mistake.png">](Python2Python3)

The majority of improvements provided by Python 3.0 are also made available in Python 2.0 through independent development teams that maintain open sources fixes. In addition, for simple applications, the difference between Python 2 and 3 is invisible, except for a few minor changes in syntax. 
Now that we know a bit more about the twin Pythons, we can move on to download the **right** Python version of Python, in the next step. 

[<img src="http://www.randalolson.com/wp-content/uploads/python-survey-2014-prevent-upgrade.png">](Python2Python3)


### Packaged Python

In order to easily get started with Python, we are going to rely on a package containing Python with several other Python science and data sciences packages called Anaconda. One of Anaconda's main goal is to simplify package management and deployment. Let's go ahead and download Anaconda: https://www.anaconda.com/distribution/

After finishing the installation of Anaconda, you should have several new applications installed on your computer (don't worry, you can uninstall all of those with one click if needed). During the next 3 sessions, you will need to run a Python shell. It is a command line environment in which you can input python commands. Python will provide verbose answers in the command line. It is an extremely convenient tool for testing and debugging. In order to start a Python shell, search for the `Anaconda prompt` app.

[<img src="https://miro.medium.com/max/965/1*uZCErUuD6OaOA2DTy1s-_A.png">](https://medium.com/@tranngocminhcdn/running-python-scripts-by-using-anaconda-prompt-da2870d86fd0)


# TL; DR

* Programming is easier on Linux
* Linux is also a widely used OS that is relevant for researchers to know
* Linux can be used through a Virtual Machine and it is recommended to use Python this way after the fourth session
* Until then (Session 1-3), we are going to use Python through a distribution that packages Python and other convenient software
* Python 2 and Python 3 are co-existing until 2020 because migration from Python 2 has met a lot of intertia since 2008
* We will be using Python 3
* Download Anaconda in order to install Python and other convenient packages
* Start the `anaconda prompt` after Anaconda install


# Homework

1. Follow this tutorial to install a Linux Virtual Machine: https://itsfoss.com/install-linux-in-virtualbox/ (ideally, you would do this while doing sessions 1-3)
