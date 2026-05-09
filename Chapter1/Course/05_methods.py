class Student:
    name = None
    age = None

    def __init__(self, name, age):
        self.name = name
        self.age = age

    # Les adresses mémoire ne sont pas très utiles, et nous pouvons
    # contrôler le comportement des conversions de classes en chaînes de caractères
    # en utilisant la méthode __str__.
    def __str__(self):
        return f"name = {self.name}, age = {self.age}"

    # less than
    def __lt__(self, other):
        return self.age < other.age

    # less than or equal
    def __le__(self, other):
        return self.age <= other.age

    # equal
    def __eq__(self, other):
        return self.age == other.age

student1 = Student("Alex", 18)
student2 = Student("Hebe", 20)
student3 = Student("Hebe", 20)
print(student1)
print(student1 > student2)
print(student2 <= student3)
print(student2 == student3)
