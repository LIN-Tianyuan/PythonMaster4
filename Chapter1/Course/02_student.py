# class
class Student:
    # propriétés(attributs) : variables
    name = None
    age = None

    # comportement : méthodes
    # self est utilisé pour désigner l'objet de la classe lui-même
    def say_hi(self):
        print(f"Bonjour à tous, je m'appelle {self.name} et j'ai {self.age} ans.")

    # self est transparent lorsque l'argument est passé et peut être ignoré
    def say_hi2(self, msg):
        print(f"Bonjour à tous, {msg}.")

# objet = nom de la classe()
stu_1 = Student()
stu_1.name = "Alex"
stu_1.age = 18
stu_1.say_hi()

stu_2 = Student()
stu_2.name = "Lucie"
stu_2.age = 16
stu_2.say_hi()
stu_2.say_hi2("enchanté de vous rencontrer.")