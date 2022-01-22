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

# Listas de datos para los comboxs
global listaAnos
listaAnos = [2015,2016,2017,2018,2019,2020,2021]
global listaMeses
listaMeses = [1,2,3,4,5,6,7,8,9,10,11,12]
global listaDias
listaDias = [1,2,3,4,5,6,7,8,9,10,11,12,13,14,15,16,17,18,19,20,21,22,23,24,25,26,27,28,29,30,31]
global listaHoras
listaHoras = [0,1,2,3,4,5,6,7,8,9,10,11,12,13,14,15,16,17,18,19,20,21,22,23]
global listaOptimizadores
listaOptimizadores = ['RMSprop','Adam','Adadelta']

 
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


# 1.  --------------- Elementos Frame Datos históricos ---------------------------- #

        # 1. Canvas de controles
        canvasDatosHistoricos = Canvas(self.frameDatosHistoricos, bg= colorBlanco,
         width = 250, height =240, bd =0, highlightthickness=2, highlightbackground="white")
        canvasDatosHistoricos.place(x=15,y=10)

        # 2. Botones de control
        
        btnvisualizarDatos = Button(self.frameDatosHistoricos,text= 'Visualizar Datos',
            font=("Courie",10,'bold'),command=self.nada, width=31, height=2, 
            bd= 2,bg=colorBlanco, relief=GROOVE, highlightbackground=colorAzul)
        btnvisualizarDatos.place(x=15,y=265)

        btnGraficar = Button(self.frameDatosHistoricos,text= 'Graficar',
            font=("Courie",10,'bold'),command=self.nada, width=31, height=2, 
            bd= 2,bg=colorBlanco, relief=GROOVE, highlightbackground=colorAzul)
        btnGraficar.place(x=15,y=315)

        btnExportar = Button(self.frameDatosHistoricos,text= 'Exportar gráfico',
            font=("Courie",10,'bold'),command=self.nada, width=31, height=2, 
            bd= 2,bg=colorBlanco, relief=GROOVE, highlightbackground=colorAzul)
        btnExportar.place(x=15,y=365)


        def seleccionarRadioButton():
            print('Seleccionaste: ',opcion.get())        
            #opcionDatosHistoricos = opcion.get()

        global opcion
        opcion = StringVar()
        
        # --- Sección de radio buttons

        label0 = ttk.Label(canvasDatosHistoricos,width=22,text='Datos', background=colorBlanco, font=("Courie",10,'bold'))
        label0.place(x=100, y=15)
        
        radioTotal = Radiobutton(canvasDatosHistoricos, text="Total", variable=opcion, 
            value='Total', command=seleccionarRadioButton, tristatevalue=0)
        radioTotal.place(x=80,y=40)

        radioParcial = Radiobutton(canvasDatosHistoricos, text="Parcial", variable=opcion, 
            value='Parcial', command=seleccionarRadioButton, tristatevalue=0)
        radioParcial.place(x=80,y=60)

        # -- Encabezados para seleccionar fecha

        label0 = ttk.Label(canvasDatosHistoricos,width=6,text='Desde', background=colorBlanco, font=("Courie",10, 'bold'))
        label0.place(x=20, y=90)
        
        label2 = ttk.Label(canvasDatosHistoricos,width=6,text='Hasta', background=colorBlanco, font=("Courie",10,'bold'))
        label2.place(x=150, y=90)

        # --- Parte izquierda desde

        label3 = ttk.Label(canvasDatosHistoricos,width=6,text='Año', background=colorBlanco, font=("Courie",10))
        label3.place(x=5, y=120)

        combo1 = ttk.Combobox(canvasDatosHistoricos,values=listaAnos, width=5)
        combo1.place(x=45,y=120)

        label4 = ttk.Label(canvasDatosHistoricos,width=6,text='Mes', background=colorBlanco, font=("Courie",10))
        label4.place(x=5, y=150)

        combo2 = ttk.Combobox(canvasDatosHistoricos,values=listaMeses, width=5)
        combo2.place(x=45,y=150)
       
        label5 = ttk.Label(canvasDatosHistoricos,width=6,text='Día', background=colorBlanco, font=("Courie",10))
        label5.place(x=5, y=180)

        combo3 = ttk.Combobox(canvasDatosHistoricos,
            values=listaDias,
            width=5)
        combo3.place(x=45,y=180)
       
        label6 = ttk.Label(canvasDatosHistoricos,width=6,text='Hora', background=colorBlanco, font=("Courie",10))
        label6.place(x=5, y=210)

        combo4 = ttk.Combobox(canvasDatosHistoricos,
            values=listaHoras,
            width=5)
        combo4.place(x=45,y=210)


        # Parte derecha - Hasta
        
        label7 = ttk.Label(canvasDatosHistoricos,width=6,text='Año', background=colorBlanco, font=("Courie",10))
        label7.place(x=125, y=120)

        combo5 = ttk.Combobox(canvasDatosHistoricos,values=listaAnos, width=5)
        combo5.place(x=165,y=120)

        label4 = ttk.Label(canvasDatosHistoricos,width=6,text='Mes', background=colorBlanco, font=("Courie",10))
        label4.place(x=125, y=150)

        combo6 = ttk.Combobox(canvasDatosHistoricos,values=listaMeses, width=5)
        combo6.place(x=165,y=150)
       
        label5 = ttk.Label(canvasDatosHistoricos,width=6,text='Día', background=colorBlanco, font=("Courie",10))
        label5.place(x=125, y=180)

        combo7 = ttk.Combobox(canvasDatosHistoricos,
            values=listaDias,
            width=5)
        combo7.place(x=165,y=180)
       
        label6 = ttk.Label(canvasDatosHistoricos,width=6,text='Hora', background=colorBlanco, font=("Courie",10))
        label6.place(x=125, y=210)

        combo8 = ttk.Combobox(canvasDatosHistoricos,
            values=listaHoras,
            width=5)
        combo8.place(x=165,y=210)


