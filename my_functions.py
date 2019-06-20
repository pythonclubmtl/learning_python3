# - *- coding: utf- 8 - *-
import csv
from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.model_selection import train_test_split
from sklearn.naive_bayes import ComplementNB
from joblib import dump, load
import os
import glob
import bibtexparser
from sklearn import preprocessing

# ================================================================================================================================
# It goes to the folder_path and gets all the csv files and put their abstracts and labels in abstracts_csv and label_csv lists
# ================================================================================================================================
def csv_reader():
    folder_path = '/home/kachic/PythonFiles/bib_files'
    extension = 'csv'
    os.chdir(folder_path)
    files_list = glob.glob('*.{}'.format(extension))
    abstracts_csv=[]; label_csv=[]
    for files_name in files_list:
        with open(files_name) as file:
            table = csv.reader(file, delimiter=',')
            for row in table:
                if not row[10]:
                    pass
                else:
                    abstracts_csv.append(row[10])
                    label_csv.append(files_name.rsplit(".")[0])
    return abstracts_csv, label_csv, files_list

# ================================================================================================================================
# It goes to the folder_path and gets all the BibTex files and put their abstracts and labels in abstracts_bib and label_bib lists
# ================================================================================================================================
def bib_reader():
    folder_path = '/home/kachic/PythonFiles/bib_files'
    extension = 'bib'
    os.chdir(folder_path)
    files_list = glob.glob('*.{}'.format(extension))
    abstracts_bib=[]; label_bib=[]
    for files_name in files_list:
        with open(files_name) as bibtex_file:
            bib_database = bibtexparser.load(bibtex_file)
            for row in bib_database.entries:
                if not row.get("abstract"):
                    pass
                else:
                    abstracts_bib.append(row.get("abstract"))
                    label_bib.append(files_name.rsplit(".")[0])
    return abstracts_bib, label_bib, files_list

# ================================================================================================================================
# It gets the filename of a BibTex file (ending with .bib) and retunrs its abstract as a string.
# ================================================================================================================================
def bib_reader_predict(file_name):
    file='/home/kachic/PythonFiles/bib_predict/'+file_name
    extension = 'bib'
    with open(file) as bibtex_file:
        bib_database = bibtexparser.load(bibtex_file)
        for row in bib_database.entries:
            if not row.get("abstract"):
                pass
            else:
                abstract=row.get("abstract")
    return abstract

# ================================================================================================================================
# This function vectorizes.fit the abstracts and then dump it in 'vectorized_abstracts.joblib'
# ================================================================================================================================
def my_vectorizer(abstracts):
    vectorizer = TfidfVectorizer(min_df=5, ngram_range=(1,3))
    vectorizer.fit(abstracts)
    dump(vectorizer, 'vectorized_abstracts.joblib')
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
# labels (not vectorized) and the classifier.
# ================================================================================================================================
def my_classifier(abstracts, label, vectorizer, percentage_split = 0.33):
    # vectorizer=my_vectorizer(abstracts)
    abstracts_vect=transform_vect(abstracts, vectorizer)
    X_train, X_test, y_train, y_test = train_test_split(abstracts_vect, label, test_size=percentage_split, random_state=42)
    clf = ComplementNB()
    clf.fit(X_train, y_train)
    dump(clf, 'trained_data.joblib')
    return X_train, X_test, y_train, y_test, clf

# ================================================================================================================================
# This function predicts the abstracts that was split for the testing to see if they match their labels and gives us the % of
# success. It uses the classifier (clf) from the return of my_classifier.
# ================================================================================================================================
def my_score(X_test, y_test, clf):
    clf.predict(X_test)
    result_test = clf.score(X_test, y_test)
    print(result_test*100, '% success')

# ================================================================================================================================
# This function gets a text in form of string and uses our classifier and vectorizer by loading their joblib files, and predict
# the class corresponding to the abstract. It retunrs the predicted class, the probability (range:0-1) of matching, and a list
# of classes
# ================================================================================================================================
def my_predict(text):
    clf=load('/home/kachic/PythonFiles/bib_files/trained_data.joblib')
    vectorizer=load('/home/kachic/PythonFiles/bib_files/vectorized_abstracts.joblib')
    text_vect=transform_vect([text], vectorizer)
    predicted_category=clf.predict(text_vect)
    predicted_proba=clf.predict_proba(text_vect)
    classes=clf.classes_
    return predicted_category, predicted_proba, classes
