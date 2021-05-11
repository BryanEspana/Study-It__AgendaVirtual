#------------------DOCUMENTACIÓN EXTERNA------------------
#Diseño:
#           Diego Estuardo Lemus López - 21469
#             Diego José Valdez Soto - 21328
#      Bryan Carlos Roberto España Machorro - 21550
#         Gustavo Andrés González Pineda – 21438
#Fecha: 9/05/2021 | Proposito: Prototipo de menu de Study It - La agenta universitaria
import tkinter as tk
from tkinter.ttk import *
from PIL import Image, ImageTk



class ventana1:#Crea la primera ventana donde se despliega el menu
    ventana = 0
    posx_y = 0
    def __init__(self, main):#Función para agregar el self en la ventana llamada main
        self.main = main
        self.main.geometry("1300x700")#Dimensiones de la ventana
        self.main.title("Agenda Universitaria - Study It")#Nombre de la ventana
        self.main.configure(bg="gray10")#Color de background
        self.frame = tk.Frame(self.main)
        #Widget de color mas claro en el fondo
        self.widget = Image.open("widget.png")#Importa la imagen
        self.widget = ImageTk.PhotoImage(self.widget)#Agrega la imagen al tkinter
        self.widgetfondo = Label(self.main, image = self.widget). place(x=0,y=0)
        #Logo
        self.logo = Image.open("logo3.png")#Importa la imagen
        self.logo=ImageTk.PhotoImage(self.logo)#Agrega la imagen al Tkinter
        self.logoagenda=Label(self.main,image= self.logo).place(x=15,y=10)
        #FOTO UVG
        self.fotouvg = Image.open("logouvg1.png")#Importa la imagen
        self.fotouvg = ImageTk.PhotoImage(self.fotouvg)#Agregar la imagen a tkinter
        self.fotouvgg =Label(self.main, image= self.fotouvg).place(x=1090,y=10)
        #Citas Appa
        self.botonAPA = Image.open("botonApa.png")#Importa la imagen
        self.botonAPA=ImageTk.PhotoImage(self.botonAPA)#Agrega la imagen al Tkinter
        self.botonapa=Button(self.main,image= self.botonAPA, command=self.CrearVentanaAPA).place(x=15,y=125)#Crea y posiciona el botonAPA
        #Diccionario
        self.botonDic = Image.open("botonDiccionario.png")#Importa la imagen
        self.botonDic=ImageTk.PhotoImage(self.botonDic)#Agrega la imagen al Tkinter
        self.Botondic=Button(self.main,image= self.botonDic, command=self.CrearVentanaDic).place(x=15,y=225)#Crea y posiciona el boton del diccionario
        #Agenda
        self.botonAge = Image.open("botonAgenda.png")#Importar imagen
        self.botonAge = ImageTk.PhotoImage(self.botonAge)#Agregar l a imagen a tkinter
        self.botonAgenda = Button(self.main,image = self.botonAge, command=self.CrearVentanaAgenda).place(x=15,y=325)#Crea y posiciona el boton de agenda
        #Boton de información
        self.botoninf = Image.open("info.png")#Importa la image
        self.botoninf = ImageTk.PhotoImage(self.botoninf)#Agrega la imagen a tkinter
        self.botoninfo = Button(self.main, image=self.botoninf, command=self.CrearVentanaInf).place(x=15, y = 600)#Crea y pocisiona el boton de información de abajo
        #Esta funcion cierra el programa
        self.exitbuton = Image.open("exit.png")#Importar Imagen
        self.exitbuton = ImageTk.PhotoImage(self.exitbuton)
        self.botonClose = Button(self.main, image=self.exitbuton, command=self.quit).place(x=1200,y=640)#Boton para cerrar programa
        self.frame.pack()#Termina el frame

    #Cerrar programa
    def quit(self):
        self.main.destroy()
    #Crear ventana de APA
    def CrearVentanaAPA(self):
        VentanaAPA = tk.Toplevel(self.main)

    #Crea ventana del Diccionario
    def CrearVentanaDic(self):
        VentanaDic = tk.Toplevel(self.main)
    #Crea ventana de Agenda
    def CrearVentanaAgenda(self):
        VentanaAgenda = tk.Toplevel(self.main)
    
    #Crea ventana de información
    def CrearVentanaInf(self):
        ventanaInf= tk.Toplevel(self.main)

raiz = tk.Tk()
app = ventana1(raiz)
raiz.mainloop()



