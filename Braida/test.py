import os
os.system("clear") #replit e su LINUX / ("cls") per WINDOWS

dati=[]
my_file = open('lista_invitati.txt', 'r')
for line in my_file:
    splittata = line.split(' ')
    dati.append(splittata)
print(dati)

