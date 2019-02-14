# class

> Classes provide a means of bundling data and functionality together. 
> Creating a new class creates a new type of object, allowing new instances of that type to be made.

A class can have variables attached to it, it can also have functions attached to it. If you crate a new instance of that class, it will also have variables and functions attached to it.
Classes are behind the concept of **Object Oriented Programming**: an instance of a class is also called an `object`. 

You actually already used classes: `integer`, `string` or `list` are actually `python` classes. All `lists` are instances of the `list` class contained within `python`.

Examples help.

Let's build our first class. Building classes without any thinking behind it is not useful. In this case, we are going to create a class that represents cats.
Let's define our class:

```python
class Cat:
	pass
```
That's it ! This is the simplest class you can make ! It is useless, but it shows how you can initialize a class. Notice that everything within the class must be indented. 

Later on during the code, or even from another file, you can assign a new `cat` object to the `floki` variable doing:
```
floki = Cat()
```
Ok, now let's improve our class a bit. To initialize a class (let's be honest, our previous class was really useles), you always need a `__init__` function, like this:

```python
class Cat:

    # Initializer / Instance Attributes
    def __init__(self, name, age):
        self.name = name
        self.age = age
```
An `__init__` method always takes `self` as an input, `self` refers to the class itself. Any function which is part of the class (meaning that it will be able to access variables and functions from the class) must take `self` as an input.
Here, the class is initialized by providing a name and age for our cat. To initialize this class, you could use:
```
floki = Cat("floki", 3)
```

If you then try:
```
>>> floki.name
'floki'
>>> floki.age
3
```
Notice how the `Cat` object is carrying all its variables with it, and these can be called any time. We could also have a second cat object:
```
louise = Cat("louise", 2)
```
We could then retrieve information about louise using: `louise.name` and `louise.age`
We can actually retrieve these variables because they were defined using `self.name = name`. If a variable is defined within the class without a `self` it will not be accessible from outside the class.


Alright, our classes can now have variables that we can access from outside the class.
Let's try to add a class function:

```python
class Cat:
    def __init__(self, name, age):
        self.name = name
        self.age = age
        
    def hungry(self):
    	print("Miaou") #these cats are moroccan they dont say meow
```
Notice how our function takes a `self` as an input even if there is no input. Since it is a class function it needs to input the `object` itself.
Now if we initialize the class again, we should be able to trigger this class function:
```
>>> floki = Cat("floki", 3)
>>> floki.hungry
'Miaou'
```

A function can also be triggered when the class initializes:
```python
class Cat:
    def __init__(self, name, age):
        self.name = name
        self.age = age
        self.hungry()
        
    def hungry(self):
    	print("Miaou") 
```
Notice how we are calling the function with a self before it since it is a function within the class. This time, if you create a new instance of a cat object:
```
>>> floki = Cat("floki", 3)
'Miaou'
```
The `hungry()` function is triggered during its initialization.

Don't forget, if you define a variable without a `self` before it, it will only be accessible within the class

```python
class Cat:
    def __init__(self, name, age):
        name = name
        age = age
```

For example, this time, you will not be able to print name and age after initializing your class.

# import

A few additions about import. We have explored in [functions](005-functions.md) how imports can be used to import functions or classes from other files.

Let's say we have a folder with two files:

```bash
ilyass@tx1:~/ex_imports$ ls
myfunctions.py  myscript.py
```
The file `myfunctions.py` contains a function called `hellofunc()` that prints `"Hello"` when called:
```python
def hellofunc():
	print("hello")
```

The file `myscript.py` contains an import and then a call to the `hellofunc()` function:
```python
from myfunctions import hellofunc

hellofunc()
```
Since both files are in the same folder, the `from myfunctions import hellofunc` will try to import a python package installed on your system which is called `myfunctions` and that contains a `hellofunc` function, but since there is no such package it will find the file in the same folder called `myfunctions.py` and it will import `hellofunc`.

If you execute the `myscript` it will thus successfully print `'hello'`:
```bash
ilyass@tx1:~/ex_imports$ python myscript.py 
hello
```
It is a convenient way to store some functions you might need in several projects.
You can import functions and classes from other files using this method.
It is also possible to import functions and classes stored in folders within your project folder, it requires respecting a certain folder and file structure. We will not be exploring these structures in this intro class.

# pip

In this section, we will explore how you can install python packages using `pip`, a python pckage manager, using Ubuntu.
We will use the `slackclient` package as an example. This package allows you to easily build a bot for Slack, the widely spread communication software.

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