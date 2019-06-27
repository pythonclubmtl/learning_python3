# *-* utf-8 *-*
import my_functions as functions

# ================================================================================================================================
# This part gets a file or text of an abstract for prediction of its class; then predicts the class and prints all the classes, the predicted class related
# to the abstract, and the probability values (range:0-1) corresponding to each class.
# ================================================================================================================================
input1=''
while input1 != 'E':
    input1 = str(input('Predict Abstract (A) or File (F)? '))
    if input1.upper()=='A':
        abstract=str(input('Copy/Paste the abstract you want to test: '))
    else:
        if input1.upper()=='F':
            file=str(input('Please upload your file in bib_predict folder and write its name here: '))
            abstract=functions.bib_reader_predict(file)

    (predicted_category1, predicted_proba1, classes)=functions.my_predict(abstract)

    print("Classes", classes)
    print (predicted_category1, predicted_proba1)
    print ('Type "E" for exit.')
