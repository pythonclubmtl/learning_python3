from rake_nltk import Rake

def Kextract(x):
    r = Rake()
    r.extract_keywords_from_text(x)
    scores = r.get_ranked_phrases_with_scores()
    result = {}
    seuil = 10
    for score in scores: # Scores est une liste, pour laquelle chaque element est une liste egalement. Cette boucle for passe de score[1] a scores[2] etc... et prend chaque premiere valeur de la liste (le score associe au keyword) pour la mettre dans le dictionnaire result. Chaque loop du for ajoute une valeur au dico !
        if score[0] > seuil:
#            result[score[1]] = 0
            result[score[1]] = score[0]
    return result #Donne a manger x a Kextract(), elle te renvoie le dico result

textt='''In industry today, the use of vibratory finishing processes as a final manufacturing step is increasing rapidly. Through the ability of these processes to achieve stable material removal rates, very consistent results in the control of surface texture are achieved. Even though the importance of these processes to manufacturing industry is increasing, the fundamentals of the material removal mechanism have not yet been established, and the associated lack of scientific understanding is an obstacle for process optimization. This paper proposes a mathematical model of the material removal mechanism based on abrasive finishing theory. The proposed model is used to identify key parameters and analyze their effect on the material removal mechanism. Experimental tests were conducted to validate the proposed model and provide correlation with the results obtained from the theoretical analysis. For the first time, fundamental abrasive machining process parameters such as the equivalent chip thickness and specific cutting energy realized through vibratory finishing are revealed.'''

scores_per_keyword = Kextract(textt) # result = Resultat de la fonction a qui on a donne a manger textt (Ce que la fonction retourne). Cette ligne de commande ecrit ce resultat dans la variable scores_per_keyword !
print(scores_per_keyword)
