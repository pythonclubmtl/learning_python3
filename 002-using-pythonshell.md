
# Using Python as a calculator: operators

### Exercise 1:

Enter Python in the interactive mode by typing `python3` in a terminal (`Ctrl`+`Alt`+`T`):

    >>>

Let's use python as a calculator to practice a bit with operators, try to guess what each operator stands for: 

    >>>  42+2

    >>>  42-4

These two are self-evident.

    >>>  42/240

These ones are also quite obvious, right ?

Next ones are less often used:

    >>> 42//5
    8

The `//` stands for floor division. In this case `5 * 8 = 40` and the remainer of this divsiion will be `2`. Let's get the remainer using the Modulus operator:

    >>> 42%5
    2

The last operator is the Exponentiation operator:

    >>> 42**5
    130691232

Now that we know our operators a bit, here are some additional operations you can perform yourself, just to be sure you memorize them well.

### Exercise 2:

Which operations result in 8?

1. `0 + 8`
2. `4 4`
3. `8 /`
4. `65 // 8`
5. `17 % 9`
6. `2 * * 4`
7. `64 ** 0.5`

---

# Using Python as a calculator with variables

Variables can be used to conveninetly re-use values that you might re-use several times. We will get started with a very short introduction to variables here.

You might have noticed that we used the number 42 several times in the first exercise. We had to retype 42 each time we needed to perform our operations, we can actually avoid that.
In addition, let's suppose we want to apply these operations to another number, we would have to re-write them all with the different number.
Let's introduce variables to address these issues.

Firstly, we affect the value `42` to the variable `a`:

    >>> a = 42

The prompt should not provide any answer, but we can easily check to see if it worked by checking the value of `a`, you can do that simply by typing `a`:

    >>> a
    42

The prompt will print `42`, which the rigth value we just put in the box `a` (imagining variables as boxes sometimes help).
We can now perform our operations:

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

You can now change the value of `a`, for example:

    >>> a = 51

Now, try pressing the top arrow of your keyboard while you are in the python prompt. Each time you press the top arrow, you should see your previous commands appear in inverse chronological order.

Press enter to re-execute one of the previous commands. This time, the result will be different as the value of `a` changed:

    >>> a = 42
    >>> a%5
    2
    >>> a = 51
    >>> a%5
    1
