from logging import root
from tkinter import GROOVE, SUNKEN,Canvas, StringVar, Tk,Frame , ttk, Button, Radiobutton
from math import cos, sin, radians, pi
import random
from turtle import pos
from typing import Text

from tkinter import PhotoImage
from PIL import Image,ImageTk


# Colores
global colorBlanco
colorBlanco = '#F7F7F7'
global colorNegro
colorNegro = '#090909'
global colorAzul
colorAzul = '#0853B3'
global colorCeleste
colorCeleste = '#D7DEF5'
global colorAmarilloClaro
colorAmarilloClaro = '#EBFF91'
global colorVerdeClaro
colorVerdeClaro = '#C4FFB2'

#Dimensiones
global ancho_ventana
ancho_ventana = 950
global alto_ventana
alto_ventana = 650
global heightSubFrames
heightSubFrames = 450

#Posiciones
global posicionFrames
posicionFrames = (0,200)


 
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

    

class Interfaz:

    def __init__(self):
        #self.ventana = Tk()
        #self.dibujar()
        
        self.frameDatosHistoricos = None       
        self.frameEntrenamientoRed = None
        self.framePrediccion = None
        self.dibujar()
       

    def nada(self):
        pass

    def mostrarFrameDatosHistoricos(self):
        self.ocultarOtrosFrames();
        self.frameDatosHistoricos.place(x=posicionFrames[0], y=posicionFrames[1])

    def mostrarFrameEntrenamiento(self):
        self.ocultarOtrosFrames();
        self.frameEntrenamientoRed.place(x=posicionFrames[0], y=posicionFrames[1]) 

    
    def mostrarFramePrediccion(self):
        self.ocultarOtrosFrames();
        self.framePrediccion.place(x=posicionFrames[0], y=posicionFrames[1])         
    
    def ocultarOtrosFrames(self):
        #print('Intentadno eliminar')             
        self.frameDatosHistoricos.place_forget() 
        self.frameEntrenamientoRed.place_forget() 
        self.framePrediccion.place_forget()
        
    def dibujar(self):
    # Cracción Root y configuraciones iniciales
        ventana = Tk()
        posicion = str(ancho_ventana) + "x" + str(alto_ventana)
        ventana.geometry(posicion)
        ventana.resizable(0,0)
        ventana.minsize(width=ancho_ventana, height=alto_ventana)
        ventana.title('Predicción Demanda')
        ventana.config(bg=colorBlanco)
        ventana.iconbitmap('img/icono.ico')
        center(ventana)

        #Frame -> Contenedor

        frameGlobal = Frame(ventana, width = ancho_ventana,  height=alto_ventana, 
                            bg= colorBlanco, relief ='sunken')
        frameGlobal.grid(column=0,row=0)

        # Frames
      
        
        #  ----------------------------  Frame Entrenamiento de Red  -----------------------------------------------#        
        self.frameEntrenamientoRed = Frame(frameGlobal, width = ancho_ventana, 
                                    height=heightSubFrames, bg= colorAmarilloClaro, relief ='sunken')
        self.frameEntrenamientoRed.place(x=posicionFrames[0], y=posicionFrames[1])
        # --------------------------------------------------------------------------------------------------------------#


        #  ----------------------------  Frame Predicción  -----------------------------------------------#        
        self.framePrediccion = Frame(frameGlobal, width = ancho_ventana,  height=heightSubFrames, 
                                    bg= colorVerdeClaro, relief ='sunken')
        self.framePrediccion.place(x=posicionFrames[0], y=posicionFrames[1])
        # --------------------------------------------------------------------------------------------------------------#

        #  ----------------------------  Frame de Datos Históricos -----------------------------------------------#
        
        self.frameDatosHistoricos = Frame(frameGlobal, width = ancho_ventana,  
                                    height=heightSubFrames, bg= colorCeleste, relief ='sunken')
        self.frameDatosHistoricos.place(x=posicionFrames[0], y=posicionFrames[1])
        #frameDatosHistoricos.pack()
        # --------------------------------------------------------------------------------------------------------------#


        #  ---------------------------------------  Encabezado  ------------------------------------------------- #
        cargarImg(ventana, 'img/logo1.png',(100,100),(30,20))
        cargarImg(ventana, 'img/logo2.png',(100,100),(800,20))

        label1 = ttk.Label(frameGlobal, text="UNIVERSIDAD TÉCNICA DE COTOPAXI", background=colorBlanco, font=("Courie",14,'bold'))
        label1.place(x=280, y=10)

        label2 = ttk.Label(frameGlobal, text="INGENIERÍA ELÉCTRICA", background=colorBlanco, font=("Courie",14,'bold'))
        label2.place(x=350, y=40)

        canvasAutores = Canvas(frameGlobal, bg= colorBlanco, width = 350, height =50, bd =0, highlightthickness=2, highlightbackground=colorNegro)
        canvasAutores.place(x=300,y=75)

        labelAutores = ttk.Label(canvasAutores, text="Autores:\n-Autor1\n-Autor2", background=colorBlanco, font=("Courie",8,'bold'))
        labelAutores.place(x=5, y=5)


        # ------------------ Botones encabezado --------------------------

        btnDatosHistoricos = Button(frameGlobal,text= 'Datos Históricos',font=("Courie",10,'bold'),command=self.mostrarFrameDatosHistoricos, width=20, height=2, bd= 2,bg=colorBlanco, relief=GROOVE, highlightbackground=colorNegro)
        btnDatosHistoricos.place(x=50,y=140)

        btnEntrenamiento = Button(frameGlobal,text= 'Entrenamiento Red \nNeuronal',font=("Courie",10,'bold'),command=self.mostrarFrameEntrenamiento, width=20, height=2, bd= 2,bg=colorBlanco, relief=GROOVE, highlightbackground=colorNegro)
        btnEntrenamiento.place(x=270,y=140)

        btnPrediccion = Button(frameGlobal,text= 'Predicción de\nla demanda',font=("Courie",10,'bold'),command=self.mostrarFramePrediccion, width=20, height=2, bd= 2,bg=colorBlanco, relief=GROOVE, highlightbackground=colorAzul)
        btnPrediccion.place(x=490,y=140)

        btnSalir = Button(frameGlobal,text= 'Salir',font=("Courie",10,'bold'),command=ventana.destroy, width=20, height=2, bd= 2,bg=colorBlanco, relief=GROOVE, highlightbackground=colorAzul)
        btnSalir.place(x=710,y=140)


        # --------------- Elementos Frame Datos históricos ---------------------------- #

        canvasDatosHistoricos = Canvas(self.frameDatosHistoricos, bg= colorBlanco,
         width = 300, height =300, bd =0, highlightthickness=2, highlightbackground="white")
        canvasDatosHistoricos.place(x=15,y=10)
     

        def seleccionarRadioButton():
            print('Seleccionaste: ',opcion.get())        
            #opcionDatosHistoricos = opcion.get()

        global opcion
        opcion = StringVar()
        

        label0 = ttk.Label(canvasDatosHistoricos,width=22,text='Datos', background=colorBlanco, font=("Courie",10,'bold'))
        label0.place(x=35, y=15)
        
        radioTotal = Radiobutton(canvasDatosHistoricos, text="Total", variable=opcion, 
            value='Total', command=seleccionarRadioButton, tristatevalue=0)
        radioTotal.place(x=20,y=40)

        radioParcial = Radiobutton(canvasDatosHistoricos, text="Parcial", variable=opcion, 
            value='Parcial', command=seleccionarRadioButton, tristatevalue=0)
        radioParcial.place(x=20,y=60)

        label1 = ttk.Label(canvasDatosHistoricos,width=6,text='Desde', background=colorBlanco, font=("Courie",10))
        label1.place(x=20, y=100)
        
        label2 = ttk.Label(canvasDatosHistoricos,width=6,text='Hasta', background=colorBlanco, font=("Courie",10))
        label2.place(x=150, y=100)

        label3 = ttk.Label(canvasDatosHistoricos,width=6,text='Año', background=colorBlanco, font=("Courie",10))
        label3.place(x=5, y=120)

        combo = ttk.Combobox(canvasDatosHistoricos,values=[2018,2019,2020], width=5)
        combo.place(x=45,y=120)

        label4 = ttk.Label(canvasDatosHistoricos,width=6,text='Mes', background=colorBlanco, font=("Courie",10))
        label4.place(x=5, y=150)

        combo2 = ttk.Combobox(canvasDatosHistoricos,values=[1,2,3,4,5,6,7,8,9,10,11,12], width=5)
        combo2.place(x=45,y=150)
       
        label5 = ttk.Label(canvasDatosHistoricos,width=6,text='Día', background=colorBlanco, font=("Courie",10))
        label5.place(x=5, y=180)

        combo3 = ttk.Combobox(canvasDatosHistoricos,
            values=[1,2,3,4,5,6,7,8,9,10,11,12,13,14,15,16,17,18,19,20,21,22,23,24,25,26,27,28,29,30,31],
            width=5)
        combo3.place(x=45,y=180)
       
       

        # ------------------------------------------------------------------------------------------------------- #                
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
        # 
        ventana.mainloop()          

interfaz = Interfaz()
#interfaz.dibujar()