## Indentation in python

As we will see later, `python` uses indentations (spaces at the beginnig of a line) to order the code and separate between different cases. 

For example, a "for loop" is written like this:

```
for x in "banana":
    print(x)
```

The code here changes the value of the variable `x` at each loop, the value `x` will consecutively take the value of each caracter in the word "banana", which means `x = b`, then `x = a`, then `x = n`, ...

If you execute this code yourself, the result will thus be:
```
b
a
n
a
n
a

```

Ok, now that we have a functional example that we understand, let 's get back to our indentation issue. We will now focus on this line:

```
    print(x)
```
Before the function `print(x)`, there are four spaces (exactly four). If we omit these spaces, the code will not execute as the content of the for loop is actually everything that is indented.
Let's add another line to our "for loop".

```
for x in "banana":
    print(x)
    print(1)
```

The result for this one is:
```
b
1
a
1
n
1
a
1
n
1
a
1

```
What is really important here for us are again the indentations before `print(x)` and `print("1")`. Again there are four spaces before each line. If we now replace the four spaces before `print("1")` by a Tabulation, visually, it will look the exactly the same:

```
for x in "banana":
    print(x)
    print("1")
```
But in reality, the "spaces" before `print(x)` and `print("1")` are different.
So if we run this code, this time we will get:
```
  File "<stdin>", line 3
    print("1")
             ^
TabError: inconsistent use of tabs and spaces in indentation
```
So it will be important to agree (ideally, the whole world) on what kind of indentation (four spaces? five spaces? one space? or tabs?) we will all be using.


This will surely cause problems from time to time when:
1. You copy code from your browser and the code you copied is using "Tab spaces", while you used four spaces
2. You work with another person who regularly updates your code, but that person uses four spaces, while you used Tab spaces.

## Consensus

There is actually a definitive answer [here](https://www.python.org/dev/peps/pep-0008):  
the  `Style Guide for Python Code - PEP8`.
A global consensus was reached around almost everything python related, all these conventions are provided in the PEP8 Style Guide.
As the document starts by stating: "This document gives coding conventions for the Python code comprising the standard library in the main Python distribution".

The specific section related to the four spaces / Tabs space issues is can be found [here](https://www.python.org/dev/peps/pep-0008/#tabs-or-spaces).

