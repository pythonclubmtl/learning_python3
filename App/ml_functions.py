# - *- coding: utf- 8 - *-
import csv
from sklearn.feature_extraction.text import TfidfVectorizer
#from sklearn.feature_extraction.text import CountVectorizer
from sklearn.model_selection import train_test_split
from sklearn.naive_bayes import ComplementNB
from joblib import dump, load
import os
import glob
import bibtexparser
from sklearn import preprocessing
from nltk.corpus import stopwords
from nltk.tokenize import word_tokenize
import re
import nltk
from collections import Counter
import matplotlib.pyplot as plt


#from nltk.tokenize.moses import MosesDetokenizer
import string
nltk.download('stopwords')
nltk.download('punkt')


def untokenizer(token_sentences):
    sentences = "".join([" "+i if not i.startswith("'") and i not in string.punctuation else i for i in token_sentences]).strip()
    return sentences

# ================================================================================================================================
# This function filters the abstracts from stopwords!
# ================================================================================================================================
def stopwords_func(abstract):
    stop_words = set(stopwords.words('english'))
    word_tokens = word_tokenize(abstract)
    filtered_sentence = []
    for word in word_tokens:
        if word not in stop_words:
            filtered_sentence.append(word)
    filtered_sentence = untokenizer(filtered_sentence)
    return filtered_sentence

# ================================================================================================================================
# It goes to the folder_path and gets all the csv files and put their abstracts and labels in abstracts_csv and label_csv lists
# ================================================================================================================================
def csv_reader():
    folder_path = os.getcwd()+"/bib_files"
    extension = 'csv'
    os.chdir(folder_path)
    files_list = glob.glob('*.{}'.format(extension))
    abstracts_csv=[]; label_csv=[]
    for files_name in files_list:
        with open(files_name, encoding="utf8") as file:
            table = csv.reader(file, delimiter=',')
            for row in table:
                if not row[10]:
                    pass
                else:
                    clean_abstract=stopwords_func(row[10])
                    abstracts_csv.append(clean_abstract)
                    label_csv.append(files_name.rsplit(".")[0])
    os.chdir('..')
    return abstracts_csv, label_csv, files_list

# ================================================================================================================================
# It goes to the folder_path and gets all the csv files and put their abstracts and labels in abstracts_csv and label_csv lists
# And then it makes a graph of the high freq. words with their repeated values.
# ================================================================================================================================
def csv_reader_ploter():
    folder_path = os.getcwd()+"/bib_files"
    extension = 'csv'
    os.chdir(folder_path)
    files_list = glob.glob('*.{}'.format(extension))
    abstracts_csv=[]; label_csv=[]
    for files_name in files_list:
        with open(files_name, encoding="utf8") as file:
            table = csv.reader(file, delimiter=',')
            for row in table:
                if not row[10]:
                    pass
                else:
                    clean_abstract=stopwords_func(row[10])
                    abstracts_csv.append(clean_abstract)
                    label_csv.append(files_name.rsplit(".")[0])
            reg = re.compile('\S{4,}')
            s = str(abstracts_csv)
            c = Counter(ma.group() for ma in reg.finditer(s))
            dictc=dict(c)
            for key, value in sorted(dictc.items(), key=lambda item: item[1]):
               print("%s: %s" % (key, value))
            lists = sorted(dictc.items()) # sorted by key, return a list of tuples
            x, y = zip(*lists) # unpack a list of pairs into two tuples
            plt.plot(x, y)
            plt.show()
            import pdb; pdb.set_trace()

#            words=[]
#            values=[]
#            for x in c.items():
#                words.append (x[0])
#                values.append (x[1])
#            values, words = zip(*sorted(zip(values, words)))
#            values, words = (list(t) for t in zip(*sorted(zip(values, words))))
#            values.sort(reverse = True)
#            normalized_values = [float(i)/max(values) for i in values]
        plt.scatter(words, normalized_values)
    os.chdir('..')
    return abstracts_csv, label_csv, files_list

