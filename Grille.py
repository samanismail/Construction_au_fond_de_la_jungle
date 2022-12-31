import random
import matplotlib.pyplot as plt
import numpy as np

from Cellule import Cellule


class Grille:
    def __init__(self, lignes, colonnes):
        self.lignes = lignes
        self.colonnes = colonnes
        g = [[Cellule(0, 0, 0, 0) for x in range(colonnes)] for y in range(lignes)]

        for i in range(lignes):
            for j in range(colonnes):
                if j - 1 >= 0 and i == 0:
                    g[i][j] = Cellule(0, random.randint(1, 5), random.randint(1, 5),
                                      random.randint(1, 5))
                elif i - 1 >= 0 and j == 0:
                    g[i][j] = Cellule(random.randint(1, 5), 0, random.randint(1, 5),
                                      random.randint(1, 5))
                elif i - 1 >= 0 and j - 1 >= 0:
                    g[i][j] = Cellule(0, 0, random.randint(1, 5),
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

    def AfficherGrille(self):
        compteur = 0
        fig, axes = plt.subplots(nrows=self.lignes, ncols=self.colonnes)
        for row in axes:
            for ax in row:
                ax.set_axis_off()
                x1, y1 = [0, 0], [0, 1]
                x2, y2 = [0, 1], [1, 1]
                x3, y3 = [1, 1], [0, 1]
                x4, y4 = [0, 1], [0, 0]
                ax.plot(x1, y1, color='lightblue',
                        linewidth=self.grille[compteur // self.colonnes][compteur % self.colonnes].getGauche()*10)
                ax.plot(x2, y2, color='lightblue',
                        linewidth=self.grille[compteur // self.colonnes][compteur % self.colonnes].getHaut()*10)
                ax.plot(x3, y3, color='lightblue',
                        linewidth=self.grille[compteur // self.colonnes][compteur % self.colonnes].getDroit()*10)
                ax.plot(x4, y4, color='lightblue',
                        linewidth=self.grille[compteur // self.colonnes][compteur % self.colonnes].getBas()*10)
                compteur += 1

        fig.tight_layout(pad=0)
        plt.show()

    def __str__(self):
        s = ""
        for i in range(self.lignes):
            for j in range(self.colonnes):
                s += "   "+str(self.grille[i][j].getHaut()) + "\n"+str(self.grille[i][j].getGauche()) + "      " + str(self.grille[i][j].getDroit()) + "\n" +"   "+ str(self.grille[i][j].getBas()) + "\n"
        return s
