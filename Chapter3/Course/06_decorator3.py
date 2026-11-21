def outer(func):
    # inner affiche "Je vais dormir.", appelle func(), puis affiche "Je suis debout."
    def inner():
        print("Je vais dormir.")
        func()
        print("Je suis debout.")
    return inner

# Raccouri: On écrit @outer juste au dessus de la fonction.
# On appelle ça du <sucre syntaxique>
@outer
def sleep():
    import random
    import time
    print("Sleeping......")
    time.sleep(random.randint(1,5))

sleep()

# Un décorateur est une fermeture qui appelle la fonction cible à l'interieur.
# Il ajoute des fonnctionnalité sans modifier la fonction cible.

# Deux façons: fn = outer(sleep) ou @outer au-dessus de la fonction
