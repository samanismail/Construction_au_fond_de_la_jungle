from Grille import Grille
n=-1
m=-1
while n<0 or type(n) != int:
    n = int(input("Entrer le nombre de lignes: "))
while m<0 or type(m) != int:
    m = int(input("Entrer le nombre de colonnes: "))
grille = Grille(n, m)
grille.AfficherGrille()
grille.afficherChemin()
print("cout: " + str(grille.calculCout()))
print("Chemin: " + str(grille.chemin()))
