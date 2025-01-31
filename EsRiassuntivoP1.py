#



def creaAccount():
    nomeUtente=input("Inserire nuovo nome utente: ")
    password=input("Inserire password: ")
    return [nomeUtente,password]

account=creaAccount()

def aggiungiNumero():
    numero=input("Inserire nuovo numero di telefono: ")
    account.append(numero)
    print(account)
    
aggiungiNumero()