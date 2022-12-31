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
                    g[i][j] = Cellule(g[i][j - 1].getDroit(), random.randint(1, 5), random.randint(1, 5),
                                      random.randint(1, 5))
                elif i - 1 >= 0 and j == 0:
                    g[i][j] = Cellule(random.randint(1, 5), g[i - 1][j].getBas(), random.randint(1, 5),
                                      random.randint(1, 5))
                elif i - 1 >= 0 and j - 1 >= 0:
                    g[i][j] = Cellule(g[i][j - 1].getDroit(), g[i - 1][j].getBas(), random.randint(1, 5),
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
        """s = ""
        for i in range(self.lignes):
            for j in range(self.colonnes):
                s += "   "+str(self.grille[i][j].getHaut()) + "\n"+str(self.grille[i][j].getGauche()) + "      " + str(self.grille[i][j].getDroit()) + "\n" +"   "+ str(self.grille[i][j].getBas()) + "\n"
        return s"""
        """compteur = 0
        fig, ax = plt.subplots(self.lignes, self.colonnes)
        while compteur < self.lignes * self.colonnes:
            x1, y1 = [0, 0], [0, 2]
            x2, y2 = [0, 2], [2, 2]
            x3, y3 = [2, 2], [0, 2]
            x4, y4 = [0, 2], [0, 0]
            ax[compteur].plot(x1, y1, color='black', linewidth=20)
            ax[compteur].plot(x2, y2, color='red', linewidth=10)
            ax[compteur].plot(x3, y3, color='green', linewidth=10)
            ax[compteur].plot(x4, y4, color='blue', linewidth=10)
            compteur += 1

        fig.tight_layout(pad=-1)
        plt.axis('off')
        plt.show()"""
        compteur = 0
        fig, axes = plt.subplots(nrows=self.lignes, ncols=self.colonnes ,figsize=(100, 100))
        for row in axes:
            for ax in row:
                ax.set_axis_off()
                ax.set_facecolor('white')
                x1, y1 = [0, 0], [0, 2]
                x2, y2 = [0, 2], [2, 2]
                x3, y3 = [2, 2], [0, 2]
                x4, y4 = [0, 2], [0, 0]
                ax.plot(x1, y1, color='lightblue', linewidth=self.grille[compteur // self.colonnes][compteur % self.colonnes].getGauche()*10)
                ax.plot(x2, y2, color='lightblue', linewidth=self.grille[compteur // self.colonnes][compteur % self.colonnes].getHaut()*10)
                ax.plot(x3, y3, color='lightblue', linewidth=self.grille[compteur // self.colonnes][compteur % self.colonnes].getDroit()*10)
                ax.plot(x4, y4, color='lightblue', linewidth=self.grille[compteur // self.colonnes][compteur % self.colonnes].getBas()*10)
                compteur += 1

        fig.tight_layout(pad=-0.5)
        plt.show()
