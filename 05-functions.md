# Python 05

1. [Functions](#functions)
2. [Exercises](#exercises)
3. [Project: Baby names NY](#project-baby-names-ny)

Project: Baby names NY

# functions

> A function is a group of connected statements (code) that perform a specific task.

A function usually looks like this:

```python
def function_name( input_variables ):
   something happens
   if something is True:
       then something else
   else:
       then stuff here
   maybe even another thing
   return output_variables
```

* Functions help break our code into **smaller** and **modular** parts. 
* Functions make larger codes more **organized** and **manageable**
* A function does not necessarily **return** something
* When called, the content of the function is executed sequentially.


Let's write a function which tells us if today is Monday.
We will use the `datetime` package (provided with python), open your python shell:

* `date` refers to a "class" from the `datetime` package, which contains a function, `today()`, that returns today's date. Try it:

```python
>>> from datetime import date
>>> date.today()
>>> datetime.date(2019, 1, 28)
```
* `datetime` also provides a function which finds the day of the week for a specific date (https://docs.python.org/3/library/datetime.html#datetime.date.weekday):
```python
>>> from datetime import date
>>> today = date.today()
>>> isitmonday = today.weekday()
>>> isitmonday
>>> 0 #Because I executed this on a Monday 
```

Now that we're able to determine if today is a Monday or not, let's write our function:

* Our function will take the date as an `input_variable`
* It will return a certain message if it is Monday and a different one if it isn't

```python
from datetime import date

def monday_check(specimen_date):
    if specimen_date.weekday() == 0:
        message = "Monday again ... Go away Monday!"
    else:
        message = "Today is not a Monday!"
    return message
```

Let's now call our function in our script *(to execute a script `python3 script.py`)*:
```python
#IMPORTS
from datetime import date

#FUNCTIONS
def monday_check(specimen_date):
    if specimen_date.weekday() == 0:
        message = "Monday again ... Go away Monday!"
    else:
        message = "Today is not a Monday!"
    return message

#SCRIPT
print("This program will tell you if it is already the worst day of the week.")
today = date.today()
print( monday_check(today) )
```
Try this code: https://github.com/pythonclubmtl/learning_python3 -> `ex_mondaycheck.py`


# Exercises

##### Perfect numbers

 > In number theory, a perfect number is a positive integer that is equal to the sum of its proper positive divisors, that is, the sum of its positive divisors excluding the number itself. Equivalently, a perfect number is a number that is half the sum of all of its positive divisors (including itself).
>The first perfect number is 6, because 1, 2, and 3 are its proper positive divisors, and 1 + 2 + 3 = 6. 
>Equivalently, the number 6 is equal to half the sum of all its positive divisors: ( 1 + 2 + 3 + 6 ) / 2 = 6. 
 
* Your function should input a **number** (any integer number)
* Your function should return the **boolean value** `False` or `True`

> Hint: `message = False` affects the **boolean value** `False` to message. Not "false", `False`. `False` is not a string, not an integer, it is a boolean.

##### More exercises

* Go through: https://www.practicepython.org/exercise/2014/01/29/01-character-input.html
* Then this one: https://www.practicepython.org/exercise/2014/02/05/02-odd-or-even.html
* Next: https://www.practicepython.org/exercise/2014/03/05/05-list-overlap.html

# Project: Baby names NY

The dataset [Popular_Baby_Names_NY.csv](./datasets/Popular_Baby_Names_NY.csv) presents a list of the most popular baby names for the city of New York between 2011-2016. As you might notice after exploring the dataset, a count and rank are provided per baby name, per ethnicity, per year, per sex. You can easily find the most popular baby name for a certain year and a certain ethnicity, but determining the most popular baby name for the year 2012, regardless of the ethnicity or sex is quite complicated.

For this project, you will have 3 tasks:
1. Create a function (`get_csv_data`) that inputs a path (as a string) and returns the content of a CSV file as a list which itself contains each column as a list (without the header): `[[column_1], [column_2], ... , [column_n]]`
2. Write a script that provides (use your `get_csv_data` function in it):
* The **most popular female name** for **each year**
* The **most popular hispanic name for males between 2011-2016** 
* The **most popular female name for any ethnicity between 2012-2015**

```python
string.lower() # Converts given string into lowercase and returns it
max(list) # Returns maximum value from a list
set(list) # Returns a list without any duplicates
```
A detailed solution for the first task (without using functions though, you will have to take care of that) is [provided here](./datasets/ex_babynames.py).

---

[>>> You should now move on to the next session.](./06-classes.md)
[<<< Feel like you need to review a few things in the previous session ?](./04-lists-and-dicts.md)