#  2.  --------------- Elementos Frame Entrenamiento Red Neuronal ---------------------------- #
# Usa desde el combox número 9

        # 1. Canvas de controles
        canvasEntrenamiento = Canvas(self.frameEntrenamientoRed, bg= colorBlanco,
         width = 250, height =240, bd =0, highlightthickness=2, highlightbackground="white")
        canvasEntrenamiento.place(x=15,y=10)     

         # 2. Botones de control
        
        btnvisualizarDatos = Button(self.frameEntrenamientoRed,text= 'Entrenar Red Neuronal',
            font=("Courie",10,'bold'),command=self.nada, width=31, height=2, 
            bd= 2,bg=colorBlanco, relief=GROOVE, highlightbackground=colorAzul)
        btnvisualizarDatos.place(x=15,y=265)

        btnGraficar = Button(self.frameEntrenamientoRed,text= 'Exportar Gráfica',
            font=("Courie",10,'bold'),command=self.nada, width=31, height=2, 
            bd= 2,bg=colorBlanco, relief=GROOVE, highlightbackground=colorAzul)
        btnGraficar.place(x=15,y=315)

        #btnExportar = Button(self.frameDatosHistoricos,text= 'Exportar gráfica\nentrenamientp',
            #font=("Courie",10,'bold'),command=self.nada, width=31, height=2, 
            #bd= 2,bg=colorBlanco, relief=GROOVE, highlightbackground=colorAzul)
        #btnExportar.place(x=15,y=365)

         # --- Sección de radio buttons

        label7 = ttk.Label(canvasEntrenamiento,width=22,text='Parámetros', background=colorBlanco, font=("Courie",10,'bold'))
        label7.place(x=85, y=15)
  
        label8 = ttk.Label(canvasEntrenamiento,width=11,text='Optimizador', background=colorBlanco, font=("Courie",10))
        label8.place(x=15, y=50)

        combo9 = ttk.Combobox(canvasEntrenamiento,values=listaOptimizadores, state='readonly',width=9)
        combo9.place(x=125,y=50)
        
        label9 = ttk.Label(canvasEntrenamiento,width=11,text='Neuronas', background=colorBlanco, font=("Courie",10))
        label9.place(x=15, y=80)

        entryNeuronas = ttk.Entry(canvasEntrenamiento,width=12)
        entryNeuronas.place(x=125, y=80)

        #labeln = ttk.Label(canvasEntrenamiento,width=11,text='Learning-Rate', background=colorBlanco, font=("Courie",10))
        #labeln.place(x=15, y=80)

        #entryLearningRate = ttk.Entry(root)
        #entryLearningRate.place(x=110, y=120)


        
    #Ejecución
        ventana.mainloop()          

interfaz = Interfaz()
#interfaz.dibujar()