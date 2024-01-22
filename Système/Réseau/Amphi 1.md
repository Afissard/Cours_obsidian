La ressource va principalement traiter des langages bas niveau (ASM) + étude d'un micro processeur / micro contrôle
Théorie des pointeurs

#TODO trouvé le gitlab avec les ressources du cours (le pdf de madoc n'est pas le même)

# Exécution d'un programme
Passage d'un langage haut niveau (Golang) à un langage bas niveau.
go build produit un fichier ELF 64bit exécutable LSB executable, x86-64 (jeu d'instruction pour certains processeurs)
Exécution du programme avec go build:
1. Compilation (langage haut niveau -> code objet)
	1. Analyse lexicale (vérifie l'ortographe des mots clef)
	2. Analyse de la syntaxe (vérifie si les ligne de commande sont bien écrite (exemple : est-ce que le *if* est bien ordonné))
	3. Analyse sémantique (vérifie si les ligne de commande font sens (si par exemple la variable est bien typé sur tout le code))
	4. Traduction en code intermédiaire (génère du code très similaire à de l'ASM mais pas dépendant de l'architecture du processeur, celui peut ensuite être transformé vers de l'ASM pour l'architecture voulue)
	5. Optimisation
	6. Génération du code objet  (= code machine sauf les appel à d'autre morceau de code, exemple appel à une fonction print de la lib stdio) (et ASM ?)
2. Edition des liens (code objets -> exécutable)
	1. Résolution des liens (appel de librairie externe)
	2. Optimisation
	3. Génération du code executable (visualisable avec par exemple xxd, ou un désassembleur : objdump)
Le langage machine (ASM) à deux representation (format texte et format binaire pour la machine)