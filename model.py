from matplotlib import pyplot


class Model():

    def fit(self, data):
        raise NotImplementedError('Metodo non implementato')

    def predict(self, data):
        raise NotImplementedError('Metodo non implementato')


class IncrementModel(Model):

    def predict(self, data):
        prev_value = None
        mean = None
        somma = 0

        for i in range(len(data) - 1):
            if type(data[i + 1]) == "<class 'str'>":
                raise TypeError('Valore in lista non valido')
            somma += data[i + 1] - data[i]
        mean = somma / (len(data) - 1)

        prev_value = mean + data[len(data) - 1]
        return prev_value


class FitIncrementModel(IncrementModel):

    def fit(self, data):
        somma = 0
        for i in range(len(data) - 1):
            if type(data[i + 1]) == "<class 'str'>":
                raise TypeError('Valore in lista non valido')
            somma += data[i + 1] - data[i]
            self.global_avg_increment = somma / (len(data) - 1)

    def predict(self, data, fitdata):
        somma = 0
        mean = None
        for i in range(len(data) - 1):
            if type(data[i + 1]) == "<class 'str'>":
                raise TypeError('Valore in lista non valido')
            somma += data[i + 1] - data[i]
        mean = somma / (len(data) - 1)

        self.fit(fitdata)
        return (mean + self.global_avg_increment) / 2 + data[len(data) - 1]


dati_fit = [8, 19, 31, 41]
dati_n = [50, 52, 60]
n = 3
modello = IncrementModel()
prediction = modello.predict(dati_n)
print('predizione dati: ',prediction)

modello_fit = FitIncrementModel()
prediction_fit = modello_fit.predict(dati_n, dati_fit)
print('predizioni dati con fit: ',prediction_fit)

pyplot.plot(dati_fit + dati_n + [prediction], color='tab:red')
pyplot.plot(dati_fit + dati_n, color='tab:blue')
pyplot.show()

pyplot.plot(dati_fit + dati_n + [prediction_fit], color='tab:red')
pyplot.plot(dati_fit + dati_n, color='tab:blue')
pyplot.show()
