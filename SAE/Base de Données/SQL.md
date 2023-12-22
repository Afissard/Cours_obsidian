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
-- Suppression des tables
DROP TABLE Avis;
DROP TABLE Trajet;
DROP TABLE Ville;
DROP TABLE Vehicule;
DROP TABLE Conducteur;
DROP TABLE Utilisateur;

-- Création des tables
CREATE TABLE Utilisateur (
	idUtilisateur INT PRIMARY KEY,
	nom VARCHAR(64),
	adresse VARCHAR(64), -- clé étrangère vers ville ?
	dateAgrement DATE,
);

-- Nécessaire ? Si un utilisateur possède une voiture (enregistré dans BD) => conducteur aussi ?
CREATE TABLE Conducteur (
		idConducteur INT PRIMARY KEY,
		-- idUtilisateur (clé étrangère) ?
		-- matricule (clé étrangère) ?
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

-- Insertion de donnée dans la base de donnée

-- Requètes
-- 1 : Liste des conducteurs qui effectuent des trajets entre Nantes et Cholet.

-- 2 : Trouvez pour chaque conducteur habitant Nantes et conduisant un véhicule immatriculé avant 2000, le type d’énergie utilisé par le véhicule (essence, diesel etc.)

-- 3 : Trouvez les conducteurs Nantais qui n’ont reçu que des avis positifs.

-- 4 : Quels sont les conducteurs qui ont parcouru le plus de trajet

-- 5 : Lister les trajets pour lesquels au moins un des passagers habite la ville d’arrivée

-- 6 : Lister les conducteurs qui ont reçu leur agrément après l’année 2014

-- 7 : Lister les conducteurs qui n’ont jamais transporté de passager

-- 8 : Trouver le conducteur qui a transporté le plus de passagers.

-- 9 : A créer

-- 10: A créer

```