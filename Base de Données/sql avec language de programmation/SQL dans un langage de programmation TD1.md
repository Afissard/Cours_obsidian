---
sujets: 
type:
  - TD
lien sujet: "[[sujet]]"
---
# SQL dans un langage de programmation TD1
*prise de note*
identifiant pour l'année : `s3a02b`
PDF du TD : [[TD1.pdf]]
## Réponse du TD
#TODO ajouter une intégration du code
### Question 1
**Table des contraintes**

| nom table | nom contrainte | type de contrainte | différer ou non |
| --------- | -------------- | ------------------ | --------------- |
| Employe   | PK_employe     | Clé primaire       | non             |
| Service   | PK_service     | Clé primaire       | non             |
| Projet    | PK_projet      | Clé primaire       | non             |
| Employe   | FK_employe     | Clé étrangère      | non             |

**Table de tests des contraintes**

| nom table  | requête                                                                                      | code d'erreur | message d'erreur            |
| ---------- | -------------------------------------------------------------------------------------------- | ------------- | --------------------------- |
| PK_employe | `--insertion d'un employé qui existe déjà`<br>`Insert into employe values(20,'toto',35,1) ;` | '-0001'       | Vilolation de la contrainte |
|            |                                                                                              |               |                             |
