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
        for i in range(len(self.grille)):
            for element in self.grille[i]:
                ordonne, abscisse = -element.getCentre()[0], element.getCentre()[1]
                if not element.getGauche() == 0:
                    plt.plot([abscisse - 0.5, abscisse - 0.5], [ordonne - 0.5, ordonne + 0.5], color='aqua',
                             linewidth=element.getGauche())
                if not element.getHaut() == 0:
                    plt.plot([abscisse - 0.5, abscisse + 0.5], [ordonne + 0.5, ordonne + 0.5], color='aqua',
                             linewidth=element.getHaut())
                if not element.getDroit() == 0:
                    plt.plot([abscisse + 0.5, abscisse + 0.5], [ordonne - 0.5, ordonne + 0.5], color='aqua',
                             linewidth=element.getDroit())
                if not element.getBas() == 0:
                    plt.plot([abscisse - 0.5, abscisse + 0.5], [ordonne - 0.5, ordonne - 0.5], color='aqua',
                             linewidth=element.getBas())
        plt.show()

    def creationDictionnaire(self):
        dico = {}
        for i in range(self.lignes):
            for j in range(self.colonnes):
                L=[]
                if i == j == 0:
                    L.append([(i, j + 1), self.grille[i][j].getDroit()])
                    L.append([(i + 1, j), self.grille[i][j].getBas()])
                elif i == 0 and j == self.colonnes - 1:
                    L.append([(i, j - 1), self.grille[i][j].getGauche()])
                    L.append([(i + 1, j), self.grille[i][j].getBas()])
                elif i == self.lignes - 1 and j == 0:
                    L.append([(i, j + 1), self.grille[i][j].getDroit()])
                    L.append([(i - 1, j), self.grille[i][j].getHaut()])
                elif i == self.lignes - 1 and j == self.colonnes - 1:
                    L.append([(i, j - 1), self.grille[i][j].getGauche()])
                    L.append([(i - 1, j), self.grille[i][j].getHaut()])
                elif i == 0 and 1 < j < self.colonnes - 2:
                    L.append([(i, j + 1), self.grille[i][j].getDroit()])
                    L.append([(i, j - 1), self.grille[i][j].getGauche()])
                    L.append([(i + 1, j), self.grille[i][j].getBas()])
                elif i == self.lignes - 1 and 1 < j < self.colonnes - 2:
                    L.append([(i, j + 1), self.grille[i][j].getDroit()])
                    L.append([(i, j - 1), self.grille[i][j].getGauche()])
                    L.append([(i - 1, j), self.grille[i][j].getHaut()])
                elif j == 0 and 1 < i < self.lignes - 2:
                    L.append([(i + 1, j), self.grille[i][j].getBas()])
                    L.append([(i - 1, j), self.grille[i][j].getHaut()])
                    L.append([(i, j + 1), self.grille[i][j].getDroit()])
                elif j == self.colonnes - 1 and 1 < i < self.lignes - 2:
                    L.append([(i + 1, j), self.grille[i][j].getBas()])
                    L.append([(i - 1, j), self.grille[i][j].getHaut()])
                    L.append([(i, j - 1), self.grille[i][j].getGauche()])
                else:
                    L.append([(i + 1, j), self.grille[i][j].getBas()])
                    L.append([(i - 1, j), self.grille[i][j].getHaut()])
                    L.append([(i, j + 1), self.grille[i][j].getDroit()])
                    L.append([(i, j - 1), self.grille[i][j].getGauche()])
                dico[(i, j)] = L

        return dico
