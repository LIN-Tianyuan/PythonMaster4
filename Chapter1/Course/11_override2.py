class Phone:
    serial_number = None
    producer = "HUAWEI"

    def call_by_5g(self):
        print("5g calls.")


class MyPhone(Phone):
    producer = "Apple"

    def call_by_5g(self):
        # La première façon d'appeler un membre de la classe père
        print(f"La marque de la classe est: {self.producer}.")
        print(f"La marque de la classe père est: {Phone.producer}.")
        Phone.call_by_5g(self)

        print("----------")
        # La deuxième façon d'appeler un membre de la classe père
        print(f"La marque de la classe père est: {super().producer}.")
        super().call_by_5g()

my_phone = MyPhone()
my_phone.call_by_5g()

# Override: Redéfinir une variable ou une méthode membre d'une classe père
