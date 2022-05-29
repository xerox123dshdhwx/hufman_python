class ArbreBinaire:
    def __init__(self, valeur):
        self.valeur = valeur
        self.bit = 0
        self.enfant_gauche = None
        self.enfant_droit = None

    def insert_gauche(self, valeur):
        if self.enfant_gauche == None:
            self.enfant_gauche = (valeur)

    def insert_droit(self, valeur):
        if self.enfant_droit == None:
            self.enfant_droit = (valeur)

    def get_valeur(self):
        return self.valeur

    def get_gauche(self):
        return self.enfant_gauche

    def get_droit(self):
        return self.enfant_droit

    def get_bit(self):
        return self.bit
