```sql
/*
// Récupération des table
CREATE TABLE employe as select * FROM basetd.employe
CREATE TABLE service as select * FROM basetd.service;
CREATE TABLE travail as select * FROM basetd.travail;
CREATE TABLE projet as select * FROM basetd.projet;
CREATE TABLE concerne as select * FROM basetd.concerne;
*/


// 1.1
// Question 1 : selection des employés qui travail sur tout les projets
SELECT nomempl FROM employe, travail WHERE employe.nuempl=travail.nuempl;

// Question 2 : Sélectionnez les noms des employés possédant les numéros suivants : 20,30 et 42
SELECT nomempl FROM employe WHERE nuempl IN (20, 30, 42);

// Question 3 : Sélectionnez les numéros des projets dont les noms commencent par la lettre ’C’
SELECT nuproj FROM projet WHERE nomproj LIKE 'c%';

// Question 4 : Sélectionnez les numéros des employés dont le temps hebdomadaire n’est pas renseigné.
SELECT nuempl FROM employe WHERE hebdo IS  NULL; // table vide ?!

// Question 5 : Sélectionnez les noms des employés avec la durée de travail sur les projets. Si un employé n’est pas impliqué dans un projet son nom doit sortir dans le résultat de la requête.
SELECT nomempl, duree FROM employe, travail WHERE employe.nuempl = travail.nuempl(+);

// Question 6 : Sélectionnez les numéros des projets sur lesquels travaille un employé.
SELECT nuproj, nuempl FROM travail;

// Question 7 : Sélectionnez les numéros des employés qui ne travaillent pas sur des projets
SELECT nuempl FROM employe MINUS SELECT nuempl FROM travail;

// 1.2
// Question 1 : Sélectionnez les numéros et noms de tous les employés dans la table Employé 
SELECT nuempl, nomempl FROM employe;

// Question 2 : Sélectionnez le nombre d’employés
SELECT COUNT(*) from employe;

// Question 3 : Sélectionnez le temps hebdomadaire moyen de travail des employés
SELECT AVG(hebdo) FROM employe;

// Question 4 : Sélectionnez la somme des durées consacrées par les employés aux projets
SELECT SUM(duree) FROM travail;

// Question 5 : Affichez les noms des employés par ordre croissant 
SELECT nomempl FROM employe ORDER BY nomempl ASC;

// Question 6 : Affichez les numéros des employés et la durée de travail consacrée par chacun des employés à chacun des projets. Les résultats doivent être triés par numéro employé (ordre décroissant)
SELECT nuempl, duree, nuproj FROM travail ORDER BY nuempl DESC;

// Question 7 : Affichez le nom du service numéro 1 
SELECT nomempl FROM service WHERE nuserv = 1;

// Question 8 : Affichez les noms des autres services
SELECT nomempl FROM service WHERE nuserv != 1;

// Question 9 : Affichez les noms des employés qui ne travaillent pas 
SELECT nomempl FROM employe WHERE NOT nuempl IN (SELECT nuempl FROM travail); // requete imbriquée mais existe plus simple
SELECT nomempl FROM employe MINUS SELECT nomempl FROM employe, travail WHERE employe.nuempl = travail.nuempl; // Solution "plus simple" ...

// Question 10 : Affichez les noms des employés dont le temps de travail hebdomadaire est compris entre 20 et 30 (deux versions)
SELECT nomempl FROM employe WHERE hebdo BETWEEN 20 and 30;
SELECT nomempl FROM employe WHERE hebdo >= 20 and hebdo <=30;
```
