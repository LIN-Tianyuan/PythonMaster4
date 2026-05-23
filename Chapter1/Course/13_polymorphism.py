class Animal:
    def speak(self):
        pass

class Dog(Animal):
    def speak(self):
        print("Woof woof woof")

class Cat(Animal):
    def speak(self):
        print("Miaou miaou miaou")

def make_noise(animal: Animal):
    animal.speak()

dog = Dog()
cat = Cat()

make_noise(dog)
make_noise(cat)

# Polymorphisme: états multiples
# lors de l'exécution d'un certain comportement,
# différents objets sont utilisés pour obtenir différent états.

# Même comportement, introduction d'objets différents, obtention d'état différents.

# classe abstraite: une classe contenant des méthodes abstraites est appelée classe abstraite.
# Méthode abstraite: une méthode dont le corps est une implémentation vide (pass) est appelée methode abstraite.