# Ma version
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

# Version Clement
```mocodo
:

PASSAGER:numUtilisateur, nom, adresse, avis

AvisP, 0N PASSAGER, 0N CONDUCTEUR : avis

:


SeFaitTransporter, 1N PASSAGER, 11 TRAJET

AvisC, 0N CONDUCTEUR, 0N PASSAGER : avis

CONDUCTEUR:numUtilisateur, nom, adresse, avis, date_agrement

Possède, 01 CONDUCTEUR, 11 VEHICULE


Départ, 0N VILLE, 11 TRAJET : nomVille

TRAJET: noTrajet, villeDep, villeAri, heureDes, conducteur, passager, longueur, tarif

Conduit, 1N CONDUCTEUR, 11 TRAJET 

VEHICULE: matricule, type, marque, energie, nbrPlace, dateMiseEnCirculation, numUtilisateur


VILLE: nomVille

Arrivé, 0N VILLE, 11 TRAJET : nomVille

:
```
# Version Léa
```mocodo
AVIS2, 1N PASSAGER, O1 CONDUCTEUR : avis
PASSAGER: numPassager, nom, adresse, avis, dateAgrement
SEFAITCONDUIRE, ON TRAJET, IN PASSAGER
ARRIVÉ, 11 VILLE, 11 TRAJET : nomVille

CONDUCTEUR: noConducteur, nom, addresse, avis, dateAgrement
AVIS1, 1N CONDUCTEUR, 01 PASSAGER : avis
TRAJET: noConducteur, date, villeDep, villeAri, heureDes, passager, longueur, tarif
VILLE: nomVille

POSSÈDE, IN CONDUCTEUR, ON VEHICULE
VEHICULE: matricule, type, marque, energie, nbrPlace, dateMiseEnCirculation, numUtilisateur
UTILISÉ, 11 VEHICULE, 1N TRAJET
DÉPART, 11 VILLE, 11 TRAJET : nomVille
```
...