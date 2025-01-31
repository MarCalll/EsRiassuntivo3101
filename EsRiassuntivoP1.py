#



def creaAccount():
    nomeUtente=input("Inserire nuovo nome utente: ")
    password=input("Inserire password: ")
    return [nomeUtente,password,[],[],[]]

account=creaAccount()

def aggiungiNumero():
    numero=input("Inserire nuovo numero di telefono: ")
    account[2].append([numero])
    print(account)
    
aggiungiNumero()

def checkNomeUtente(nuovoNomeUtente):
    if account[0]==nuovoNomeUtente:
        return True
    else:
        

def modificaAccount():
    print("Cosa vuoi modificare?")
    print("1.Nome utente")
    print("2.Password")
    print("3.Numero di telefono")
    scelta=int(input())
    if scelta==1:
        nuovoNomeUtente=input("Inserisci nuovo nome utente ")
        checkNomeUtente(nuovoNomeUtente)