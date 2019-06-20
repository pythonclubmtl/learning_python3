# *-* utf-8 *-*
import my_functions as functions

# ================================================================================================================================
# This part takes files (bib or csv) from defined folders in the my_functions files, make a list of abstracts/labels
# vectorizes abstracts;
# ================================================================================================================================
(abstracts_bib, label_bib, files_list_bib)=functions.bib_reader()
(abstracts_csv, label_csv, files_list_csv)=functions.csv_reader()
label=label_bib+label_csv
abstracts= abstracts_csv+abstracts_bib
trained_vectorizer=functions.my_vectorizer(abstracts)

# ================================================================================================================================
# This part uses my_classifier function from my_functions file to split, train, and test the vectorized abstracts and reports the
# my_score which is the % of success. In the end it writes that it is trained and then introduces the classes in the database.
# ================================================================================================================================
(X_train, X_test, y_train, y_test, clf)=functions.my_classifier(abstracts, label, trained_vectorizer)

functions.my_score(X_test, y_test, clf)


(predicted_category1, predicted_proba1, classes)=functions.my_predict('')

print('Trained! These are the classes: ', classes)
