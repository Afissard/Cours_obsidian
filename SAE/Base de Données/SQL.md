# Version 1
```sql
DROP TABLE AvisP;
DROP TABLE AvisC;
DROP TABLE Passager;
DROP TABLE Trajet;
DROP TABLE Ville;
DROP TABLE Vehicule;
DROP TABLE Conducteur;



Create Table Passager
(
    nuPassager int PRIMARY KEY,
    nom varchar(16),
    adresse varchar(50),
    dateAgrement varchar(50)
);
Create Table Conducteur
(
    nuConducteur int PRIMARY KEY,
    nom varchar(16),
    adresse varchar(50),
    dateAgrement varchar(50)
);
Create Table AvisP
(
   noAvis int PRIMARY KEY,
   débiteur int,
   CONSTRAINT débiteur FOREIGN KEY (débiteur)
   REFERENCES Passager(nuPassager),
   concerné int,
   CONSTRAINT concerné FOREIGN KEY (concerné)
   REFERENCES conducteur(nuConducteur),
   avis varchar(50),
   estPositif BINARY_DOUBLE
);
Create Table AvisC
(
   noAvis int PRIMARY KEY,
   débiteur int,
   CONSTRAINT débiteur FOREIGN KEY (débiteur)
   REFERENCES conducteur(nuConducteur),
   concerné int,
   CONSTRAINT concerné FOREIGN KEY (concerné)
   REFERENCES Passager(nuPassager),
   avis varchar(50),
   estPositif BINARY_DOUBLE
);
Create Table Ville
(
    nomVille varchar(58)PRIMARY KEY
);

Create Table Vehicule
(
    matricule int PRIMARY KEY,
    type varchar(16),
    marque varchar(50),
    energie varchar(50),
    nbPlace int,
    dateMiseEnCirculation int,
    nuConducteur int,
    CONSTRAINT nuConducteur FOREIGN KEY (nuConducteur)
    REFERENCES Conducteur(nuConducteur)
);
Create Table Trajet
(
    idTrajet int PRIMARY KEY, 
    dateT varchar(16),
    villeDép varchar(50),
    CONSTRAINT villeDép FOREIGN KEY (villeDép)
    REFERENCES Ville(nomVille),
    villeArr varchar(50),
    CONSTRAINT villeArr FOREIGN KEY (villeArr)
    REFERENCES Ville(nomVille),
    HeureDep int,
    nuPassager int,
    longueur int,
    tarif int,
    utilisé int,
    CONSTRAINT utilisé FOREIGN KEY (utilisé)
    REFERENCES Vehicule(matricule)
)
```
il y a un erreur quelque part
# Version 2
```sql
CREATE TABLE UTILISATEUR (
	idUtilisateur int PRIMARY KEY
)
```