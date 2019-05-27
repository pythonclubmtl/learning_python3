
import csv
from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.model_selection import train_test_split
from sklearn.naive_bayes import ComplementNB
from joblib import dump, load

def csv_reader(path):
    with open(path) as file:
        table = csv.reader(file, delimiter=',')
        abstracts=[]; label=[]
        for row in table:
            if not row[10]:
                pass
            else:
                abstracts.append(row[10])
                label.append('ilyass')
    return abstracts, label

def csv_reader_crypto():
    with open('3dprinting-crypto.csv') as file:
        table = csv.reader(file, delimiter=',')
        crypto_text=[]; crypto_label=[]
        for row in table:
            if row[0] != '3dprinting':
                crypto_text.append(row[1])
                crypto_label.append(row[0])
    return crypto_text, crypto_label

def my_vectorizer(abstracts):
    vectorizer = TfidfVectorizer(min_df=5, ngram_range=(1,3))
    vectorizer.fit(abstracts)
    dump(vectorizer, 'vectorized_abstracts.joblib')
    return vectorizer

def transform_vect(list_sentences, vectorizer):
    vecorized_sentences = vectorizer.transform(list_sentences)
    return vecorized_sentences

def my_classifier(abstracts, label, vectorizer, percentage_split = 0.33):
    vectorizer=my_vectorizer(abstracts)
    abstracts_vect=transform_vect(abstracts, vectorizer)
    X_train, X_test, y_train, y_test = train_test_split(abstracts_vect, label, test_size=percentage_split, random_state=42)
    clf = ComplementNB()
    clf.fit(X_train, y_train)
    dump(clf, 'trained_data.joblib')
    return X_train, X_test, y_train, y_test, clf

def my_score(X_test, y_test, clf):
    clf.predict(X_test)
    result_test = clf.score(X_test, y_test)
    print(result_test, '% success')

#--------------------------------------------------------------------------------------------------
#PROGRAM
#--------------------------------------------------------------------------------------------------
(abstracts,label)=csv_reader('ilyassBib.csv')
(crypto_text, crypto_label)=csv_reader_crypto()
label=label+crypto_label
abstracts=abstracts+crypto_text
import pdb; pdb.set_trace()
trained_vectorizer=my_vectorizer(abstracts)
(X_train, X_test, y_train, y_test, clf)=my_classifier(abstracts, label, trained_vectorizer)
#import pdb; pdb.set_trace()
#my_classifier(X_train, y_train)
#import pdb; pdb.set_trace()
my_score(X_test, y_test, clf)
print('after my_predict ')

import pdb; pdb.set_trace()
