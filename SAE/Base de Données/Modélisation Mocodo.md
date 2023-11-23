```Mocodo
Avis, 0N UTILISATEUR, 0N UTILISATEUR : avis

:
UTILISATEUR: numUtilisateur, nom, addresse, avis

:
Possède, 01 UTILISATEUR, 11 VEHICULE: numUtilisateur
Conducteur, 1N UTILISATEUR, 11 TRAJET : numUtilisateur
Passager, 0N UTILISATEUR, 1N TRAJET : numUtilisateur
:

VEHICULE: matricule, type, marque energie, nbrPlace, dateMiseEnCirculation, numUtilisateur
Utilisé, 11 VEHICULE, 1N TRAJET
TRAJET: noConducteur, villeDep, villeAri, heureDes, passager, longueur, tarif

:
Arrivé, 0N VILLE, 11 TRAJET : nomVille
Départ, 0N VILLE, 11 TRAJET : nomVille

VILLE: nomVille

```
![[Pasted image 20231123091538.png]]
Pas définitif ...