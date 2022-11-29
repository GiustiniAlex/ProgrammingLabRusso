import random
import os
os.system("clear")

def controllo():
    for i in range(dim):
        for j in range(dim):
            if campo[i][j] != piano[i][j] and campo[i][j] != 'X':
                return False
    return True

dim=100
while dim<4 or dim>9:
    dim = int(input('Inserisci la dimensione del campo (da 4 a 9): '))
print('')
coordinate='4 100'
def espansione(i, j):
    if j-1>-1 and campo[i][j-1]!='X' and piano[i][j-1] !=0 and campo[i][j]==0:
        piano[i][j-1] = campo[i][j-1]
        espansione(i, j-1)
    if j+1<dim and campo[i][j+1]!='X' and piano[i][j+1] !=0 and campo[i][j]==0:
        piano[i][j+1] = campo[i][j+1]
        espansione(i, j+1)
    if i-1>-1 and campo[i-1][j]!='X' and piano[i-1][j] !=0 and campo[i][j]==0:
        piano[i-1][j] = campo[i-1][j]
        espansione(i-1, j)
    if i+1<dim and campo[i+1][j]!='X' and piano[i+1][j] !=0 and campo[i][j]==0:
        piano[i+1][j] = campo[i+1][j]
        espansione(i+1, j)
   

perc_bombe=20
campo=[[i for i in range(dim)] for y in range(dim)]

for i in range(dim):
    for j in range(dim):
        if random.randint(0, 100) < perc_bombe:
            campo[i][j] = 'X'
        else:
            campo[i][j] = 0
"""
for i in range(dim):
    for j in range(dim):
        print(campo[i][j], end='')
    print('')
print('') """

for i in range(dim):
    for j in range(dim):
        if campo[i][j] == 0:
            num=0
            if j-1>-1 and campo[i][j-1]=='X':
                num+=1
            if j+1<dim and campo[i][j+1]=='X':
                num+=1
            if i-1>-1 and campo[i-1][j]=='X':
                num+=1
            if i+1<dim and campo[i+1][j]=='X':
                num+=1
            if i-1>-1 and j-1>-1 and campo[i-1][j-1]=='X':
                num+=1
            if i-1>-1 and j+1<dim and campo[i-1][j+1]=='X':
                num+=1
            if i+1<dim and j-1>-1 and campo[i+1][j-1]=='X':
                num+=1
            if i+1<dim and j+1<dim and campo[i+1][j+1]=='X':
                num+=1
            campo[i][j]=num
            
"""
for i in range(dim):          #stampa del campo X 0 1
    for j in range(dim):
        print(campo[i][j], end='')
    print('') """

piano=[['#' for i in range(dim)] for y in range(dim)]

for i in range(dim):           #stampa del piano #
    print(i, end='| ')
    for j in range(dim):
        print(piano[i][j], end=' ')
    print('')
print('   ', end='')
for i in range(dim):
    print('_', end=' ')
print('')
print('   ', end='')
for i in range(dim):
    print(i, end=' ')
print('\n')


while True:  
    while int(coordinate.split()[0]) > dim or int(coordinate.split()[1]) > dim:
        coordinate = input('Dimmi la coordinata "x y [f]": ')
        while len(coordinate)<3:
            coordinate = input('Dimmi la coordinata "x y [f]": ')
    os.system("clear")
    cella = coordinate
    cella = cella.split()
    cella[0] = int(cella[0])
    cella[1] = int(cella[1])
    print('')
    #print(campo[cella[1]][cella[0]])
    if len(cella)>2 and piano[cella[1]][cella[0]] != 'F':
        piano[cella[1]][cella[0]] = 'F'
    elif len(cella)>2:
        piano[cella[1]][cella[0]] = '#'
    else:
        piano[cella[1]][cella[0]] = campo[cella[1]][cella[0]]

    if campo[cella[1]][cella[0]] == 0 and len(cella)<3:
        espansione(cella[1], cella[0])

    if controllo():
        break
    for i in range(dim):           #stampa del piano #
        print(i, end='| ')
        for j in range(dim):
            print(piano[i][j], end=' ')
        print('')
    print('   ', end='')
    for i in range(dim):
        print('_', end=' ')
    print('')
    print('   ', end='')
    for i in range(dim):
        print(i, end=' ')
    print('\n')
    coordinate='3 100'
    if campo[cella[1]][cella[0]] == 'X' and len(cella)<3:
        break

if campo[cella[1]][cella[0]] == 'X' and len(cella)<3:
    print('BOMBAA - HAI PERSO!')
else:
    for i in range(dim):           #stampa del campo completo #
        print(i, end='| ')
        for j in range(dim):
            print(campo[i][j], end=' ')
        print('')
    print('   ', end='')
    for i in range(dim):
        print('_', end=' ')
    print('')
    print('   ', end='')
    for i in range(dim):
        print(i, end=' ')
    print('\n\nHAI VINTO !')