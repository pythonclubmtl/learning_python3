## Objectives

In this section, you will learn about conditional probabilities, Naive Bayes' theorem, and finally application of Naive Bayes' conditional probabilities as a classifier for class categorization.
The goal of this section is not for you to become an expert in conditional probabilities but rather to simply understand the theorem and its application as a classifier. We are doing this part as programmers not as mathematicians or statisticians.

You need to take notes during this work as you will need to present your work to your fellow pythonclubists. To do so, we will use Marp (https://github.com/yhatt/marp/).

## Naive Bayes classifiers

Get started by quickly reading the following page: https://www.python-course.eu/naive_bayes_classifier_introduction.php
**Stop reading before the beginning of the section "A Naive Bayes Classifier Example"**.

Take the time to understand the formulas and examples. You can also try the code examples in your VM (you will need matplotlib, install it using `pip install matplotlib --user`), we're also going to use this opportunity to install numpy that will be necessary later: `pip install numpy --user`.

Once you are done with the previous page, let's move on to something which is a bit more hands on, and focused on text analysis: https://medium.com/datadriveninvestor/understanding-naive-bayes-and-its-application-in-text-classification-99c38e739f88
Take some time to read the code proposed by the author (https://github.com/khalidbouziane/Naive-Bayes-for-text-classification/blob/master/NB.ipynb). You do not need to execute it (reading it and understanding it is enough), but you can do it by copy-pasting it to a `.py` file. If you'd like to do so, you will need pandas and scikit-learn, install them using `pip install pandas --user` and `pip install scikit-learn --user`.
If you're a bit confused about the format of the code you're reading, ask me about it.

## Vectorizers and TF-IDF

Open the following page: https://scikit-learn.org/stable/modules/feature_extraction.html#text-feature-extraction
Read through the page until section 4.2.3.4 and try the code snippets.

You can now vectorize and apply the TF-IDF transformation to a text files (plus you have a general idea of what it is you're actually doing as a bonus).

The next step is to then train a Naive Bayes classifier to categorize text, but before that, we're going to see how we can get rid of a lot of noise that will probably be useless for text classification.

## Stop words

Read this quick tutorial that explains how to remove stop words from text using NLTK: https://www.geeksforgeeks.org/removing-stop-words-nltk-python/
You will need NLTK: `pip install nltk --user`

## Complement Multinomial Naive Bayes

Finally, the last step is to learn how we can apply a Complement Multinomial Naive Bayes classifier to text data.
Read the intro of section 1.9, then sections 1.9.1, 1.9.2 and 1.9.3: https://scikit-learn.org/stable/modules/naive_bayes.html

Finally, carefully read : https://scikit-learn.org/stable/modules/generated/sklearn.naive_bayes.ComplementNB.html#sklearn.naive_bayes.ComplementNB
You should now be able to apply a CMNB to text data, it's time to practice your newly acquired skills !

## Application

Open and go through: https://scikit-learn.org/0.19/datasets/twenty_newsgroups.html

## Objectives

1. Write a file (called `modules/vectorizer.py`) that contains several functions that can be used in a row to perform TF-IDF vectorization of a list of strings.
2. Write another file (called `modules/classifier.py`) that either takes as an input a vectorizer object from the functions of the previous file or loads a `.joblib` vectorizer (see Notes) in addition to a dictionary of `{ labels: strings }` that are labels of a document and string documents. The file will contain several functions that generate a classifier (save it as a `.joblib`)
3. Write another function in the file called `modules/classifier.py` that inputs a `vectorizer.joblib`, a `classifier.joblib` and a string. The functions should output the class (or label) and the probability as a percentage of the document belonging to that class.

##### Notes

* The file's first function should first concatenate (with spaces in between) all the strings from the list to feed the complete vocabulary to the following functions.
* It is possible to feed the NLTK stopwords to the vectorizer (https://scikit-learn.org/stable/modules/feature_extraction.html#common-vectorizer-usage).
* You can also save a vectorizer or classifier as a `.joblib` file. You can then reload and re-use it later from another file or function: https://scikit-learn.org/stable/modules/model_persistence.html





