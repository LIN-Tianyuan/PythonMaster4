class AC:
    def cool_wind(self):
        """Réfrigération"""
        pass

    def hot_wind(self):
        """Chaleur"""
        pass

    def swing_l_r(self):
        """Le vent souffle à droite et à gauche"""
        pass

class Midea_AC(AC):
    def cool_wind(self):
        print("Climatisation et refroidissement par Midea.")

    def hot_wind(self):
        print("Chauffage par Midea.")

    def swing_l_r(self):
        print("Les climatiseurs Midea se balacent de gauche à droite.")

class GREE_AC(AC):
    def cool_wind(self):
        print("Climatisation et refroidissement par GREE.")

    def hot_wind(self):
        print("Chauffage par GREE.")

    def swing_l_r(self):
        print("Les climatiseurs GREE se balacent de gauche à droite.")

def make_cool(ac: AC):
    ac.cool_wind()

midea_ac = Midea_AC()
gree_ac = GREE_AC()

make_cool(midea_ac)
make_cool(gree_ac)