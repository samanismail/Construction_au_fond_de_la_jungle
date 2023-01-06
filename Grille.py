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
        return grille

    def AfficherGrille(self):
        plt.figure()
        plt.axis('off')
        plt.title("Grille initiale")
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
        compteur = 0
        for i in range(self.lignes * self.colonnes):
            L = []
            if compteur == 0:
                L.append((i + 1, self.grille[compteur // self.colonnes][compteur % self.colonnes].getDroit()))
                L.append((i + self.colonnes, self.grille[compteur // self.colonnes][compteur % self.colonnes].getBas()))
            elif compteur == self.colonnes - 1:
                L.append((i - 1, self.grille[compteur // self.colonnes][compteur % self.colonnes].getGauche()))
                L.append((i + self.colonnes, self.grille[compteur // self.colonnes][compteur % self.colonnes].getBas()))
            elif compteur == self.lignes * self.colonnes - self.colonnes:
                L.append(
                    (i - self.colonnes, self.grille[compteur // self.colonnes][compteur % self.colonnes].getHaut()))
                L.append((i + 1, self.grille[compteur // self.colonnes][compteur % self.colonnes].getDroit()))
            elif compteur == self.lignes * self.colonnes - 1:
                L.append(
                    (i - self.colonnes, self.grille[compteur // self.colonnes][compteur % self.colonnes].getHaut()))
                L.append((i - 1, self.grille[compteur // self.colonnes][compteur % self.colonnes].getGauche()))
            elif compteur < self.colonnes:
                L.append((i - 1, self.grille[compteur // self.colonnes][compteur % self.colonnes].getGauche()))
                L.append((i + 1, self.grille[compteur // self.colonnes][compteur % self.colonnes].getDroit()))
                L.append((i + self.colonnes, self.grille[compteur // self.colonnes][compteur % self.colonnes].getBas()))
            elif compteur % self.colonnes == 0:
                L.append(
                    (i - self.colonnes, self.grille[compteur // self.colonnes][compteur % self.colonnes].getHaut()))
                L.append((i + 1, self.grille[compteur // self.colonnes][compteur % self.colonnes].getDroit()))
                L.append((i + self.colonnes, self.grille[compteur // self.colonnes][compteur % self.colonnes].getBas()))
            elif compteur % self.colonnes == self.colonnes - 1:
                L.append(
                    (i - self.colonnes, self.grille[compteur // self.colonnes][compteur % self.colonnes].getHaut()))
                L.append((i - 1, self.grille[compteur // self.colonnes][compteur % self.colonnes].getGauche()))
                L.append((i + self.colonnes, self.grille[compteur // self.colonnes][compteur % self.colonnes].getBas()))
            elif compteur > self.lignes * self.colonnes - self.colonnes:
                L.append(
                    (i - self.colonnes, self.grille[compteur // self.colonnes][compteur % self.colonnes].getHaut()))
                L.append((i - 1, self.grille[compteur // self.colonnes][compteur % self.colonnes].getGauche()))
                L.append((i + 1, self.grille[compteur // self.colonnes][compteur % self.colonnes].getDroit()))
            else:
                L.append(
                    (i - self.colonnes, self.grille[compteur // self.colonnes][compteur % self.colonnes].getHaut()))
                L.append((i - 1, self.grille[compteur // self.colonnes][compteur % self.colonnes].getGauche()))
                L.append((i + 1, self.grille[compteur // self.colonnes][compteur % self.colonnes].getDroit()))
                L.append((i + self.colonnes, self.grille[compteur // self.colonnes][compteur % self.colonnes].getBas()))

            dico[i] = L
            compteur += 1
        return dico

    def dijkstra_pred(self):
        G = self.creationDictionnaire()
        s = 0
        D = {}  # tableau final des distances minimales
        d = {k: float('inf') for k in G}  # distances initiales infinies
        d[s] = 0  # sommet de départ
        P = {}  # liste des prédécesseurs
        while len(d) > 0:  # fin quand d est vide
            k = self.minimum(d)  # sommet de distance minimale pour démarrer une étape
            for i in range(len(G[k])):  # on parcourt les voisins de k
                v, c = G[k][i]  # v voisin de k, c la distance à k
                if v not in D:  # si v n'a pas été déjà traité
                    if d[v] > d[k] + c:  # est-ce plus court en passant par k ?
                        d[v] = d[k] + c
                        P[v] = k  # stockage du prédécesseur de v
            D[k] = d[k]  # copie du sommet et de la distance dans D
            del (d[k])  # suppression du sommet de d
        return D, P  # on retourne aussi la liste des prédécesseurs

    def minimum(self, dico):
        i = -1
        m = float('inf')
        for k in dico:  # parcours des clés
            if dico[k] < m:
                m = dico[k]
                i = k
        return i

    def chemin(self):
        D, P = self.dijkstra_pred()
        i = self.lignes * self.colonnes - 1
        chemin = [(i // self.colonnes, i % self.colonnes)]
        while i in P:
            i = P[i]
            chemin.append((i // self.colonnes, i % self.colonnes))
        chemin.reverse()
        return chemin

    def afficherChemin(self):
        plt.axis("off")
        plt.title("Grille percéé")
        chemin = self.chemin()
        plt.plot([0, 0], [0.5, 0], color='brown', linewidth=10)
        plt.plot([self.lignes - 1, self.lignes - 1], [-self.lignes + 1, -self.lignes + 0.5], color='brown',
                 linewidth=10)
        for i in range(len(chemin) - 1):
            plt.plot([chemin[i][1], chemin[i + 1][1]], [-chemin[i][0], -chemin[i + 1][0]], color='brown', linewidth=10)
        # percer des murs afin d'obtenir le chemin voulu.
        for i in range(len(chemin) - 1):
            # cellule gauche haut
            if i == 0:
                self.grille[0][0].setHaut(0)
            # cellule doite bas
            if i == len(chemin) - 2:
                self.grille[self.lignes - 1][self.colonnes - 1].setBas(0)
            if chemin[i][0] == chemin[i + 1][0]:
                if chemin[i][1] < chemin[i + 1][1]:
                    self.grille[chemin[i][0]][chemin[i][1]].setDroit(0)
                    self.grille[chemin[i + 1][0]][chemin[i + 1][1]].setGauche(0)
                else:
                    self.grille[chemin[i][0]][chemin[i][1]].setGauche(0)
                    self.grille[chemin[i + 1][0]][chemin[i + 1][1]].setDroit(0)
            else:
                if chemin[i][0] < chemin[i + 1][0]:
                    self.grille[chemin[i][0]][chemin[i][1]].setBas(0)
                    self.grille[chemin[i + 1][0]][chemin[i + 1][1]].setHaut(0)
                else:
                    self.grille[chemin[i][0]][chemin[i][1]].setHaut(0)
                    self.grille[chemin[i + 1][0]][chemin[i + 1][1]].setBas(0)
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

    def calculCout(self):
        D, P = self.dijkstra_pred()
        return D[self.lignes * self.colonnes - 1]