# ================================================================================================================================
# It goes to the folder_path and gets all the BibTex files and put their abstracts and labels in abstracts_bib and label_bib lists
# ================================================================================================================================
def bib_reader():
    folder_path2 = os.getcwd()+"/bib_files"
    extension = 'bib'
    os.chdir(folder_path2)
    files_list = glob.glob('*.{}'.format(extension))
    abstracts_bib=[]; label_bib=[]
    for files_name in files_list:
        with open(files_name, encoding="utf8") as bibtex_file:
            bib_database = bibtexparser.load(bibtex_file)
            for row in bib_database.entries:
                if not row.get("abstract"):
                    pass
                else:
                    clean_abstract=stopwords_func(row.get("abstract"))
                    abstracts_bib.append(clean_abstract)
                    label_bib.append(files_name.rsplit(".")[0])
    os.chdir('..')
    return abstracts_bib, label_bib, files_list

# ================================================================================================================================
# It gets the filename of a BibTex file (ending with .bib) and return its abstract as a string.
# ================================================================================================================================
def bib_reader_predict(file_name):
    file=os.getcwd()+"/bib_predict"+file_name
    extension = 'bib'
    with open(file) as bibtex_file:
        bib_database = bibtexparser.load(bibtex_file)
        for row in bib_database.entries:
            if not row.get("abstract"):
                pass
            else:
                abstract=row.get("abstract")
    os.chdir('..')
    return abstract

# ================================================================================================================================
# This function vectorizes.fit the abstracts and then dump it in 'vectorized_abstracts.joblib'
# ================================================================================================================================
def my_vectorizer(abstracts):
    vectorizer = TfidfVectorizer(min_df=5, ngram_range=(1,3))
    vectorizer.fit(abstracts)
    os.chdir(os.getcwd()+"/bib_files")
    dump(vectorizer, 'vectorized_abstracts.joblib')
    os.chdir('..')
    return vectorizer

# ================================================================================================================================
# This function vectorize.transform the abstracts, resulted from vectorizer.fit and return vectorized_sentences(abstract)
# ================================================================================================================================
def transform_vect(list_sentences, vectorizer):
    vecorized_sentences = vectorizer.transform(list_sentences)
    return vecorized_sentences

# ================================================================================================================================
# This function gets abstracts, label (name of ref files), and our vectorizer; then split them; train using ComplementNB
# and dump the classifier in 'trained_data.joblib' file. In the end it returns: vectorized abstract for train and test,
# labels (not vectorized) and the clas=sifier.
# ================================================================================================================================
def my_classifier(abstracts, label, vectorizer, percentage_split = 0.33):
    # vectorizer=my_vectorizer(abstracts)
    abstracts_vect=transform_vect(abstracts, vectorizer)
    X_train, X_test, y_train, y_test = train_test_split(abstracts_vect, label, test_size=percentage_split, random_state=42)
    clf = ComplementNB()
    clf.fit(X_train, y_train)
    os.chdir(os.getcwd()+"/bib_files")
    dump(clf, 'trained_data.joblib')
    os.chdir('..')
    return X_train, X_test, y_train, y_test, clf

# ================================================================================================================================
# This function predicts the abstracts that was split for the testing to see if they match their labels and gives us the % of
# success. It uses the classifier (clf) from the return of my_classifier.
# ================================================================================================================================
def my_score(X_test, y_test, clf):
    clf.predict(X_test)
    result_test = clf.score(X_test, y_test)
    result_percent=result_test*100
    print(result_percent, '% success')
    return (result_percent)

# ================================================================================================================================
# This function gets a text in form of string and uses our classifier and vectorizer by loading their joblib files, and predict
# the class corresponding to the abstract. It retunrs the predicted class, the probability (range:0-1) of matching, and a list
# of classes
# ================================================================================================================================
def my_predict(text):
    clf=load(os.getcwd()+'/bib_files/trained_data.joblib')
    vectorizer=load(os.getcwd()+'/bib_files/vectorized_abstracts.joblib')
    text_vect=transform_vect([text], vectorizer)
    predicted_category=clf.predict(text_vect)
    predicted_proba=clf.predict_proba(text_vect)
    classes=clf.classes_
    return predicted_category, predicted_proba, classes
