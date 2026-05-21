class Phone:
    serial_number = None
    producer = None

    def call_by_4g(self):
        print("4g calls.")

class Phone2026(Phone):
    face_id = True

    def call_by_5g(self):
        print("2026 lastest 5g calls.")

phone2026 = Phone2026()
phone2026.call_by_4g()
phone2026.call_by_5g()
phone2026.serial_number = "2026-001"
print(phone2026.serial_number)
