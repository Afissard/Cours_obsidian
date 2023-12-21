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
DROP TABLE Avis;
DROP TABLE Trajet;
DROP TABLE Ville;
DROP TABLE Vehicule;
DROP TABLE Conducteur;
DROP TABLE Utilisateur;

CREATE TABLE Utilisateur (
	idUtilisateur INT PRIMARY KEY,
	nom VARCHAR(64),
	adresse VARCHAR(64),
	dateAgrement DATE,
);

-- Nécessaire ? Si un utilisateur possède une voiture (enregistré dans BD) => conducteur aussi ?
CREATE TABLE Conducteur (
		idConducteur INT PRIMARY KEY,
);

CREATE TABLE Vehicule (
    matricule INT PRIMARY KEY,
    type VARCHAR(64),
    marque VARCHAR(64),
    energie VARCHAR(64),
    nbPlace INT,
    dateMiseEnCirculation DATE,
    idConducteur INT,
    CONSTRAINT idConducteur FOREIGN KEY (idConducteur)
    REFERENCES Conducteur(idConducteur),
);

CREATE TABLE Ville (
	nomVille VARCHAR(64)PRIMARY KEY
);

CREATE TABLE Trajet (
	idTrajet INT PRIMARY KEY, 
    dateT DATE,
    villeDép VARCHAR(64),
    CONSTRAINT villeDép FOREIGN KEY (villeDép)
    REFERENCES Ville(nomVille),
    villeArr VARCHAR(64),
    CONSTRAINT villeArr FOREIGN KEY (villeArr)
    REFERENCES Ville(nomVille),
    HeureDep INT,
    nuPassager INT,
    longueur INT,
    tarif INT,
    vehicule INT,
    CONSTRAINT vehicule FOREIGN KEY (vehicule)
    REFERENCES Vehicule(matricule)
);

CREATE TABLE Avis (
	idUtilisateur INT,
	CONSTRAINT idUtilisateur FOREIGN KEY (idUtilisateur)
    REFERENCES Utilisateur(idUtilisateur),
    avis BOOL,
    idTrajet INT,
	CONSTRAINT idTrajet FOREIGN KEY (idTrajet)
    REFERENCES Trajet(idTrajet),
);
```