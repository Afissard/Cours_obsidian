# Exo 1
## 1.1
1. cardinalité : 5 ligne
2. degré 4 colonne
3. clés de la relation : C, D sont les clés primaire de cette relation
4. Dépendance fonctionnelle A->B, A->C ? Oui pour A->B et non pour A->C.
# Exo 2
## 2.1
```
Fournisseur (#nofr, nom,ville) 
Fourniture(#nofr, #nopr, quantite) 
Produit(#nopr, nom, prix)
```
1. Clef étrangères appliqué : 
	- F-fournisseur : nofr -> nom, nofr -> ville
	- F-produit : nopr -> nom, nopr -> prix
	- F-fourniture : nofr & nopr-> quantité
	Raison application : 
	- nofr : parce qu'il faut que le fournisseur qui veut fournir soit enregistré dans la base de donnée
	- nopr : on veut que le produit soit dans le stock, un fournisseur ne peut fournir que les produit enregistré dans la base de donnée
## 2.2
```
Voiture(#noserie, modèle, marque, prix) 
Vendeur(#idvendeur, nom, tél) 
Vente(#idvendeur, #noserie, date, montant)
```
1. Clef étrangère appliqué : 
	- F-voiture : noserie -> modèle, noserie -> marque, noserie -> prix 
	- F-vendeur : idvendeur -> nom, idvendeur -> tel
	- F-vente : idvendeur & noserie -> date, idvendeur & noserie -> montant
	Raison application :
	- noserie : on veut que seules les voitures des série enregistré soit vendu
	- idvendeur : seul les vendeurs enregistré dans la base de donnée sont autorisé à vendre
1. Tuples de relation : (vendeur, voiture)
2. Exemple d'insertion de tuple 
	- incorrecte :
	- correcte :
