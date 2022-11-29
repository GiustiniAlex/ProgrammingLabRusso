def continua():
    return((lista['x1y1'] == lista['x2y1'] and lista['x2y1'] == lista['x3y1'] and lista['x3y1'] != '/') or (lista['x1y2'] == lista['x2y2'] and lista['x2y2'] == lista['x3y2'] and lista['x3y2'] != '/') or(lista['x1y3'] == lista['x2y3'] and lista['x2y3'] == lista['x3y3'] and lista['x3y3'] != '/') or(lista['x1y1'] == lista['x1y2'] and lista['x1y2'] == lista['x1y3'] and lista['x1y3'] != '/') or(lista['x2y1'] == lista['x2y2'] and lista['x2y2'] == lista['x2y3'] and lista['x2y3'] != '/') or(lista['x3y1'] == lista['x3y2'] and lista['x3y2'] == lista['x3y3'] and lista['x3y3'] != '/') or(lista['x1y1'] == lista['x2y2'] and lista['x2y2'] == lista['x3y3'] and lista['x3y3'] != '/') or(lista['x3y1'] == lista['x2y2'] and lista['x2y2'] == lista['x1y3'] and lista['x1y3'] != '/'))

def NessunVincitore():
    return(not(continua()) and lista['x1y1'] != '/' and lista['x1y2'] != '/'and lista['x2y1'] != '/'and lista['x2y2'] != '/'and lista['x2y3'] != '/'and lista['x3y1'] != '/'and lista['x3y2'] != '/'and lista['x3y3'] != '/' and lista['x1y3']!='/')
        #not(continua()) and lista['x1y1'] != '/' and lista['x1y2'] != '/'and lista['x2y1'] != '/'and lista['x2y2'] != '/'and lista['x2y3'] != '/'and lista['x3y1'] != '/'and lista['x3y2'] != '/'and lista['x3y3'] != '/'

def controllo(c):
    return('x1y3'==c or 'x2y3'==c or 'x3y3'==c or 'x1y2'==c or 'x2y2'==c or 'x3y2'==c or 'x1y1'==c or 'x2y1'==c or 'x3y1'==c)


           
tria="\n y3  {} | {} | {}\n    -----------\n y2  {} | {} | {}\n    -----------\n y1  {} | {} | {}\n     x1  x2  x3 "

lista = {'x1y3':'/', 'x2y3':'/','x3y3':'/','x1y2':'/','x2y2':'/','x3y2':'/','x1y1':'/','x2y1':'/','x3y1':'/'}

Segni=['X', 'O']
giocatori = {'1':'X', '2':'O'}

giocatoreI = input('Giocatore 1 scegli X o O: ')
mossa='x1x1'

if giocatoreI==Segni[0] or giocatoreI=='x' : 
    print('Giocatore 2 sarà O')
    i=0
else:
    print('Giocatore 2 sarà X')
    giocatori = {'1':'O', '2':'X'}
    i=1


print('\nIniziamo!')

print(tria.format(lista['x1y3'], lista['x2y3'], lista['x3y3'], lista['x1y2'], lista['x2y2'], lista['x3y2'], lista['x1y1'], lista['x2y1'], lista['x3y1']));

while not(continua()) :
    
    while not(controllo(mossa) and lista[mossa]!=Segni[0] and lista[mossa]!=Segni[1]) :
        mossa = input('\nGiocatore, fai la tua mossa: ') 
        if(not(controllo(mossa)) or lista[mossa]==Segni[0] or lista[mossa]==Segni[1]):
            print('\nMossa non valida! riprova')
            
    lista[mossa]=Segni[i]

    print(tria.format(lista['x1y3'], lista['x2y3'], lista['x3y3'], lista['x1y2'], lista['x2y2'], lista['x3y2'], lista['x1y1'], lista['x2y1'], lista['x3y1']));
    
    if(i==0): 
        i=1
    else:
        i=0

    mossa='non valida'

    if NessunVincitore():
        break

if NessunVincitore():
    print('Non ce nessun vincitore! :(')
else:
    if giocatori['1']==Segni[i] :
        print('\nGiocatore 2 è il VINCITORE!!!')
    else:
        print('\nGiocatore 1 è il VINCITORE!!!')

