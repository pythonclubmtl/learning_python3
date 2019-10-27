
# Python 01

1. [Anaconda](#Anaconda): Run Python on your current OS
2. **If you are currently trying to install Python on your Linux Virtual Machine**: [Linux Virtual Machine](#LinuxVirtualMachine); otherwise, you should move on to the next section. 
3. [Requirement](#Requirement)



---

# Anaconda

Anaconda provides easy access to a large amount of scientific packages for the `R` or Python languages. The list of packages available for [Windows are for example provided here](https://docs.anaconda.com/anaconda/packages/py3.6_win-64/). Among the list of packages are the powerful TensorFlow, Machine Learning and Deep Learning framework by Google, or PyTorch, the equivalent but mainly being maintained by Facebook. Scientific packages are also available, the whole of Python's scientific suite is available: numpy, scipy, scikit and sympy will provide a framework as powerful as Matlab to solve complex equations, manipulate mathematical objects, solve symbolic problems, solve optimization/minimization using a variety of technique, etc... During these workshops, we will only explore a tiny, very tiny, portion of the possibilities offered by the packages compiled within the Anaconda distribution. 

## Anaconda Prompt / Python Shell

You should also be able to run the `Python` version included with Miniconda that we previously installed, reminder:
* Search for an application named `Anaconda prompt` on your laptop, launch it
* Input `python`; press Enter


## (Optional) Interactive Development Editor: Spyder

Instead of interacting with Python from the pure command line interface, you can also do so from an Interactive Development Editor (IDE). An IDE will provide a visual interface specifically designed to write a certain type of code (scientific, web development, etc...). Spyder is geared to provide a comfortable experience for scientific users by constantly displaying a Variable Explorer, a Python Shell, and a code editor optimized for python's scientific packages. Since Spyder is a software completely written in Python, it is quite easy to install it from Miniconda, that is a framework for Python.
In order to install Spyder from Miniconda, write the following command in your Anaconda Prompt:
```
    conda install -c anaconda spyder
```
This command will automatically download all the Python packages necessary to run Spyder and install them for you by using the packages available within the Miniconda compilation. You might need to type a `y` at some point during the installation.

After the installation, you should have a new software installed on your computer called Spyder. You should also be able to start Spyder from your Anaconda Prompt by simply typing `Spyder`.
You should now try to launch Spyder.

[<img src="https://i.postimg.cc/Cxpj2bnP/Python-Spyder-Initial-Screen.png
">](https://i.postimg.cc/Cxpj2bnP/Python-Spyder-Initial-Screen.png)

Spyder's interface is divided into 3 areas. The large panel on the left allows you to edit scripts, several scripts can be opened at the same time thanks to tabs. The top right hand corner panel can either display the current in memory value of the variables used in your scripts or can be a file explorer. Finally, the feature we are currently interested in, the bottom right hand corner provides an iPython console. iPython is a command line interface built for Python that is a slightly improved version of the command line interface you accessed through the `Anaconda Prompt`>`Python` command. It can display images, graphs, it is also faster than the standard black and white command line interface and can be a bit more helpful with its answers.

For the following sessions (2 and 3), you can either use the standard black and white command line interface or the iPython interface from Spyder. Spyder will become a much more convenient tool around Session 4 and 5 when we will start writing scripts.

---

# Linux Virtual Machine

If you are currently using Python fron Miniconda/Anconda, **do not go through this section**.

## Installing Python

The first step into programming is to get Python installed on your Virtual Machine (VM). You will need two things

* Python itself
* A code editor

### On Ubuntu Linux

#### python3

By default, Python is already installed. In this tutorial however, we will use Python3 whenever possible. You can install it from a terminal window (`Ctrl`+`Alt`+`T`) with: 

    sudo apt-get install python3

If you are using our VM, you already have python, this is in case you ever need to install it.

To check whether everything worked, type:

    python3

This will take you to the interactive console.

#### Code editor

If you open a terminal and type `gedit`. It will open the text editor **gedit**.

As a text editor, it is fine to start with **gedit**. Please make sure to change tabs to spaces via *Edit -> Preferences -> Editor -> tick 'Insert spaces instead of tabs'*.

Later, we will use a text editor with more features that will be helpful for python code writing.

---

# Requirement

> Which python version are you running?


Check your python version by typing:

* **Linux Virtual Machine** (in the terminal): 
```
python3 --version
```
* **Anaconda**: Start Python by typing `python` in your `conda prompt` (look for this app), you should see the Pŷthon version written right there

You should see something like `Python 3.6.7`.
It is important that your python version is superior to 3.5.