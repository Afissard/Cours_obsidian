```Mocodo
Avis, 0N UTILISATEUR, 0N UTILISATEUR : avis
UTILISATEUR: numUtilisateur, nom, addresse, avis, dateAgrement

:
Conducteur, 1N UTILISATEUR, 11 VEHICULE: numUtilisateur
Passager, 0N UTILISATEUR, 1N TRAJET : numUtilisateur
:

VEHICULE: matricule, type, marque, energie, nbrPlace, dateMiseEnCirculation, numUtilisateur
Utilisé, 11 VEHICULE, 1N TRAJET
TRAJET: noConducteur, date, villeDep, villeAri, heureDes, passager, longueur, tarif

:
Arrivé, 11 VILLE, 11 TRAJET : nomVille
Départ, 11 VILLE, 11 TRAJET : nomVille

VILLE: nomVille
```

...