package chocolats

import ("math")

/*
Une marque de barres de chocolat fait une promotion~: si on retourne k embalages 
on en obtient une gratuite. On se demande alors combien de barres de chocolat on 
peut obtenir quand on dispose de n euros et que chacune coûte m euros.
La fonction miam doit répondre (de manière récursive) à cette question.

# Entrées
- n : la somme dont on dispose en euros
- m : le prix d'une barre de chocolat en euros, toujours supérieur à 0
- k : le nombre d'embalages qu'il faut pour obtenir une barre de chocolat gratuite, toujours supérieur à 1

# Sortie
- choco : le nombre de barre de chocolat qu'on peut obtenir en tout

# Exemple
*/
func miam(n, m, k uint) (choco uint) {
	if n >= m { // tant que achat possible
		choco += uint(math.Floor(float64(n/m)))
		n -= m*choco
		choco += miam(n,m,k)
	} 
	// calcule barre bonus
	choco += bonus(choco, k)
	return choco
}

func bonus(choco, k uint)(newChoco uint) {
	if choco >= k {
		sup := uint(math.Floor(float64(choco/k)))
		newChoco += sup
		newChoco += bonus(sup + (choco%k), k)
	}
	return newChoco
}