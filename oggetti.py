class CSVFile():

    def  __init__(self, nome):
        self.nome = nome

    def __str__(self):
        return 'Io sono il file {}'.format(self.nome)

    def get_data(self):
        dati=[]
        my_file = open(self.nome, 'r')
        for line in my_file:
            splittata = line.split(', ')
            dati.append(splittata)
        return dati

primo_file = CSVFile('shampoo_sales.csv')
print(primo_file.get_data())