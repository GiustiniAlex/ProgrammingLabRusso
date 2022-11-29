class CSVFile():

    def  __init__(self, nome):
        self.nome = nome
            
    def __str__(self):
        return 'Io sono il file {}'.format(self.nome)

    def get_data(self):
        dati=[]
        try:
            my_file = open(self.nome, 'r')
        except:
            return 'Errore, il file non esiste'
            
        for line in my_file:
            splittata = line.split(',')
            dati.append(splittata)
        return dati

class NumericalCSVFile(CSVFile):
    def  __init__(self, nome):
        self.nome = nome

    def tutto_float(self):
        dati = super().get_data()

        try:
            for i in dati:
                for j in range(len(i)):
                    if i[j] != 'Sales\n' and j!=0:
                        i[j] = float(i[j])
        except ValueError as e:
            print('Errore {}'.format(e))
            return None
        return dati
        

primo_file = NumericalCSVFile('shampoo_sales.txt')
print(primo_file.tutto_float())