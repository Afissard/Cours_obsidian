# Exo 1
Soit la structure de données suivante : 
```
Fournisseur (#nofournisseurs, nom, ville)
Mafourniture (#nofournisseur, noproduit, quantité)
Produit (#noproduit, nom-produit, couleur, origine, PVU) 
```

Exprimez chacune des questions suivantes en algèbre relationnelle : 
1 ▶ Trouvez les numéros des fournisseurs qui fournissent quelque chose.
```R1 <- Mafourniture{nofounisseur}``` 
2 ▶ Trouvez les numéros des fournisseurs qui ne fournissent rien.
```R2 <- Diff(Fournisseur{nofournisseur}, MaFourniture{nofounisseur})```
3 ▶ Trouvez les numéros des fournisseurs qui fournissent au moins le produit P6.
```R3 <- MaFourniture[noproduit='P6']{nofournisseur}```
4 ▶ Trouvez les numéros des fournisseurs qui fournissent quelque chose d’autre que P6.
```
R4 <- Diff(Fournisseur{nofournisseur}, MaFourniture[noproduit = 'P6'{nofournisseur})
Autre solotion plus simple :
R4 <- MaFourniture[noproduit != 'P6']{nofournisseur}
```
5 ▶ Trouvez les numéros des fournisseurs qui fournissent quelque chose mais pas P6.
``` 
On peut utilisé les résultat précédant :
R5 <- Diff(R3, R1)
```
6 ▶ Trouvez les numéros des fournisseurs qui fournissent au moins un produit originaire de leur ville.
```
A <- Join(Fournisseur, Fourniture / Founisseur.nofournisseur = Mafourniture.nofournisseur)
B <- Join(A, Produit / A.produit = produit.noproduit AND A.ville = produit.origine)
R6 <- B{nofournisseur}
```
7 ▶ Trouvez les numéros des fournisseurs qui fournissent tous les produits originaires de Nantes 
```
R7 <- Div(MaFourniture{nofournisseur, noproduit}, Produit[origine = 'Nantes']{noproduit})
```
8 ▶ Trouvez les numéros des fournisseurs dont toutes les fournitures contiennent des produits verts.
```
R8 <- 
```
