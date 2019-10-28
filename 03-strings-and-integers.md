# Python 03

1. [Strings](#strings)
  a. [len()](#len)
  b. [string arrays](#string-arrays)
  c. [Exercise 1](#exercise-1)
2. [Types](#types)
  a. [Exercise 2](#exercise-2)
3. [Simple String methods](#simple-string-methods)
  a. [Check String][#check-string]
  b. [Exercise 3][#exercise-3]

[<img src="https://i.postimg.cc/5N2bdFCR/pythonswap.png">](https://i.postimg.cc/5N2bdFCR/pythonswap.png)


# Strings

In programming, a string is a sequence of characters. These characters can be a literal constant (such as a name we want to save) or some kind of variables.

The symbol that represents a string in python is the `""` or `''`, if these values surround any set of characters, then that set of characters is a string.

Let's assign a string to a variable:
```python
>>> a = "hello"
>>> a
'hello'
```
Notice that I defined my string using the double quotation marks `"hello"`, while Python printed the string with single quotation marks `'hello'`. These two are interchangeable and necessary in order to be able to define strings that contain quotation marks:
```python
>>> a = 'hell"o'
>>> a
'hell"o'
```

## len()

Any string in Python is already, internally, defined as an array/list. You can this easily manipulate it. Since it is a list, we can easily get the length of any string using the `len()` function:
```python
>>> a = "If you torture the data long enough, it will confess."
>>> len(a)
53
```
Just like `print()`, `len()` is a function, so it will always be followed by double parenthesis that contain the function input(s). In this case, the input is our string, `a`. The length function returns a length of 53 characters for the input `a`.

Notice than the `len()` function does not accept integer types. If you try to input an integer in `len()`, Python will return an error.

## string arrays

In order to print values stored in an array or a list with the Python syntax, we will use the `list` type symbols `[]`. We will explore lists in more details in the next session, but since Python also sees strings as lists, this will serve as an early introduction to lists. 
Let's try to print a specific character, the first and the last characters, of a string:
```python
>>> a = "If you torture the data long enough, it will confess."
>>> len(a)
53
>>> a[0]
'I'
>>> a[52]
'.'
>>> a[-1]
'.'
>>> a[-53]
'I'
```
The first thing we did here is determine the length of our string, `53`. Then, we simply used `a[0]` in order to print the first element of the list `a`. Python starts counting from `0`. Thus, since the list contains `53` elements and that we start counting from `0`, that means that the index of the last element is going to be `52`. We can thus print the last element of the string with `a[52]`.
Python also allows negative indexing, for which it starts counting at `-1`. We can thus also print the last element of the string using `-1`: `a[-1]`. And the last one, using `a[-53]`.

These notations can also be used for slicing a string into smaller parts, let's try to extract the word `data` out of the string `a`:
```python
>>> a = "If you torture the data long enough, it will confess."
>>> a[15:20]
'the d'
>>> a[20:24]
'ata '
>>> a[19:24]
'data '
```
Using the `[:]` syntax, that can also be used with lists, we are able to slice a long string into smaller parts. 

PS: A list is a 1D array, it can also be called a vector.


### Exercise 1

In the following code snippet, you must insert a value/variable and the `len()` function where the `__` symbols are in order to get the exact same result as the one showed in the snippet:

```python
>>> a = "If you torture the data long enough, it will confess."
>>> a[ 0 : __ - __ ]
'If you torture the data long enough, it will confess'
```



# Types

You can check the type of any variable using the `type()` function:

```python
>>> a = 5
>>> type(a)
<class 'int'>
>>> a = "hello"
>>> type(a)
<class 'str'>
```

You can see here that `a` was at first an integer, and the became a string when the value `hello` was affected to it.
The `type()` function is extremely important when debugging and should not be forgotten. Often, we will try to perform an operation between two objects, such as:

```python
>>> a = "42"
>>> b = "24"
>>> a+b
'4224'
```

Notice that here, we can perform the "addition" between two strings which simply concatenates both objects and returns a string. However, let's suppose that we made a mistake and that we instead wrote:

```python
>>> a = "42"
>>> b = 24
>>> a+b
Traceback (most recent call last):
  File "<stdin>", line 1, in <module>
TypeError: can only concatenate str (not "int") to str
```

In this case, we get an error. The trace says that the error is a **TypeError**, and that we tried to do a forbidden operation: `can only concatenate str (not "int") to str`. This statement means that we can only concatenate strings to strings, not to integers. This also means that we provided an integer instead of a string. Since we are a dealing with a **TypeError**, we can investigate it properly in order to find a solution. Let's look into the types of the variables we are trying to concatenate:

```python
>>> a = "42"
>>> b = 24
>>> type(a), type(b)
(<class 'str'>, <class 'int'>)
```

We can thus immediately see that the variable `b` is an integer and is the source of our problem. Of course, in this case, the debugging was pretty easy. In practice, your variables will not have been defined the line right before the concatenation, they might be the result of several functions being applied in a row, which will easily lead to confusion. In order to be able to face bugs and error messages, it is necessary to always try to carefully read the `Traceback`. 

```python
>>> a+b
Traceback (most recent call last):
  File "<stdin>", line 1, in <module>
TypeError: can only concatenate str (not "int") to str
```

The Traceback will provide you with most of the information you need in order to determine how you should investigate your problem. This is not always true as in some cases your understanding of the technical vocabulary employed in the Traceback could be limited, but that is often due to a limited knowledge of the technical vocabulary used in the package. It is always good to Google the last line of your Traceback, the error itself, in the case, the `TypeError` line. Always try that first, and hope for a Stack Over Flow answer with a very high score as a first Google result. 

### Exercise 2

1. Analyze and try to understand the error message returned by Python when you try to input an integer into the `len()` function
2. Determine the length of the word `pneumonoultramicroscopicsilicovolcanoconiosis`, which is a *"lung disease contracted from the inhalation of very fine silica particles, specifically from a volcano; medically, it is the same as silicosis" (Wikipedia)*
3. Define a variable `a` that contains a boolean variable and print its type with the `type()` function


# Simple String methods

`type()`, `len()` and `print()` are Python standard functions. These functions can be used at any time within a Python console. They are independent of the variable used as an input as they can accept any object. They will return an error message if the object is not of the expected type though, as you have seen in [Exercise 1](#exercise-1) with integers and `len()`.

Python also has a set of built-in functions/methods that can be used on any string object. These functions are automatically available with any string object. The first method that comes with string types is the `.strip()` method:
```python
>>> a = " HELLO "
>>> a
' HELLO '
>>> a.strip()
'HELLO'
```
Notice how the `.strip()` function does not apply the same way the `type()` or `len()` functions apply. That is because the `.strip()` functions is *built-in within all string types*. We will explain what this actually means when we get to the 6th session, classes. Until then, try to assume that, for Python, a string is a very specific type of objects, just like an integer or a boolean is, and that as soon as Python detects a string it puts it in a special type of box/variable that provides it with some special functions. As you might have noticed, we did not write anything within the parenthesis of `.strip()` when we applied to `a`, rather, we added the `.strip()` at the end of `a`. That is "because" *`.strip()` is specific to the string type*. 
The `type()`, `len()` and `print()` are different as they can accept any kind of object as an input.

Another string type built-in function is `.lower()`, which is very convenient when you're trying to find a specific string in a longer document. `.lower()` will return a string in lower case:
```python
>>> a = "HELLO"
>>> a.lower()
'hello'
```
`.upper()` does the opposite of `.lower()`.
These functions can be combined in order to perform them all in one line:
```python
>>> a = " HELLO "
>>> a.strip().lower()
'hello'
```
A very convenient string built-in method is the `.replace()` method. This method will replace a certain strings by another string, in your string. Let's take a look at an example instead:
```python
>>> a = "If you torture the data long enough, it will confess."
>>> a.replace("data", "ice cream")
'If you torture the ice cream long enough, it will confess.'
>>> a.replace(" ", "-")
'If-you-torture-the-data-long-enough,-it-will-confess.'
```

## Check String

In order to check if a string or character is present in another string, you can use the commands `in` or `not in`:
```python
>>> s = "Almost nothing was more annoying than having our wasted time wasted on something not worth wasting it on."
>>> "time" in s
True
```

### Exercise 3

Variables, reminder:

Which are correct variable assignments?

1. `a = 1 * 2`
2. `2 = 1 + 1`
3. `5 + 6 = y`
4. `seven = 3 * 4`

An assignment variable is done with the `=` operator and affects the right side value to the left side box/variable.


[>>> You should now move on to the next session.](./04-lists-and-dicts.md)
[<<< Feel like you need to review a few things in the previous session ?](./02-operator-calculator.md)