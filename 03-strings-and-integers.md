# Storing numbers

In programming, a string is a sequence of characters. These characters can be a literal constant (auch as a name we want to save) or some kind of variables.
In the previous section, we actually already used a string [in the last section](0002-using-pythonsell.md) when we assigned integer values (42, 24, 51) to the string `a`.
In this section, we are going to manipulate strings a bit more.


### Exercise 1:

We'll get started with a few exercises involving variables. Try to guess the output of the python console when there's a _____.

```python
    >>> emily = 25952
    >>> hannah = 23073
    >>> khaleesi = 5
    >>> emily
        _______
    >>> hannah + 1
        ______
    >>> 3 * khaleesi
        ______
```

### Exercise 2:

Let's change the content. Insert the correct values and variable names into the blanks.
```python
    >>> emily = emily + 1
    >>> emily
        _____

    >>> all_babies = 0
    >>> all_babies = _____ + _____ + _____
    >>> all_babies
        49031
```

### Exercise 3:

Which of the following variable names are correct? Try assigning some numbers to them.

    Sarah
    ASHLEY
    madison alexis
    sam90
    2000jessy
    liz_lauren
    alyssa.kay

### Exercise 4:

Which are correct variable assignments?

* `a = 1 * 2`
* `2 = 1 + 1`
* `5 + 6 = y`
* `seven = 3 * 4`


### Types

You can check the `type` of any variable using the type command:

```python
>>> a = 5
>>> type(a)
<class 'int'>
>>> a = "hello"
>>> type(a)
<class 'str'>
```

You can see here that `a` was at first an integer, and the became a string when the value `hello` was affected to it.