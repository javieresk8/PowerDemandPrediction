from logging import root
from tkinter import Canvas, Tk,Frame ,LAST, ttk
from math import cos, sin, radians, pi
import random
from typing import Text

from tkinter import PhotoImage
from PIL import Image,ImageTk

global colorBlanco
colorBlanco = '#F7F7F7'
 
class Modelos: 

    def __init__(self,modelo, optimizador):
        self.modelo = modelo
        self.optimizardor = optimizador

def center(win): 
    """ centers a tkinter window :param win: the main window or Toplevel window to center """ 
    win.update_idletasks() 
    width = win.winfo_width() 
    frm_width = win.winfo_rootx() - win.winfo_x() 
    win_width = width + 2 * frm_width 
    height = win.winfo_height() 
    titlebar_height = win.winfo_rooty() - win.winfo_y() 
    win_height = height + titlebar_height + frm_width 
    x = win.winfo_screenwidth() // 2 - win_width // 2 
    y = win.winfo_screenheight() // 2 - win_height // 2 
    win.geometry('{}x{}+{}+{}'.format(width, height, x, y)) 
    win.deiconify()

# Permite cargar cualquier imagen a la interfaz, se especifica el nombre del archivo
# tamaño deseado que tenga y la ubicación dentro de la ventana
def cargarImg(root, file, size: tuple, place: tuple):
    img=Image.open(file)
    img=img.resize(size,Image.ANTIALIAS)
    img.save(file)
    img=PhotoImage(master=root,file=file)
    panel=ttk.Label(root,image=img)
    panel.image = img
    panel.place(x=place[0],y=place[1])
    

def mainInterfaz():

    # Cracción Root y configuraciones iniciales
    ventana = Tk()
    ancho_ventana = 950
    alto_ventana = 600
    posicion = str(ancho_ventana) + "x" + str(alto_ventana)
    ventana.geometry(posicion)
    ventana.resizable(0,0)
    ventana.minsize(width=ancho_ventana, height=alto_ventana)
    ventana.title('Predicción Demanda')
    ventana.config(bg=colorBlanco)
    center(ventana)

    #Frame -> Contenedor
    frame = Frame(ventana, width = ancho_ventana,  height=alto_ventana, bg= colorBlanco, relief ='sunken')
    frame.grid(column=0,row=0)

    # Encabezado 
    cargarImg(ventana, 'logo1.png',(100,100),(30,20))
    cargarImg(ventana, 'logo2.png',(100,100),(800,20))

    label1 = ttk.Label(frame, text="UNIVERSIDAD TÉCNICA DE COTOPAXI", background=colorBlanco, font=("Courie",14,'bold'))
    label1.place(x=280, y=30)

    label2 = ttk.Label(frame, text="INGENIERÍA ELÉCTRICA", background=colorBlanco, font=("Courie",14,'bold'))
    label2.place(x=350, y=70)

    # Canvas Parqueaderos
    #canvasParqueadero = Canvas(frame, bg= '#50A3D3', width = 300, height =320, bd =0, highlightthickness=2, highlightbackground="white")
    #canvasParqueadero.place(x=30,y=50)

    # Canvas Controles
    #canvasInfo = Canvas(frame, bg= '#50A3D3', width = 150, height =400, bd =0, highlightthickness=2, highlightbackground="white")
    #canvasInfo.place(x=550,y=50)

    #combo = ttk.Combobox(state="readonly", values=['COM 0','COM 1'])
    #combo.place(x=560,y=110)

    #label0 = ttk.Label(frame,width=22,text='ZigBee Communication Port', background='#50A3D3', font=("Courie",8))
    #label0.place(x=560, y=80)

    #labelSalida = ttk.Label(frame,width=22,text='', background='white', font=("Courie",8))
    #labelSalida.place(x=560, y=160)

    #labelBault1 = ttk.Label(frame,width=8,text='', background='white', font=("Courie",8))
    #labelBault1.place(x=620, y=190)

    #labelBault2 = ttk.Label(frame,width=8,text='Bault', background='#50A3D3', font=("Courie",8))
    #labelBault2.place(x=560, y=190)
                   
  

    ventana.mainloop()

mainInterfaz()