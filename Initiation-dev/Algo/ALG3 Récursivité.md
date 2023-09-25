Retour sur la recherche, exemple d'une fonction de recherche avec une fonction recursive
```go
// Voir #Madoc pour exemple écrit en go
```
Une fonction recursive est une fonction qui s'appelle elle même, ou via une chaine d'appel de fonction.
```go
func my_fn(i int){
	log.Print(i)
	i --
	if (i>0){
		my_func(i)
	} 
}
```
**Attention au boucle infini si un cas d'arret est oublié, la compilation ne seras pas possible ou causeras un bug à cause d'une dépassement de la mémoire alloué au programme.**
cours pas fidèle à au pdf de #Madoc 
L'appel d'une fonction est couteux en langage machine, parfois le compilateur peut de manière intelligente remplacer l'appel de la fonction par le code de la fonction (voir *Inlining*), or pour une fonction récursive ... (démonstration pour 3 appel de fonction)

La récursivité est une alternative, plus simple (mais dure à maitrisé) aux boucles.

Exemple de suite codé avec des fonction récursive