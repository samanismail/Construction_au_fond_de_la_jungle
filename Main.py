from Grille import Grille

n = input("Lignes : ")
m = input("Colonnes : ")
if n.isdigit() and m.isdigit():
    grille = Grille(int(n), int(m))
    print("Cout: " + str(grille.calculCout()))
    grille.AfficherGrille()
    grille.afficherChemin()
    print("Chemin: " + str(grille.chemin()))
else:
    print("Veuillez entrer des nombres")
    exit()
