from sklearn.preprocessing import LabelEncoder
from sklearn.model_selection import train_test_split
import keras
from keras.models import Sequential
from keras.layers import Dense, Activation, Dropout
from keras.optimizers import SGD
from sklearn.metrics import mean_squared_error
from keras.layers import LSTM
from sklearn.metrics import mean_squared_error
import numpy as np
import pandas as pd


data = pd.read_csv('../data/DEPURACION_FINAL.csv', sep=',')

print('\n\nShape:',data.shape)

from datetime import datetime 
data_final = pd.DataFrame()
fechas_dt = []
kwh_dt = []
for registro in data.values:
    fecha = "{}-{}-{} {}".format(registro[0], registro[1], registro[3], registro[4])
    fecha_dt = datetime.strptime(fecha, '%Y-%m-%d %H')
    fechas_dt.append(fecha_dt)
    kwh_dt.append(registro[5])
#Creamos un nuevo dataframe con el formato de fecha correcto y el valor de KW-H
data_final['FECHA'] = fechas_dt
data_final['KW-H'] = kwh_dt

data_final.set_index('FECHA', drop=True, inplace = True)

size = int(0.18292*data_final.shape[0])
data_test = data_final[-size:]
data_train = data_final[:-size]

data_train['KW-H'] = [valor.replace(",", ".") for valor in data_train['KW-H'] ]
data_train['KW-H'] = [float(valor) for valor in data_train['KW-H'] ]

data_test['KW-H'] = [valor.replace(",", ".") for valor in data_test['KW-H'] ]
data_test['KW-H'] = [float(valor) for valor in data_test['KW-H'] ]


from sklearn.preprocessing import MinMaxScaler
sc = MinMaxScaler(feature_range = (0,1))
data_train_scaled = sc.fit_transform(data_train)

time_step = 60 
X_train = [] #Lista de conjuntos de 60 datos 
Y_train = []
m = len(data_train_scaled)
for i in range(time_step, m):
    X_train.append(data_train_scaled[i-time_step:i, 0]) #Guardamos 60 valores
    Y_train.append(data_train_scaled[i, 0]) #Buscamos predecir el dato time_step + 1, no la var KW
X_train, Y_train = np.array(X_train), np.array(Y_train) #Usamos np por reshape y optimizacion



X_train = np.reshape(X_train, (X_train.shape[0], X_train.shape[1], 1))



def NN_LSTM(optimizador, neuronas, epocas):
    #print('\nX sahep',X_train.shape)
    dim_entrada = (X_train.shape[1],X_train.shape[2])
    dim_salida = 1 
    num_neuronas = neuronas

    model = Sequential()
    #Primera capa LSTM con 1 neurona (Capa de entrada)
    #Segunda capa LSTM con num_neuronas (Capa oculta)
    model.add(LSTM(units=num_neuronas, return_sequences = True, input_shape=dim_entrada))
    #Esto no es una capa de neuronas, solo es una capa de congelamiento de neuronas 
    #congela el 40% de las neuronas para evitar overfitting
    model.add(Dropout(0.4))
    # Tercera capa LSTM con num_neuronas (Capa oculta)
    model.add(LSTM(units=num_neuronas))
    # model.add(Dropout(0.2))
    #Cuarta y ??ltima capa (no es LSTM) tiene una sola neurona de salida
    model.add(Dense(units = dim_salida))
    model.compile(optimizer= optimizador, loss='mse', metrics = ['mean_absolute_error']) #mean_squared_error

    #Entrenamiento 
    print('\nX sahepFit',X_train.shape)
    history = model.fit(X_train, Y_train, epochs = epocas, batch_size = 64)
    print('\nX sahepDespuesFit',X_train.shape)
    return model, history

def predecirFecha(fecha_inicio, fechaFin, model):
    time_step = 60
    #Se debe validar que fecha_inicio no sea menor a esta

    #Transforma texto a datetime
    fechaInicio_real =  str(data_train[-time_step:].index[0]) #2019-02-03 12:00:00
    fechaFin = datetime.strptime(fechaFin, "%Y-%m-%d %H:%M:%S")
    fechaInicio_real = datetime.strptime(fechaInicio_real, "%Y-%m-%d %H:%M:%S")
    fecha_inicio = datetime.strptime(fecha_inicio, "%Y-%m-%d %H:%M:%S")

    #Obtiene el n??mero de horas que existen entre el fin y le fecha inicio real
    diferencia = fechaFin - fechaInicio_real
    total_horas = diferencia.days*24 + diferencia.seconds/3600

    #Obtiene cual es la hora de inicio que debemos devolver 
    hora_inicio = fechaFin - fecha_inicio
    hora_inicio = hora_inicio.days*24 + hora_inicio.seconds/3600

    #Obtenemos los 60 primeros datos que nos ayudaran en la prediccion
    predic_final = []
    data_inicial = data_test[:time_step]
    data_inicial = sc.transform(data_inicial)
    data_resp = data_test[time_step:]
    data_resp = sc.transform(data_resp)

    #Iteramos hasta que tengamos la prediccion de todas las horas 
    pos =0

    for i in range(int(total_horas)):
      X_test = []
      X_test.append(data_inicial)
      X_test = np.array(X_test)
      X_test = np.reshape(X_test, (X_test.shape[0], X_test.shape[1], 1))
      X_test.shape #(totaldatos, time_step, 1) - (1, 60, 1)
      # data_inicial.shape
      predic = model.predict(X_test)
      predic_final.append(predic)

      #Buscamos reemplazar el ultimo valor de la data de entrada, pero  
      #esto debe hacerse a modo de PILA 

      #Eliminamos el primer elemento 
      data_inicial = data_inicial[1:]

      #Insertamos al final (ultimo) la prediccion en el arreglo
      data_inicial = np.append(data_inicial, data_resp[i%len(data_resp)])
      #print("Quedan {} horas por predecir... | Predicci??n actual {} | Data cambiada: {}".format(total_horas, predic, data_inicial[:]))
      print('Quedan por predecir',total_horas)
      total_horas = total_horas - 1
    # while(total_horas >0):
        
    predic_final = np.array(predic_final)
    predic_final = np.reshape(predic_final, (predic_final.shape[0], predic_final.shape[1]))
    predic_final = sc.inverse_transform(predic_final)
    #print("VALORES OBTENIDOS=========")
    #print(predic_final)
    return predic_final[-int(hora_inicio):] #Filtra que sean los valores de fecha_inicio