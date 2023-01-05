import random
import matplotlib.pyplot as plt

from Cellule import Cellule


class Grille:
    def __init__(self, lignes, colonnes):
        self.lignes = lignes
        self.colonnes = colonnes

        self.grille = self.creationGrille()

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

    def creationGrille(self):
        # epaisseurs[random.randint(0, 4)

        grille = []
        for i in range(self.lignes):
            matrice = []
            for j in range(self.colonnes):
                matrice.append(Cellule(0, 0, 0, 0))
            grille.append(matrice)
        epaisseurs = [5, 10, 15, 20, 25]
        for i in range(self.lignes):
            for j in range(self.colonnes):
                if i == 0:
                    grille[i][j].setHaut(epaisseurs[random.randint(0, 4)])
                else:
                    grille[i][j].setHaut(grille[i - 1][j].getBas())
                if j == 0:
                    grille[i][j].setGauche(epaisseurs[random.randint(0, 4)])
                else:
                    grille[i][j].setGauche(grille[i][j - 1].getDroit())

                grille[i][j].setDroit(epaisseurs[random.randint(0, 4)])
                grille[i][j].setBas(epaisseurs[random.randint(0, 4)])
                grille[i][j].setCentre(i, j)
        for i in range(self.lignes):
            for j in range(self.colonnes):
                print(grille[i][j])
        return grille

    def AfficherGrille(self):
        plt.figure()
        plt.axis('off')
        for i in range(self.lignes):
            for j in range(self.colonnes):
                plt.plot([j, j + 1], [i, i], color='blue', linewidth=self.grille[i][j].getHaut())
                plt.plot([j, j + 1], [i + 1, i + 1], color='red', linewidth=self.grille[i][j].getBas())
                plt.plot([j, j], [i, i + 1], color='yellow', linewidth=self.grille[i][j].getGauche())
                plt.plot([j + 1, j + 1], [i, i + 1], color='black', linewidth=self.grille[i][j].getDroit())
                plt.plot([j + 0.5, j + 0.5], [i + 0.5, i + 0.5], 'ro')

        plt.show()
