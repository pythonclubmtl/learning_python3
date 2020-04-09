# Python club

### Sessions

0. [Getting python](00-getting-python.md)
1. [Running python](01-running-python3.md)
2. [Using python from the shell](02-using-pythonshell.md)
3. [Strings and integers](03-strings-and-integers.md) 
4. [Lists and dictionaries](04-lists-and-dicts.md)
    * Project: [Caesar cipher](#Caesar-cipher)
5.  [Functions](05-functions.md)
    * [Perfect numbers](./examples/ex_perfectnumbers.md)
    * Project: [NY baby names](#Baby-names-NY)
6. [Class](06-classes.md)

##### Python package crash course

* [Sympy](./tuto_snippets/sympy.md): Sympy allows you to perform symbolic computations with Python. Determine the analytical solution to complex problems.
* [Matplotlib](./tuto_snippets/tuto_matplotlib.py): a Python plotting library that produces publication quality figures in a variety of hardcopy formats and interactive environments.
* [TinyDB](./tuto_snippets/tinydb.md): a document oriented tiny database entirely written in python. The complete code source is less than 1500 lines, which makes it very efficient for datasets no more than a few hundred megabytes.

---

### Projects

1. [Caesar cipher](#Caesar-cipher) (After Lists and dictionaries)
2. [NY baby names](#Baby-names-NY) (After Functions)
3. [Make a Telegram bot](./projects/telegrambot/telgram_bots.md)
4. [Make a Slack bot](./projects/slackbot/making_a_slackbot.md)
   

##### Caesar cipher:

The Caesar cipher is one of the earliest known ciphers, it is also quite simple as the encryption and decryption process can easily be done using pen and paper. Suetonius described the Caesar cipher is his book *Life of Julius Caesar*: 

>"If he had anything confidential to say, he wrote it in cipher, that is, by so changing the order of the letters of the alphabet, that not a word could be made out. If anyone wishes to decipher these, and get at their meaning, he must substitute the fourth letter of the alphabet, namely D, for A, and so with the others."
[Suetonius, Life of Julius Caesar 56](https://en.wikipedia.org/wiki/Caesar_cipher)

More detailed explanation from Wikipedia:

> In cryptography, a Caesar cipher, also known as Caesar's cipher, the shift cipher, Caesar's code or Caesar shift, is one of the simplest and most widely known encryption techniques. It is a type of substitution cipher in which each letter in the plaintext is replaced by a letter some fixed number of positions down the alphabet. For example, with a left shift of 3, D would be replaced by A, E would become B, and so on. The method is named after Julius Caesar, who used it in his private correspondence.
[Caesar cipher, Wikipedia]((https://en.wikipedia.org/wiki/Caesar_cipher))

Try it yourself: http://practicalcryptography.com/ciphers/caesar-cipher/

Your goal is to: **Write a caesar cipher program to encode and decode messages.**
Below are some helpful functions.

Need the alphabet as a string ? 
```python
>>> import string
>>> string.ascii_lowercase
```
Position of letter `t` in the alphabet (start counting from 0) ?
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


##### Baby names NY

The dataset [Popular_Baby_Names_NY.csv](./datasets/Popular_Baby_Names_NY.csv) presents a list of the most popular baby names for the city of New York between 2011-2016. As you might notice after exploring the dataset, a count and rank are provided per baby name, per ethnicity, per year, per sex. You can easily find the most popular baby name for a certain year and a certain ethnicity, but determining the most popular baby name for the year 2012, regardless of the ethnicity or sex is quite complicated.

For this project, you will have 3 tasks:
1. Create a function (`get_csv_data`) which takes a path (as a string) and returns the content of a CSV file as a list which itself contains each column as a list (without the header): `[[column_1], [column_2], ... , [column_n]]`
2. Write a script that provides (use your `get_csv_data` function in it):
* The **most popular female name** for **each year**
* The **most popular hispanic name for males between 2011-2016** 
* The **most popular female name for any ethnicity between 2012-2015**

```python
string.lower() # Converts given string into lowercase and returns it
max(list) # Returns maximum value from a list
set(list) # Returns a list without any duplicates
```
A detailed solution for the first task (without using functions though, you will have to take care of that) is [provided here](./examples/ex_babynames.py).

---

### Extras:
* [Editors Four spaces VS tabs](02b-space-tabs.md)


[Keep going](learn_more.md)
