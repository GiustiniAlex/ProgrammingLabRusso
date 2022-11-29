def sum_list(list):
    somma=0
    if len(list) == 0:
        somma=None
  
    for item in list:
        somma = somma + item
    return somma


lista = [1, 2, 3, 4, 5]

risultato = sum_list(lista)
print(risultato)