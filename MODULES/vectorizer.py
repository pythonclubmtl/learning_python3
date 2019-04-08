import csv
from sklearn.naive_bayes import ComplementNB
from sklearn.feature_extraction.text import TfidfVectorizer
from joblib import dump, load


# =============================================================================
# Import data set
# =============================================================================
def import_csv(file_path):
    file = open(file_path, "r")
    reader = csv.reader(file)
    y=[]; x=[]
    for row in  reader:
        y.append(row[0])         #classes (labels)
        x.append(row[1])         #documents (x)
    file.close()
    'y classes: 3dprinting - crypto'
    return x, y


# =============================================================================
# Vectorizer
# =============================================================================
def vectorizer_data(x):
    vectorizer = TfidfVectorizer(min_df=5, ngram_range=(1,3))
    X = vectorizer.fit_transform(x)
    dump(vectorizer, 'vectorizer.joblib')
    return X


file_path='3dprinting_crypto.csv'
(x,y)=import_csv(file_path)
X=vectorizer_data(x)
