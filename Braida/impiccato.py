
import getpass
import os

patibolo = '______________\n             |\n             |'
testa=   '            /|\ \n            \|/ '
spalle=  '            _|_  '
braccia1='           / | \  '
braccia2='          |  |  |  '
busto=   '            _|_   '
gamba=   '            | |   '
piedi=   '           _| |_   \n'

disegno=[patibolo, testa, spalle, braccia1, braccia2, busto, gamba, piedi]

indicePatibolo=1

parola=getpass.getpass('\nInserisci la parola segreta: ')
parola=parola.upper()
completare=[]
completoVerifica=[]

for i in parola:
    completare.append(i)
    completoVerifica.append(i)

    
for i in range(len(parola)):
    if i != 0 and i != len(parola)-1 and completare[i] != ' ':
        completare[i]='_'


while completare!=completoVerifica and indicePatibolo!=8:
    
    os.system("clear")
    for item in range(indicePatibolo):
        print(disegno[item])

    if indicePatibolo==7:
        print('\nATTENZIONE! Non puoi più sbagliare', end=' ')
    
    print('\n')
    for i in completare:
        print(i, end=" ")
    trovato=False
    lettera=input('\n\nInserire lettera da cercare: ')
    if lettera.upper() == parola:
        break
    lettera=lettera.upper()

    for i in range(len(parola)):
        if parola[i] == lettera:
            completare[i]=lettera
            trovato=True

    if not(trovato):
        indicePatibolo+=1

    
        
if indicePatibolo==8:
    for item in range(indicePatibolo):
        print(disegno[item])
    print('HAI PERSO!\n')
else:
    print('\n')
    for i in completare:
        print(i, end=" ")
    print('\n\nHAI VINTO!\n')