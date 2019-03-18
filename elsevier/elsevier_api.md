
## Elsapy

The files `Connector.py`, `Query.py`, `ScopusDocument.py` and `main.py` can be used to perform a query to Elsevier's API.
Before using them, you will need to install the elsapy python package, you can do so by doing:
```
pip3 install elsapy
```
You will also need an API key from Elsevier (as a `config.json` file) in order to be able to perform queries, you can ask me to send you mine so you can write some code using it.

#### Usage

To use the code go to `learning_python3/elsevier` and:
```
python3 main.py <query>
```
where `<query>` is the key word being researched.

#### Classes

The code proposed here uses classes. You might want to take a look at Session-06 (which is about classes) to better understand how classes work.

## 