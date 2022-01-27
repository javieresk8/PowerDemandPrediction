import pandas as pd
from datetime import datetime, timedelta

def obtenerDatosDemandaIntervalo(fechaInicio:str, fechaFin:str):
    data = pd.read_csv('../data/data_total.csv',skiprows=0,index_col=None,usecols=[0,1,2,4,5,6]) 
    print(data)
    datosInicio = fechaInicio.split('-')
    datosFin = fechaFin.split('-')
    for i in range(len(datosInicio)):
        datosInicio[i] = int(datosInicio[i])
        datosFin[i] = int(datosFin[i])
    print(datosInicio)
    print(datosFin)
    print(data.info())
    data = data[
        data.index[(data['AÑO']==datosInicio[0]) & (data['MES']==datosInicio[1]) & (data['FECHA']==datosInicio[2]) & (data['HORA']==datosInicio[3])].to_list()[0]:
        data.index[(data['AÑO']==datosFin[0]) & (data['MES']==datosFin[1]) & (data['FECHA']==datosFin[2]) & (data['HORA']==datosFin[3])].to_list()[0]
        ]
    return data


def obtenerTodosDatos():
    data = pd.read_csv('../data/data_total.csv',skiprows=0,index_col=None,usecols=[0,1,2,4,5,6])
    #print(data)
    return data

def generarIntervaloFecha(fechaInicio, fechaFin):
    fechaInicio = datetime.strptime(fechaInicio, "%Y-%m-%d %H:%M:%S")
    fechaFin = datetime.strptime(fechaFin, "%Y-%m-%d %H:%M:%S")
    diferencia = fechaFin - fechaInicio
    print(diferencia.days)
    print(diferencia.seconds)
    total = diferencia.days*24 +diferencia.seconds/3600
    total
    fechas = []
    fecha_temp = fechaInicio
    for _ in range(int(total)):
        fechas.append(str(fecha_temp))
        fecha_temp = fecha_temp +timedelta(hours=1)
    #     print(fechaInicio)
    #fechas.append(str(fechaFin))
    return fechas

obtenerTodosDatos()