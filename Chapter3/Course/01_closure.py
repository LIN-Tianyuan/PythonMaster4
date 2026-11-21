"""
account_amount = 0  # Solde du compte

def atm(num, deposit=True):
    global account_amount
    if deposit:
        account_amount += num
        print(f"Dépôt: +{num}, solde du compte : {account_amount}")
    else:
        account_amount -= num
        print(f"Retrait: -{num}, solde du compte : {account_amount}")

atm(300)
atm(300)
atm(100, False)
"""

# Une fermeture, c'est trois conditions:
# 1. fonction dans une autre fonction
# 2. la fonction interne utilise une variable de la fonction externe
# 3. la fonction externe renvoie la fonction interne

# initial_amount est le solde.
def account_create(initial_amount = 0):
    def atm(num, deposit=True):
        nonlocal initial_amount
        if deposit:
            initial_amount += num
            print(f"Dépôt: +{num}, solde du compte : {initial_amount}")
        else:
            initial_amount -= num
            print(f"Retrait: -{num}, solde du compte : {initial_amount}")
    return atm

# fn est la fonction atm
fn = account_create()
fn(300)
fn(300)
fn(100, False)





