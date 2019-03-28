from rake_nltk import Rake

def Kextract(textt):
    r = Rake()
    r.extract_keywords_from_text(textt)
    scores = r.get_ranked_phrases_with_scores()
    result = {}
    seuil = 0
    for score in scores:
        if score[0] > seuil:
            result[score[1]] = 0
            result[score[1]] = score[0]
    return result

textt=''' Mais qu’est-ce que j’ai fait, mais qu’est-ce que j’ai fait » ont pu entendre les conseillers de Bruno Le Maire ce matin tandis que le ministre sortait en courant de son bureau. Quelques secondes plus tôt, celui-ci avait découvert qu’il venait de privatiser sa propre famille en lieu et place de Aéroports de Paris. « C’est dramatique mais c’est signé et en plus pour 70 ans » note un responsable. « Bruno Le Maire s’est engagé par écrit, les actionnaires devraient prendre possession de sa famille dès la rentrée septembre 2019 ». C’est un consortium chinois qui prendra livraison de l’entière famille de Bruno Le Maire. Contacté, le consortium s’est réjoui, soulignant que même le gouvernement chinois n’avait pas osé avoir cette idée brillante. Selon plusieurs sources, il semble que Bruno Le Maire signait plusieurs privatisations en même temps et n’aurait pas remarqué son livret de famille sous une pile de papiers. De son côté Edouard Philippe a tenu à féliciter son ministre de l’exemple qu’il donne et encourager ses autres ministres à faire de même. « Je suis sûr que les Français suivront cet exemple et je peux vous assurer que vos familles seront bien traitées.'''
scores = Kextract(textt)
print(scores)
