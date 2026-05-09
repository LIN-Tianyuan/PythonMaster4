class Phone:
    # Variables membres publiques
    serial_number = None
    producer = None

    # Variables membres privées
    __current_voltage = None

    def call_by_5g(self):
        # Les méthodes privées ne peuvent pas être utilisées directement par les objets de la classe,
        # mais peuvent être utilisées par les méthodes publiques de la classe.
        if self.__current_voltage >= 1:
            self.__keep_single_core()
            print("Les appels 5g sont désormais possible.")
        else:
            print("Défaut d'appel, batterie faible.")

    # Méthodes membres privées
    def __keep_single_core(self):
        print("Faire fonctionner l'unité centrale en mode mono-coeur pour économiser de l'énergie.")

phone = Phone()
phone.serial_number = "123"
# Les méthodes privées ne peuvent pas être utilisées directement par les objets de la classe.
phone.__keep_single_core()

