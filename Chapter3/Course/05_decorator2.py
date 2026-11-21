# outer reçoit une fonction: func, la fonction à décorer.
def outer(func):
    # inner affiche "Je vais dormir.", appelle func(), puis affiche "Je suis debout."
    def inner():
        print("Je vais dormir.")
        func()
        print("Je suis debout.")
    return inner

def sleep():
    import random
    import time
    print("Sleeping......")
    time.sleep(random.randint(1,5))

fn = outer(sleep)
fn()