import pandas as pd
from urllib3 import Retry
def obtenerDatosDemandaIntervalo():
    data = pd.read_csv('../data/data_total_dattime.csv')
    print(data)

#obtenerDatosDemandaIntervalo()

def obtenerTodosDatos():
    data = pd.read_csv('../data/data_total.csv',skiprows=0,index_col=None,usecols=[0,1,2,4,5,6])
    #print(data)
    return data

obtenerTodosDatos()