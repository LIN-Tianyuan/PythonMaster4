def outer(num1):
    def inner(num2):
        # Pour modifier une variable de la fonction externe
        # depuis la fonction interne, il faut d'abord
        # la déclarer avec le mot-clé nonlocal.
        nonlocal num1
        num1 += num2
        print(num1)
    return inner

fn = outer(10)
fn(10)
fn(10)

# global: pour une variable globale
# nonlocal: pour une variable de la fonction externe.