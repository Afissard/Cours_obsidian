réexplicitions des fonctions recursive
voir fichier source et pdf sur #Madoc 

# Fibonacci récursif
exemple avec la suite (ou toute autre suite) de Fibonacci (encore avec les lapins (retour des problèmes génétiques))
## Implémentation naïve
Problème lors de grand appelle -> rallonge grandement le temps d'exécution -> "arbre d'appel de fonction" donc gourmant
Problème : on recalcule des valeurs déjà calculer
Solution : utiliser un tableau pour stocker les valeur calculé, pour allez les chercher au lieu de les recalculer, on ne calcule plus qu'une seule fois chaque valeur de la suite (voir schéma arbre de l'algo modifié)