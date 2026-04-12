class Student:
    name = None
    age = None
    tel = None

    # Methode de construction
    # Elle est automatiquement exécuté lors de la création d'un objet de classe
    # Les arguments entrants sont automatiquement tranmis à la méthode
    # __init__ pour être utilisés lors de la création d'un objet de classe
    def __init__(self, name, age, tel):
        self.name = name
        self.age = age
        self.tel = tel
        print("La classe Etudiant crée un objet.")

stu_1 = Student("Alex", 18, "110")
print(stu_1.name)
stu_2 = Student("Luna", 20, "120")
print(stu_2.name)