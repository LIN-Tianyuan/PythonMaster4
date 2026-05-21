class Phone:
    serial_number = None
    producer = 'HUAWEI'

    def call_by_5g(self):
        print("Father 5g calls.")

class MyPhone(Phone):
    # Override
    producer = "APPLE"

    def call_by_5g(self):
        print("Child 5g calls.")

my_phone = MyPhone()
print(my_phone.producer)
my_phone.call_by_5g()