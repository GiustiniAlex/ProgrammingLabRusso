def sum_csv(File):
    file=open(File, 'r')
    somma=[]

    for line in file:
        elementi=line.split(',')

        if elementi[1]!='Sales\n':
            somma.append(float(elementi[1]))
    return sum(somma)
            
sommaSales=sum_csv('shampoo_sales.txt')
print(sommaSales)