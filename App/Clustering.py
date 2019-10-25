import numpy as np

from sklearn.cluster import DBSCAN
from sklearn import metrics
from sklearn.datasets.samples_generator import make_blobs
from sklearn.preprocessing import StandardScaler
# ================================================================================
import ml_functions as functions

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
# WE USE IT HERE TO UNDERSTAND HOW MANY CLASSES WE HAVE AND THEN COMPARE IT TO THE NUMBER OF CLUSTERS!
# ================================================================================================================================
(X_train, X_test, y_train, y_test, clf)=functions.my_classifier(abstracts, label, trained_vectorizer)

functions.my_score(X_test, y_test, clf)


(predicted_category1, predicted_proba1, classes)=functions.my_predict('')

print('Trained! These are the classes: ', classes)

X=X_train
labels_true=y_train

# #############################################################################
# This part is the main clustering part that you define the eps and min_samples
# #############################################################################
# Compute DBSCAN

db = DBSCAN(eps=1, min_samples=3).fit(X)
core_samples_mask = np.zeros_like(db.labels_, dtype=bool)
core_samples_mask[db.core_sample_indices_] = True
labels = db.labels_

# The main part is: Number of clusters in labels and noise if present. 
# The other values, you might or might not use.
#==============================================================================
n_clusters_ = len(set(labels)) - (1 if -1 in labels else 0)
n_noise_ = list(labels).count(-1)

print('Estimated number of clusters: %d' % n_clusters_)
print('Estimated number of noise points: %d' % n_noise_)
print("Homogeneity: %0.3f" % metrics.homogeneity_score(labels_true, labels))
print("Completeness: %0.3f" % metrics.completeness_score(labels_true, labels))
print("V-measure: %0.3f" % metrics.v_measure_score(labels_true, labels))
print("Adjusted Rand Index: %0.3f"
      % metrics.adjusted_rand_score(labels_true, labels))
print("Adjusted Mutual Information: %0.3f"
      % metrics.adjusted_mutual_info_score(labels_true, labels,
                                           average_method='arithmetic'))
print("Silhouette Coefficient: %0.3f"
      % metrics.silhouette_score(X, labels))

