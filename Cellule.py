class Cellule:
    def __init__(self, gauche, haut, droit, bas):
        self.gauche = gauche
        self.haut = haut
        self.droit = droit
        self.bas = bas
        self.centre = (0, 0)

    def getGauche(self):
        return self.gauche

    def getHaut(self):
        return self.haut

    def getDroit(self):
        return self.droit

    def getBas(self):
        return self.bas

    def setGauche(self, gauche):
        self.gauche = gauche

    def setHaut(self, haut):
        self.haut = haut

    def setDroit(self, droit):
        self.droit = droit

    def setBas(self, bas):
        self.bas = bas

    def setCentre(self, i, j):
        self.centre = (i, j)

    def getCentre(self):
        return self.centre

    def __str__(self):
        return "Cellule: " + str(self.centre) + " " + str(self.gauche) + " " + str(self.haut) + " " + str(
            self.droit) + " " + str(self.bas)
