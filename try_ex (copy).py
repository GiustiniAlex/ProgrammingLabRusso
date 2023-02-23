class Errore(Exception):
    pass

class CSVFile():

    def  __init__(self, nome):
        self.nome = nome

    def __str__(self):
        return 'Io sono il file {}'.format(self.nome)

    def get_data(self, start=None, end=None):      
        try:
            my_file = open(self.nome, 'r')
        except:
            return 'Errore, il file non esiste'
            #raise Errore('Dio cane')
            
        if type(start) != "<class 'int'>" and type(end)!="<class 'int'>" and start != None and end!=None:
            try:
                start = int(start)
                end = int(end)
            except:
                start=None
                end=None
                start=1
                end=0
                for line in my_file:
                    end+=1
        else:
            start=1
            end=0
            for line in my_file:
                end+=1
        
        dati=[]
        i=1
        
        for line in my_file:
            print(line)
            splittata = line.split(',')
            if i >= start and i <= end:
                dati.append(splittata)
            i=+1
            
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