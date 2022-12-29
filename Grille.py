import random

from Cellule import Cellule


class Grille:
    def __init__(self, lignes, colonnes):
        self.lignes = lignes
        self.colonnes = colonnes
        g = [[Cellule(0, 0, 0, 0) for x in range(colonnes)] for y in range(lignes)]

        for i in range(lignes):
            for j in range(colonnes):
                if j-1 >= 0 and i == 0:
                    g[i][j] = Cellule(g[i][j-1].getDroit(), random.randint(1, 5), random.randint(1, 5),
                                      random.randint(1, 5))
                elif i-1 >= 0 and j == 0:
                    g[i][j] = Cellule(random.randint(1, 5), g[i-1][j].getBas(), random.randint(1, 5),
                                      random.randint(1, 5))
                elif i-1 >= 0 and j-1 >= 0:
                    g[i][j] = Cellule(g[i][j-1].getDroit(), g[i-1][j].getBas(), random.randint(1, 5),
                                      random.randint(1, 5))
                else:
                    g[i][j] = Cellule(random.randint(1, 5), random.randint(1, 5), random.randint(1, 5),
                                      random.randint(1, 5))

        self.grille = g

    def getLignes(self):
        return self.lignes

    def getColonnes(self):
        return self.colonnes

    def getGrille(self):
        return self.grille

    def setLignes(self, lignes):
        self.lignes = lignes

    def setColonnes(self, colonnes):
        self.colonnes = colonnes

    def setGrille(self, grille):
        self.grille = grille

    def __str__(self):
        s = ""
        for i in range(self.lignes):
            for j in range(self.colonnes):
                s += "   "+str(self.grille[i][j].getHaut()) + "\n"+str(self.grille[i][j].getGauche()) + "      " + str(self.grille[i][j].getDroit()) + "\n" +"   "+ str(self.grille[i][j].getBas()) + "\n"
        return s