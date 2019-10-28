# TinyDB

TinyDB is a tiny, document oriented database. TinyDB is not a relational database, meaning that it is not optimized for structured data, rather it is able to handle a variety of single documents. TinyDB is also not designed to handle very large amounts of data. It can handle datasets of a few hundreds of megabytes, a few gygabytes at most, but no more than that. TinyDB is extremely simple to use as it directly relies on the dictionary type of Python and the JSON filesystem.

## Download TinyDB

```
pip install TinyDB
```

## Get started with TinyDB in 5 minutes

```python
>>> from tinydb import TinyDB, Query
>>> db = TinyDB('path/to/db.json')
>>> User = Query()
>>> data_object = {'name': 'John', 'age': 22}
>>> db.insert( data_object )
>>> db.search(User.name == 'John')
[{'name': 'John', 'age': 22}]
```

## Setting up a TinyDB database

In order to start working with TinyDB, you first need to import the package, and then to select a JSON file that will contain our database.

```python
>>> from tinydb import TinyDB, Query
>>> db = TinyDB('db.json')
```
In this case, the file `db.json` would be the file where the database is saved. If the file you would like to use as your databse is not in the same folder as your Python script, you can write the path to your file instead of a file name.

## Insert documents in the database

We can insert any kind of Python dictionary in the database. TinyDB will recognize a dictionary and save it as a searchable object. Let's imagine that we are managing a lemonade stand. We are using TinyDB to keep track of our current stocks.

We have 7 lemonades and 3 waters left. We thus have two different `type` of objects, lemonade and water. Each type has a known count. Each object/product will thus have two **attributes**, type and count. We can write it this way:

* Product 1
  * Type: **lemonade**
  * Count: **7**
* Product 2
  * Type:  **water**
  * Count: **3**

If we translate this into python dictionaries, we can save these values into our TinyDB using its `.insert()` built-in function:

```python
>>> db.insert({'type': 'lemonade', 'count': 7})
1
>>> db.insert({'type': 'water', 'count': 3})
2
```

The `db` object we previously initialized as a `TinyDB()` class has a built-in method, `.insert()`, that allows us to insert a dictionary as a new document. In the previous code snippet, we actually inserted two new documents. The number (1, 2) Python returns is the id affected by TinyDB to the document.

We can get **all** the documents stored in a database using:
```python
>>> all_docs = db.all()
>>> all_docs
[{'type': 'lemonade', 'count': 7}, {'type': 'water', 'count': 3}]
>>> type(all_docs)
<class 'list'>
```
Notice that `.all()` returns all the documents of the database as a python list. We can thus easily iterate through these documents and manipulate them.

## Queries

The most interesting feature of a database is the ability to search and find very specific documents very quickly. In order to do so, we need to compose a query. The query will specify conditions for each attribute that are interesting to us. 
In order to compose a query, we first need to name this search. In this case, I will be looking for a product, so I am going to call this search Product (it is a dummy variable and can have any name you'd like):

```python
>>> Product = Query()
```

From now on, the variable `Product` actually represents a TinyDB query. We are going to look for Products in our database that are of the `type` lemonade:

```python
>>> db.search(Product.type == 'lemonade')
[{'type': 'lemonade', 'count': 7}]
```
We have to use the `.search()` built-in function of TinyDB in order to search with a query. We put as a parameter a comparison expression: `Product.type == 'lemonade'`. This last expression means that we are looking for documents/Products in our database that have a `type` attribute that is equal to "lemonade". The result we get is indeed the object about the lemonade, that is presented as a list again, with a single element this time.

We can use any kind of comparison operator in our query. Let's see which Products are lacking in our stocks so we can buy some more:
```python
>>> db.search(Product.count < 5)
[{'type': 'water', 'count': 3}]
```
The `count` of water is less than 5, actually 3.

## Updating

Let's say that we purchased some water, and that we now have a total of 20 waters. We need to update our database. In order to do so, we can use the built-in `.update()` method.
```python
>>> db.update({'count': 20}, Product.type == 'water')
[2]
>>> db.all()
[{'type': 'lemonade', 'count': 7}, {'type': 'water', 'count': 20}]
```
The `.update( dict, comparison )` function takes two inputs:
1. `dict`: The attribute that should be updated as a dictonary object. In this case, the count attribute should be changed to 20: `{'count': 20}`.
2. `comparison`: The second input is a comparison that returns all the objects that should be updated. In this example, it is used to specifically update the water type product, but it could be used with an `>` or `<` in order to update several documents at once.

After updating the database, it is possible to see that the water count was indeed updated by printing all the database documents.

## Removing

It is also possible to remove documents from the databse using the `remove()` built-in function. Let's say that lemonade is actually a product that does not sell that well in winter, it was thus decided to remove it from the products your lemonade stand offers. In order to delete it from the database, you can use:
```python
>>> db.remove(Product.type == "lemonade")
[1]
>>> db.all()
[{'type': 'water', 'count': 20}]
```

# Persistence

If you now exit your Python shell completely, you can start a new Python shell, load the same database and access your documents:
```python
>>> exit()
ilyass@tx1:~/pythonclubmtl$ python
Python 3.6.8 (default) 
[GCC 8.3.0] on linux
Type "help", "copyright", "credits" or "license" for more information.
>>> from tinydb import TinyDB, Query
>>> db = TinyDB('temp.json')
>>> db.all()
[{'type': 'water', 'count': 20}]
```
Building a script or a whole application that is able to save information on the hard drive, mostly using a database, and re-use it when a new instance is started is called adding persistence.

TinyDB does so by simply saving all the data in the db.json file. Since JSON is a human-friendly data interchange format we can directly read the file. In my case, the db.json file should be in the same folder as the one where I launched my Python shell.
```
>>> exit()
ilyass@tx1:~/pythonclubmtl$ ls
db.json
ilyass@tx1:~/pythonclubmtl$ cat db.json
{"_default": {"2": {"type": "water", "count": 20}}}
```
In the previous snippet, the linux terminal `cat` command is used to read the content of a file from the terminal. The result it returns is the content of the database which is the remaining Product, water.
