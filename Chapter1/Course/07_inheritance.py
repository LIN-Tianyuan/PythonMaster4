class Phone:
    serial_number = None
    producer = None

    def call_by_4g(self):
        print("4g calls.")

class Phone2026:
    serial_number = None
    producer = None
    face_id = True

    def call_by_4g(self):
        print("4g calls.")

    def call_by_5g(self):
        print("2026 latest 5g calls.")

phone2026 = Phone2026()
phone2026.call_by_5g()
phone2026.call_by_4g()