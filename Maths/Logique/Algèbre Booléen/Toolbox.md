#IMPORTANT : résumé des notions algébrique vu en cours de maths discrètes.
# Logique, [[Algèbre Booléen]] :
- A<=>B = (A=>B).(B=>A)
- -(A + B) = -A . -B
- -(A . B) = -A + -B
- **A => B = -A + B**
- -(-A) = A
- **A . (B + C) = (A . B) + A . C)**
- **A + (B . C) = (A + B) . (A + C)**
- A . A = A
- A + A = A
- A . -A = FALSE
- A + -A = TRUE
- A . TRUE = A
- A . FALSE = FALSE
- A + TRUE = TRUE
- A + FALSE = A
- A + B = B + A
- A . B = B . A
- (A + B) + C = A + (B + C)
- (A . B) . C = A . (B . C)
# Prédicats [[Prédicat définition]]:
- Négation :
	- -(∀x, F(x)) = ∃x, -F(x)
	- -(∃x, F(x)) = ∀x, -F(x) 
- Elimination :
	- ∀x, (∀y, F(y)) = ∀y, F(y) si x n'apparait pas dans F
	- ∃x, (∃y, F(y)) = ∃y, F(y) si x n'apparait pas dans F
- Permutation (Uniquement pour les même quantificateurs, sinon cela change le sens de la proposition) :
	- ∀x, ∀y, F = ∀y, ∀x, F
	- ∃x, ∃y, F = ∃y, ∃x, F
- Distribution :
	- ∀x, (F(x) . G(x)) = (∀x, F(x)) . (∀x, G(x)) : ∀ est distribuable sur AND.
	- ∃x, (F(x) + G(x)) = (∃x, F(x)) + (∃x, G(x)) : ∃ est distribuable sur OR.
- Changement de portée :
	- ∀x(F(x) . G) = (∀x, F(x)) . G : si x n'apparaît pas dans G
	- ∀x(F(x) + G) = (∀x, F(x)) + G : si x n'apparaît pas dans G
	- ∃x(F(x) . G) = (∃x, F(x)) . G : si x n'apparaît pas dans G
	- ∃x(F(x) + G) = (∃x, F(x)) + G : si x n'apparaît pas dans G