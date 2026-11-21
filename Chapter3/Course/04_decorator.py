# Un décorateur est en fait une fermeture
# Il ajoute une fonctionnalité à une fonction cible, sans modifier son code.

# La fonction sleep: elle dort entre 1 et 5 secondes.
"""
def sleep():
    import random
    import time
    print("Sleeping......")
    time.sleep(random.randint(1,5))
"""

# Nouvelle demande:
# avant de dormir, afficher "Je vais dormir."
# après, afficher "Je suis debout."
def sleep():
    import random
    import time
    print("Je vais dormir.")
    print("Sleeping......")
    time.sleep(random.randint(1,5))
    print("Je suis debout.")

sleep()