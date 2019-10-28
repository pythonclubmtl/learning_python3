# Python 04

1. [Lists](#lists)
2. [Dictionaries](#dictionaries)
3. [Scripting](#scripting)
4. [Exercises](#exercises)
5. [Project: Caesar cipher](#project-caesar-cipher)

Open your favorite Python3 prompt and let's get started !

# Lists

Lists are a compound datatypes often referred to as sequences, most common is `list`. These datatypes contain several elements which are all stored in a separate compartment, each element can be easily accessed, modified or removed. Each element is identified by its position in the list, with the first element being `element_0`, the second one `element_1`.

You can create a list by writing the following command in your python console :

```python
# empty list
>>> my_list = []
>>> my_list
```
`[]` are the symbols associated with a list, the same way `""` are the symbols associated with a string. You could for example write `a = ""` to create an empty string.

To create a list which already contains the integer 1, 2 and 3, you can input :
```python
# list of integers
>>> my_list = [1, 2, 3]
>>> my_list
```
It is possible to mix datatypes within a list, in this case, we are creating a list which contains an integer, a string and a float:
```python
# list with mixed datatypes
>>> my_list = [1, "Hello", 3.4]
>>> my_list
```
Get element of a list (first element is `0`):
```python
>>> my_list[0] 
>>> my_list[1]
>>> my_list[2]
```
If you try to get the fourth element of this list, you will get an error message:
```python
>>> my_list = [1, "Hello", 3.4]
>>> my_list[3]
Traceback (most recent call last):
  File "<stdin>", line 1, in <module>
IndexError: list index out of range
```
The error message means that the index you are requiring is out of the range of the list `my_list`, which is true, since this element does not exist.

To add an element to a list, use:
```python
>>> my_list = ['a','b','c','d','e']
>>> my_list.append('f')
>>> my_list
```
You can also modify any element from a list using its index:
```python
# I made a mistake in this list:
>>> my_list = ['a','k','c','d','e']
# change the 1st element    
>>> my_list[1] = "b" 
>>> my_list         
```
Finally, if you want to get the last element of a list, use negative indexing:
```python
>>> my_list = ['a','b','c','d','e']
>>> my_list[-1]
```
To get the one before the last one:
```python
>>> my_list[-2]
```

# Dictionaries

You can see dictionaries as lists with uniques keys that will lead to a value or element. 
A list can be seen as a kind of dictionary where the key to call the value of each element is the position of this element in the list.
For dictionaries, each element is identified by a unique string, called a key, `key: value`.

```python
# empty dictionary
>>> my_dict = {}
>>> my_dict
# dictionary with integer keys
>>> my_dict = {1: 'apple', 2: 'potato'}
>>> my_dict
```
In the previous example, integers were used as keys for the dictionary. The dictionary contains two different element, the first element's key is `1` and its value is `apple`.
To retrieve the value of the element associated with the key `1`, we can write:

```python
# get element of dict using key
>>> my_dict[1]
```

Instead of integers, strings are usually employed: 

```python
# dict with string keys
>>> my_dict = {'fruit': 'apple', 'vegetable': 'potato'}
>>> my_dict['vegetable']
```

We can again, go update any value using its key:
Update/add items to dicts:

```python
>>> my_dict = {'fruit': 'apple', 'vegetable': 'potato'}

# update value
>>> my_dict['vegetable'] = 'aspargus'
>>> my_dict
```
We can also add new elements to our dictionary:
```python
# add item
>>> my_dict['meat'] = 'beef'  
>>> my_dict
```

Get length of a list or dictionary:
```python
>>> my_list = ['a','b','c','d','e']
>>> len(my_list)
>>> my_dict = {'fdm': 'makerbot', 'sla': 'formlabs'}
>>> len(my_dict)
```

# Scripting

Until now, we have been executing python code within the shell. Most of the code us however written within files, called script, and then executed at once. Python is an interpreted language, this means that each line of the script will be executed one after the other. At this point, you should still be using Spyder from your OS. If you did not install Spyder yet, please go back to [Section 01](./01-running-python3.md). We are going to use the left large pane of Spyder to write our first script.

[<img src="https://i.postimg.cc/43zp7Kh0/spyder-browse.png">](https://i.postimg.cc/43zp7Kh0/spyder-browse.png)


The first thing you should do is change your Working Directory to a folder where you would like to save your scripts. When launching a python script, the script must be executed from a certain position within your computer. This will affect which files the script will have access and how it can access them. In my case, I am going to work in a Temporary folder than is in my home folder. Press the Browse button as shown in the screenshot above to change your WD.

Once you have setup your WD, click on the New File button in the top left side corner or by doing File > New File. Start by Saving this new script in the same folder as the previously chosen WD, I called mine `helloworld.py`.
Add a line in your script that contains:
```python
print("Hello World")
```
Your script and Spyder setup should look like this one:

[<img src="https://i.postimg.cc/pTmC9VR5/spyder-helloworld.png">](https://i.postimg.cc/pTmC9VR5/spyder-helloworld.png)

In order to run your script, press the green Play button in the top toolbar or use F5. once you do so, Spyder will ask for some additional parameters before executing the script:

[<img src="https://i.postimg.cc/ZnKTPQsN/spyder-runset.png">](https://i.postimg.cc/ZnKTPQsN/spyder-runset.png)

* `Execute in current console` means that we want Spyder to execute the script within the console visible in the bottom right side corner
* `Remove all variables before execution` means that we want Spyder to clear its variable memory at the end of the script
* `The current Wordking Directory` means that we want Spyder to execute the script within the WD we defined

After pressing `Run` your script will run and you should be able to see the output of your script in the bottom right corner Python console:

```python
In [1]: runfile('/home/ilyass/Temp/helloworld.py')
Hello World
```

:tada::fire::sparkles: Congratulations :sparkles::fire::tada:
You just executed your first Python script, the traditional `Hello World`.

You can use all of the commands and functions we previously used within a script. You should try to solve the following exercises by relying on scripts instead of by using the Python shell.

# Exercises

  * **Fibonacci**: Write a script that asks the user how many Fibonacci numbers to generate, then generates them and prints them as a list. Fibonacci sequence: $x_n = x_{n-1} + x_{n-2}$
  [Solution](./examples/ex_fibonacci.py)
  * **Divisors**: https://www.practicepython.org/exercise/2014/02/26/04-divisors.html
  * **Common elements in lists**: Write a script that prints all elements common to both lists below, and then prints all elements common to both list and divisible by 7. 
  [Solution](./examples/ex_listcommon.py)
  ```
  l1 = ["42", "11", "33", "97", "63", "86", "4", "46", "72", "88", "59", "55", "13" ]
  l2 = ["24", "98", "56", "59", "3", "42", "14", "37", "75", "5", "34", "63", "4" ]
  ```

# Project: Caesar cipher

The Caesar cipher is one of the earliest known ciphers, it is also quite simple as the encryption and decryption process can easily be done using pen and paper. Suetonius described the Caesar cipher is his book *Life of Julius Caesar*: 

>"If he had anything confidential to say, he wrote it in cipher, that is, by so changing the order of the letters of the alphabet, that not a word could be made out. If anyone wishes to decipher these, and get at their meaning, he must substitute the fourth letter of the alphabet, namely D, for A, and so with the others."
[Suetonius, Life of Julius Caesar 56](https://en.wikipedia.org/wiki/Caesar_cipher)

More detailed explanation from Wikipedia:

> In cryptography, a Caesar cipher, also known as Caesar's cipher, the shift cipher, Caesar's code or Caesar shift, is one of the simplest and most widely known encryption techniques. It is a type of substitution cipher in which each letter in the plaintext is replaced by a letter some fixed number of positions down the alphabet. For example, with a left shift of 3, D would be replaced by A, E would become B, and so on. The method is named after Julius Caesar, who used it in his private correspondence.
[Caesar cipher, Wikipedia]((https://en.wikipedia.org/wiki/Caesar_cipher))

Try it for yourself: http://practicalcryptography.com/ciphers/caesar-cipher/

Your goal is to: **Write a caesar cipher program to encode and decode messages.**
Below are some helpful functions.

Need the alphabet as a string ? 
```python
>>> import string
>>> string.ascii_lowercase
```
Position of the letter `t` in the alphabet (start counting from 0) ?
```python
>>> import string
>>> alphabet = string.ascii_lowercase
>>> alphabet.find("t")
```

Add character to a new string using character's position in the alphabet:

```python
>>> import string
>>> alphabet = string.ascii_lowercase
>>> new_character = alphabet[8]
>>> encrypted_message = ""
>>> encrypted_message += new_character
>>> new_character = alphabet[22]
>>> encrypted_message += new_character
>>> encrypted_message
```

[Need more string manipulation methods ?](https://docs.python.org/3/library/string.html)
You should now be able to write a nice Caesar's cipher encoder/decoder.
Once you're done, a possible solution is available [here](./examples/ex_caesarcipher.py) .

---

[>>> You should now move on to the next session.](./05-functions.md)
[<<< Feel like you need to review a few things in the previous session ?](./03-strings-and-integers.md)