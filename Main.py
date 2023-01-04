from Grille import Grille


grille = Grille(3, 3)
print(grille.AfficherGrille())
print(grille)



print(grille.parcoursEnProfondeur(grille.getGrille()))
