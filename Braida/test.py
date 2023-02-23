

my_file = open('shampoo_sales.txt', 'r')


dati=[]
riga = my_file.split('\n')
for line in range(5):
    print(riga[line])
