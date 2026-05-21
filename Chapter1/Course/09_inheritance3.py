class Phone:
    serial_number = None
    producer = "HUAWEI"

    def call_by_5g(self):
        print("5g calls.")

class NFCReader:
    nfc_type = "Fifth Generation"
    producer = "HM"

    def read_card(self):
        print("Read NFC cards.")

    def write_card(self):
        print("Write NFC cards.")

class RemoteControl:
    rc_type = "IR remote control"

    def control(self):
        print("Infrared remote control opening.")

# Les classes pères multiples dont les membres portent le même nom sont prioritaires
# par défaut dans l'ordre de l'héritage (de gauche à droite)
class MyPhone(NFCReader, Phone, RemoteControl):
    pass

my_phone = MyPhone()
my_phone.call_by_5g()
my_phone.control()
print(my_phone.producer)

