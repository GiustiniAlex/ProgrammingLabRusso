class ExamException(Exception):
    pass

class CSVFile():

    def  __init__(self, name):
        self.name = name

    def get_data(self):      
        try:
            my_file = open(self.name, 'r')
        except Exception:
            raise ExamException("Errore, il file non esiste")

        dati=[]
        
        for line in my_file:
            splittata = line.split(',')   
            splittata[-1] = splittata[-1].strip()
            if splittata[0] != 'date':
                dati.append(splittata)
        my_file.close()
        
        return dati        


class CSVTimeSeriesFile(CSVFile):

    def get_data(self):
        dati = super().get_data()
        time_series = []

        try:
            for i in range(len(dati)):
                anno_mese = dati[i][0].split('-')
                if len(anno_mese) < 2:
                    del dati[i]
        except:
            pass

        anno_precedente = 0
        mese_precedente = 0
        data_precedente = ''
        
        # Controlliamo timestamp fuori ordine o duplicati
        for data in dati:
            anno, mese = data[0].split('-')
            anno_corrente = int(anno)
            mese_corrente = int(mese)
            data_corrente = data[0]
            
            if anno_precedente > anno_corrente:
                raise ExamException("Errore, serie temporale non ordinata!")

            if mese_precedente > mese_corrente and mese_precedente != 12:
                raise ExamException("Errore, serie temporale non ordinata!")

            if data_corrente == data_precedente:
                raise ExamException("Errore, serie temporale duplicata!")
            
            anno_precedente = anno_corrente
            mese_precedente = mese_corrente
            data_precedente = data_corrente

         # Controlliamo i passeggeri
        for sel in dati:
            if len(sel) > 1 and sel[1] != '' and sel[1] != None and int(sel[1]) > 0:
                sel[1] = int(sel[1]) 
                time_series.append(sel)
            else:
                prov = [sel[0], 100000]
                time_series.append(prov)

        print(time_series)
        return time_series




def detect_similar_monthly_variations(time_series, years):
    if time_series == None:
        raise ExamException("Errore, serie temporale non valida")
        
    trovato0 = False
    trovato1 = False
    for sel in time_series:
        if years[0] == int(sel[0].split('-')[0]):
            trovato0 = True
        if years[1] == int(sel[0].split('-')[0]):
            trovato1 = True
    if not(trovato0) or not(trovato1):
        raise ExamException('Errore, le date non sono presenti nella serie temporale')

    pass_anno0 = [0 for x in range(12)]
    pass_anno1 = [0 for x in range(12)]
    diff_anno0 = []
    diff_anno1 = []
    risultati = []
    index1 = 0
    index0 = 0


    for mese in range(12):
        for sel in time_series:
            if int(sel[0].split('-')[0]) == years[0] and int(sel[0].split('-')[1]) == mese+1:
                pass_anno0[mese] = sel[1]


    for mese in range(12):
        for sel in time_series:
            if int(sel[0].split('-')[0]) == years[1] and int(sel[0].split('-')[1]) == mese+1:
                pass_anno1[mese] = sel[1]
    
    

    for i in range(11):
        diff_anno0.append(abs(pass_anno0[i+1] - pass_anno0[i]))
        diff_anno1.append(abs(pass_anno1[i+1] - pass_anno1[i]))

    for i in range(11):
        print(diff_anno0[i]-diff_anno1[i])
        risultati.append(diff_anno0[i]-diff_anno1[i] >= -2 and diff_anno0[i]-diff_anno1[i] <=2)

    print(pass_anno0)
    print(pass_anno1)
    return risultati


time_series_file = CSVTimeSeriesFile(name='data.csv')
time_series = time_series_file.get_data()
print(detect_similar_monthly_variations(time_series, [1949, 1950]))