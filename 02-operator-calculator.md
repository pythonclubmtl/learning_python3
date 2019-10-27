<!-- $theme: default -->
<!-- footer: #python - 02  -->
<!-- $size: 16:9 -->
<!-- page_number: true -->

# Python 02

Open your favorite Python prompt.

1. [Operators](#operators)
2. [Variables](#variables)
3. [Comparison Operators](#comparison-operators)
4. [Logical Operators](#logical-operators)
5. [Print](#print)

---

# Operators

In order to try Python's simplest feature, using Python as a calculator, we need to understand how to perform basic mathematical operations with Python.
Enter Python in the interactive mode by typing `python3` in a terminal (`Ctrl`+`Alt`+`T`):
```python
    >>>
```
Let's use python as a calculator to practice a bit with operators, try to guess what each operator stands for: 
```python
    >>>  42+2

    >>>  42-4
```
These two are self-evident.
```python
    >>>  42/240
```
---

These ones are also quite obvious, right ?

Next ones are less often used:
```python
    >>> 42//5
    8
```
The `//` stands for floor division. In this case `5 * 8 = 40` and the remainer of this divsiion will be `2`. Let's get the remainer using the Modulus operator:
```python
    >>> 42%5
    2
```
The last operator is the Exponentiation operator:
```python
    >>> 42**5
    130691232
```
Now that we know our operators a bit, here are some additional operations you can perform yourself, just to be sure you memorize them well.


### Exercise 1:

Which operations result in 8?

1. `0 + 8`
2. `4 4`
3. `8 /`
4. `65 // 8`
5. `17 % 9`
6. `2 * * 4`
7. `64 ** 0.5`


# Variables

Variables can be used to conveninetly re-use values that you might need several times.

You might have noticed that we used the number 42 several times in the previous section. We had to retype 42 each time we needed to perform our operations, which is kind of tedious and increases error chances, and we can actually avoid that.
In addition, let's suppose we want to apply these operations to another number, we would have to re-write them all with a different number.
Let's introduce variables to address these issues:


This is howyou can affect (put) the value `42` to (in) the variable (box) `a`:
```python
    >>> a = 42
```

The prompt should not provide any answer, but we can easily check to see if it worked by checking the value of `a`, you can do that simply by typing `a`:
```python
    >>> a
    42
```

The prompt will print `42`, which the rigth value we just put in the box `a` (imagining variables as boxes sometimes help).
We can now perform our operations:
```python
    >>> a+2
    44
    >>> a-4
    40
    >>> a/240
    0.175
    >>> a//5
    10
    >>> a%5
    2
    >>> a**5
    130691232
```   

You can now change the value of `a`, for example:
```python
    >>> a = 51
```
Now, try pressing the top arrow of your keyboard while you are in the python prompt. Each time you press the top arrow, you should see your previous commands appear in inverse chronological order.

Press enter to re-execute one of the previous commands. This time, the result will be different as the value of `a` changed:
```python
    >>> a = 42
    >>> a%5
    2
    >>> a = 51
    >>> a%5
    1
```


# Comparison Operators

Try these: 

```python
>>> a = 5
>>> b = 7
>>> a>b
False
>>> a<b
True
```
Comparison operators compare the values on either side of the operand and determine the relation between them. The answer you obtain will be a Logical answer: `True` or `False`. There are more comparison operators: `==`, `!=`, `<>`, `>`, `<`, `<=`, etc...

Try to guess what each one of these is for:

```python
>>> a = 5
>>> b = 7
>>> a==b
False
>>> c=7
>>> b==c
True
```
The `==` operator compares two variable to determine if they are exactly the same or not.
The oppostite of this operator is `!=`:

```python
>>> a = 5
>>> b = 7
>>> a!=b
True
>>> a!=a
False
```
These two operators can be replaced by simpler versions: `is` and `is not`.
```python
>>> a = 5
>>> b = 7
>>> c = 7
>>> a is b
False
>>> a is a
True
>>> b is c
True
>>> a is not b
True
>>> a is not a
False
```

Comparison operators can also be combined with operators:
```python
>>> a = 5
>>> b = 7
>>> a is b
False
>>> a+2 is b
True
```

### Exercise 2:

In this exercise, we are going to introduce an additional operator that we will detail and use more later during the workshop: `+=`. 

Let's first take a look at the `+=` operator:
```python
>>> a = 3
>>> b = 42
>>> a = a + b
>>> a
45
```

The `+=`, sometimes called `iadd`, is actually the equivalent of the `a = a + b` line:
```python
>>> a = 3
>>> b = 42
>>> a += b
>>> a
45
```
Which means that the `+=` operator will basically add to the left side variable the right hand variable **and** will store the result in the left side variable.

> You are responsible for the finances of a small lemonade stand. Customers can buy 3 different produts from your stand: **l**emonade, **p**opcorn or **w**ater. The persone who actually stays at the stand (and writes down the list of products sold) gives you back a list of letters at the end of the day that corresponds to that day's sales. The list you're given that day:
```
l
l
p
w
l
w
p
l
w
p
l
l
w
```
> You also know the price of each product (provided in the Table below). Could you find a way to quickly determine the total of sales for the day using your Python console, the `+=` operator and 3 variables ?

| |**L**emonade| **P**opcorn | **W**ater |
|-|-------------|-|-|
|Price [1]|2|3|1|

When using a Python shell, you can use the top arrow in order to cycle back through  the previous commands you type.

# Logical Operators

Logical (or boolean) operators can be used to determine if conditional statements are true or false.

Until now, we have only used integer variables. Here, we are going to introduce a different type of variables: boolean variables. There are only two possible boolean varialbes, as we have seen with Comparison operators: `True` or `False`.

We can apply 2 different Logical operators between boolean variables: `AND` and `OR`; the last logical operator has to be applied to a boolean variable: `NOT`

Let's play around with some logical statements:
```python
>>> A = True
>>> B = False
>>> A and B
False
>>> A or B
True
```

Examples with `NOT`:

```python
>>> not B and B
False
>>> not B and not B
True
```

It is possible to stack these expressions in order to build complex expressions:

```python
>>> (A or B) and (A or B)
True
```

---


# Print

Currently, the result of each command is always automatically printed on screen by your Python command line interface, that is only because you are currently using a Python shell. In practice, Python is mostly used by executing or writing scripts, which are `.py` python files. In that case, Python will not print on screen the result of each line, that means that a series of command, such as the previous ones, will yield a very different results if they were written in a script:

Script:
```python
a = 42
a%5
a = 51
a%5
```

Result on terminal:
```
```

The script will not be very helpful, as it would display nothing as a result, since Python will not automatically print the result of each line. In order to actually print something, a function is necessary. We will explore functions more in details later, but for now, we just need to know that functions can take input, which is written between parenthesis after the command name. Thus, to actually print something, we will need:

```python
print(a)
```
We'll get back to `print()` later in our sessions.
