# Exo 2.1
## table employé
| Nuempl | Nomempl | hebdo | salaire | affect |
| ------ | ------- | ----- | ------- | ------ |
| 20     | Marcel  | 35    | 2000    | 3      |
| 23     | Claude  | 20    | 2500    | 3      |
| 37     | Michèle | 35    | 3000    | 3      |
| 39     | Léon    | 35    | 1900    | 1      |
| 41     | Jules   | 35    | 2800    | 1      |
| 30     | Edith   | 30    | 4000    | 4      |
| 17     | Sophie  | 35    | 2800    | 2      |
| 57     | Anne    | 35    | 1300    | 2      |
| 68     | Casimir | 20    | 3000    | 4      |
| 10     | Martin  | null  | 1000    | 4      |
## table service
| Nuserv | Nomserv      | Chef |
| ------ | ------------ | ---- |
| 1      | achat        | 41   |
| 2      | vente        | 17   |
| 3      | informatique | 23   |
| 4      | mécanique    | 20   | 
## table projet
| Nuproj | Nomproj | resp |
| ------ | ------- | ---- |
| 103    | Cobra   | 30   |
| 237    | Zorro   | 30   |
| 370    | Erasmus | 57   |
| 492    | Commet  | 20   |
| 135    | Eureka  | 57   |
| 160    | Esprit  | 5     |
## table travail
| Nuempl | Nuproj | Durée |
| ------ | ------ | ----- |
| 17     | 135    | 5     |
| 20     | 492    | 10    |
| 23     | 237    | 15    |
| 23     | 135    | 10    |
| 30     | 103    | 5     |
| 30     | 370    | 5     |
| 30     | 492    | 5     |
| 30     | 135    | 5     |
| 30     | 160    | 5     |
| 30     | 237    | 10    |
| 37     | 160    | 30    |
| 37     | 135    | 5     |
| 39     | 237    | 10    |
| 39     | 135    | 15    |
| 41     | 103    | 20    |
| 41     | 492    | 20    |
| 57     | 103    | 20    |
| 57     | 370    | 10    |
| 68     | 370    | 25    | 
## 1 : Employé {NUEMPL, NOMEMPL}
| Nuempl | Nomempl |
| ------ | ------- |
| 20     | Marcel  |
| 23     | Claude  |
| 37     | Michèle |
| 39     | Léon    |
| 41     | Jules   |
| 30     | Edith   |
| 17     | Sophie  |
| 57     | Anne    |
| 68     | Casimir |
| 10     | Martin  |
## 2 : Employé \[Salaire > 2000 \]
| Nuempl | Nomempl | salaire |
| ------ | ------- | ------- |
| 23     | Claude  | 2500    |
| 37     | Michèle | 3000    |
| 41     | Jules   | 2800    |
| 30     | Edith   | 4000    |
| 17     | Sophie  | 2800    |
| 68     | Casimir | 3000    |
## 3 : Union(Employé, Travail)
| Nuempl | Nomempl | Nuproj | Durée |
| ------ | ------- | ------ | ----- |
| 17     | Sophie  | 135    | 5     |
| 23     | Claude  | 237    | 15    |
| 23     | Claude  | 135    | 10    |
| 30     | Edith   | 103    | 5     |
| 30     | Edith   | 370    | 5     |
| 30     | Edith   | 492    | 5     |
| 30     | Edith   | 135    | 5     |
| 30     | Edith   | 160    | 5     |
| 30     | Edith   | 237    | 10    |
| 37     | Michèle | 160    | 30    |
| 37     | Michèle | 135    | 5     |
| 41     | Jules   | 103    | 20    |
| 41     | Jules   | 492    | 20    |
| 68     | Casimir | 370    | 25    |
## 4 : Inter(Employé {nuempl },Travail {nuempl })
| Nuempl |
| ------ |
| 17     |
| 23     |
| 23     |
| 30     |
| 30     |
| 30     |
| 30     |
| 30     |
| 30     |
| 37     |
| 37     |
| 41     |
| 41     |
| 68     |
## 5 : Diff(Employé {nuempl },Travail {nuempl })
| Nuempl |
| ------ |
| 10     |
## 6 : Div(Travail {nuempl, nuproj }, Projet {nuproj })
????
Résultat => nmpl : 30
# Exo 2
Soit la structure de données suivante : 
Fournisseur (nofournisseurs, nom, ville)
Mafourniture (nofournisseur, noproduit, quantité)
Produit (noproduit, nom-produit, couleur, origine, PVU) 

Exprimez chacune des questions suivantes en algèbre relationnelle : 
1 ▶ Trouvez les numéros des fournisseurs qui fournissent quelque chose ; 

2 ▶ Trouvez les numéros des fournisseurs qui ne fournissent rien ; 
3 ▶ Trouvez les numéros des fournisseurs qui fournissent au moins le produit P6 ; 
4 ▶ Trouvez les numéros des fournisseurs qui fournissent quelque chose d’autre que P6 ; 
5 ▶ Trouvez les numéros des fournisseurs qui fournissent quelque chose mais pas P6 ; 
6 ▶ Trouvez les numéros des fournisseurs qui fournissent au moins un produit originaire de leur ville ; 
7 ▶ Trouvez les numéros des fournisseurs qui fournissent tous les produits originaires de Nantes 
8 ▶ Trouvez les numéros des fournisseurs dont toutes les fournitures contiennent des produits verts
# 2.2
Soit la structure de données suivante : 
Personne (matricule, nom, sexe, âge, profession, revenu) 
Livre (no-livre, titre, auteur, thème, matricule-possesseur) 
Préférence(matricule,no-livre)

## 1 : Donnez les titres des livres possédés par la personne de matricule 99 2  

## 2 : Donnez le nom du possesseur du livre n° 36 3 
## 3 : Sélectionner les noms des personnes qui ont parmi leurs livres préférés au moins un livre du thème « science-fiction » 4 
## 4 : Sélectionner les matricules des personnes dont tous les livres sont du thème « policier » 5 
## 5 : Sélectionner les nom