package main

import "fmt"

type Alien struct {
	Nom     string
	Sexe    string
	Planete string
	Cellule int
}

var Aliens []Alien
var Roswell []Alien
var Roswell_dict = make(map[int]Alien) // Only have Alien in jail

func Create_alien(number int, n string, s string, p string, jail bool) {
	/* Create an Alien and add it to the global dict : Aliens and Roswell */
	var c = 0
	cells++
	if jail {
		c = cells
		Roswell = append(Roswell, Alien{Nom: n, Sexe: s, Planete: p, Cellule: c})
		Roswell[cells] = Roswell[len(Roswell)-1]
	}
	Aliens = append(Aliens, Alien{Nom: n, Sexe: s, Planete: p, Cellule: c})
	//fmt.Println(Aliens[len(Aliens)-1])
}

var cells int = 0
var NOMS = []string{"Albert", "Bob", "Caesar", "Cody"}
var PLANETE = []string{"TERRE", "MARS", "JUPITER"}
var SEXES = []string{"MALE", "FEMELLE", "AUTRES"}

func Init_all() {
	/*Initialise toutes les combinaisons possible*/
	count := 0
	in_jail := false
	for i := 0; i < len(NOMS); i++ {
		for j := 0; j < len(SEXES); j++ {
			for k := 0; k < len(PLANETE); k++ {
				for l := 0; l < 2; l++ {
					count++
					if l == 0 {
						in_jail = false
					} else {
						in_jail = true
					}
					Create_alien(count, NOMS[i], SEXES[j], PLANETE[k], in_jail)
				}
			}
		}
	}
	/*
		for i := 0; i < len(Aliens); i++ {
			fmt.Println(Aliens[i])
		}
	*/
}

func ensemble_planete() {
	/*Question 1*/
	var ensemble_P = []string{}
	for x := 0; x < len(Roswell); x++ {
		add_pla := true
		for i := 0; i < len(ensemble_P); i++ {
			if (ensemble_P[i] != Roswell[x].Planete) && add_pla {
				add_pla = true
			} else {
				add_pla = false
			}
		}
		if add_pla {
			ensemble_P = append(ensemble_P, Roswell[x].Planete)
		}
	}
	fmt.Println("Ensemble des planètes des prisoniers", ensemble_P)
}

func ensemble_cellules_vide() {
	var ensemble_nonC = []int{}
	for x := 0; x < cells; x++ {
		if _, is_taken := Roswell_dict[x]; !is_taken {
			ensemble_nonC = append(ensemble_nonC, x)
		}
	}
	fmt.Println("Enssemble des cellues vides :", ensemble_nonC)
}

func main() {
	Init_all()
	//ensemble_planete()
	ensemble_cellules_vide()
}
