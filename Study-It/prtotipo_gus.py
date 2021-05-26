from tkinter import *
import pandas as pd
from tkinter import messagebox
import matplotlib.pyplot as pt

#Estilos de fuente
font_title = ("Helvetica", 30, " bold italic")
font_text = ("Helvetica", 15, " bold")
font_small = ("Helvetica", 7, " bold")
font_text2 = ("Helvatica", 15)

def graficarTipo():
    global df    
    df = pd.read_csv("proto3.csv")
    GrafTipoAPA = df[df["TipodeCita"]=="APA"]
    GrafTipoMLA = df[df["TipodeCita"]=="MLA"]
    GraficaAPA = len(GrafTipoAPA)
    GraficaMLA = len(GrafTipoMLA)
    print(GrafTipoAPA)
    print(GrafTipoMLA)
    fig, ax = pt.subplots()
    ax.set_ylabel("Cantidad")
    ax.set_xlabel("Tipo de Cita")
    pt.bar("APA", GraficaAPA, width=0.75)
    pt.bar("MLA", GraficaMLA, width=0.75)
    pt.show()
    
def graficarAnio():
    global df    
    df = pd.read_csv("proto3.csv")
    GrafAnio = df["Anio"].value_counts()
    df.groupby(GrafAnio["Anio"]).plot(kind = "line", title="Grafica por Año", xlabel="Años", ylabel="Cantidad")
    pt.show()

    
def winEstadistica():
    estadistic = Toplevel()
    estadistic.configure(bg="#1a1a1a")
    estadistic.geometry("500x500")
    #Boton de Graficar Citas por Tipo
    citasTipo = Button(estadistic, text = "Graficar Citas por Tipo", pady = 10, padx= 20, command=graficarTipo)
    citasTipo.configure(font = font_text)
    citasTipo.place(x=20,y=50)
    #Boton de Graficar Citas por Año
    citasTipo = Button(estadistic, text = "Graficar Citas por Año", pady = 10, padx= 20, command=graficarAnio)
    citasTipo.configure(font = font_text)
    citasTipo.place(x=20,y=200)
    #Boton de Graficar Diccionario por Categoria
    citasTipo = Button(estadistic, text = "Graficar Diccionario por Categoría", pady = 10, padx= 20)
    citasTipo.configure(font = font_text)
    citasTipo.place(x=20,y=350)
    
#Boton info
def winInfo():
    # Se Crea la ventana INnfo
    info = Toplevel()
    info.configure(bg="#1a1a1a")
    info.geometry("300x200")
    #label
    text1 = Label(info, text = "Creadores:\nBryan España - 21550,\nGustavo Gonzales - 21438,\nDiego Valdez - 21328,\nDiego Lemus - 21469\n\n\n Agenda universitaria", bg="#1a1a1a", fg="white")
    text1.configure(font = font_text2)
    text1.place(x=20,y=10)
#-----------------Ventana Normas APA---------------   
def winAPA():
    #Abrir el CSV 
    global df
    df = pd.read_csv("proto3.csv")
    Nombre = StringVar()
    Apellido = StringVar()
    Anio = StringVar()
    Titulo = StringVar()
    SitioObtenido = StringVar()
    URL = StringVar()
    citaObtenida = StringVar()
#Cerrar Programa
    def cerrar():
        APA.destroy()
#Funcion limpiar citas
    def limpiar():
        mydic={"Apellido":[], "Nombre":[], "Anio":[], "Titulo":[], "SitioObtenido":[], "URL":[],"TipodeCita":[]}
        df = pd.DataFrame(mydic)
        df.to_csv("proto3.csv",index=False)
# Funcion para generar MLA
    def generarMLA():
        global df
        data = pd.DataFrame({"Apellido":[Apellido.get()], "Nombre":[Nombre.get()], "Anio":[Anio.get()], "Titulo":[Titulo.get()], "SitioObtenido":[SitioObtenido.get()], "URL":[URL.get()],"TipodeCita":["MLA"]})
        df = df.append(data, ignore_index = True)
        df.to_csv("proto3.csv", index = False)
        citaObtenida.set(Apellido.get()+""+Nombre.get() + ", "+Titulo.get() + ", ("+Anio.get()+"), "+ URL.get())
#Funcion para generar APA 
    def generarAPA(): 
        global df
        data = pd.DataFrame({"Apellido":[Apellido.get()], "Nombre":[Nombre.get()], "Anio":[Anio.get()], "Titulo":[Titulo.get()], "SitioObtenido":[SitioObtenido.get()], "URL":[URL.get()],"TipodeCita":["APA"]})
        df = df.append(data, ignore_index = True)
        df.to_csv("proto3.csv", index = False)
        citaObtenida.set(Apellido.get() + " "+Nombre.get()+",("+Anio.get()+"), "+Titulo.get()+", "+SitioObtenido.get()+", "+URL.get())


    # Se Crea la ventana AGENDA
    APA = Toplevel()
    APA.configure(bg="#1a1a1a")
    APA.geometry("1366x768")
    
    #Texto de Apellido Autor
    autorentry = Label(APA, text = "Ingrese el Apellido del Autor:", bg="#1a1a1a", fg="white")
    autorentry.configure(font = font_text2)
    autorentry.place(x=100,y=50)

    #Button Apellido Autor
    autorname = Entry(APA,textvariable=Apellido)
    autorname.insert(0, "")
    autorname.place(x= 400, y=50)

    #Label Nombre Autor
    anioentry = Label(APA, text = "Ingrese el Nombre del Autor:", bg="#1a1a1a", fg="white")
    anioentry.configure(font = font_text2)
    anioentry.place(x=100,y=100)
    #Buton Nombre Autor
    anio = Entry(APA, textvariable=Nombre)
    anio.insert(0, "" )
    anio.place(x = 400, y=100)

    #Label Año
    anioentry = Label(APA, text = "Ingrese el año:", bg="#1a1a1a", fg="white")
    anioentry.configure(font = font_text2)
    anioentry.place(x=100,y=150)

    #Buton Año
    anio = Entry(APA, textvariable=Anio)
    anio.insert(0, "" )
    anio.place(x = 400, y=150)

    #Label Titulo 
    tituloentry = Label(APA, text = "Ingrese el Titulo:", bg="#1a1a1a", fg="white")
    tituloentry.configure(font = font_text2)
    tituloentry.place(x=100,y=200)
    #Buton Titulo
    titulop = Entry(APA, textvariable=Titulo)
    titulop.insert(0, "" )
    titulop.place(x = 400, y=200)

    # Label Sitio de donde se obtuvo
    sitioentry = Label(APA, text = "Ingrese el Sitio de obtención:", bg="#1a1a1a", fg="white")
    sitioentry.configure(font = font_text2)
    sitioentry.place(x=100,y=250)

    #Buton sitio
    sitio = Entry(APA, textvariable=SitioObtenido)
    sitio.insert(0, "" )
    sitio.place(x = 400, y=250)

    #Label URL
    URLentry = Label(APA, text = "Ingrese el link:", bg="#1a1a1a", fg="white")
    URLentry.configure(font = font_text2)
    URLentry.place(x=100,y=300)

    #Button URl
    URLlink = Entry(APA, textvariable=URL)
    URLlink.insert(0, "" )
    URLlink.place(x = 400, y=300)

    #Generar Cita APA
    GenerarCita = Button(APA, text = "Generar Cita en formato APA", pady = 10, padx= 10, command = generarAPA)
    GenerarCita.configure(font = font_text)
    GenerarCita.place(x=50,y=400)
    #Generar Cita
    GenerarCita = Button(APA, text = "Generar Cita en formato MLA", pady = 10, padx= 10, command = generarMLA)
    GenerarCita.configure(font = font_text)
    GenerarCita.place(x=50,y=500)
    #RESULTADO

    CitaGenerada = Entry(APA)
    CitaGenerada.config(textvariable=citaObtenida)
    CitaGenerada.place(x = 400, y = 400, width=600, height=50)

    #Boton REGRESAR que cierra la ventana 
    back = Button(APA, text = "regresar", pady = 10, padx= 20, command = cerrar)
    back.configure(font = font_text)
    back.place(x=1100,y=10)

    #Boton limpiar de Citas 
    GenerarCita = Button(APA, text = "Clear", pady = 10, padx= 10, command = limpiar)
    GenerarCita.configure(font = font_text)
    GenerarCita.place(x=1100,y=500)


#----------------- VENTANA DICCIONARIO -----------------
#Ventana de DICCIONARIO
def winDic():
    def cerrar():
        dic.destroy()

    #Se definen variables globales
    global x
    global cont
    global condicion
    x = pd.read_csv("proto2.csv")
    cont = -1
    condicion = True
    

    #Se crea FUNCION para AGREGAR palabras al dataframe
    def agregarFun():
        global x
        #global ekey
        #global evalue
        key = str(ekey.get())
        value = str(evalue.get())
        df = pd.DataFrame({"palabra":[key], "definicion":[value]})
        x = x.append(df, ignore_index = True) 
        x.to_csv("proto2.csv", index = False)  
        ekey.delete(len(key))  
        evalue.delete(len(value))  

    #Se crea la funcion para el boton SWITCH
    def switchFun():
        global x
        global condicion
        global txt   
        global cont     
        if condicion:
            txt.destroy()
            txt = Label(framedic, text= str(x["palabra"][cont]))
            txt.pack(pady = 100)
            txt.configure(font = font_title)
            condicion = False
        else:
            txt.destroy()
            txt = Label(framedic, text= str(x["definicion"][cont]))
            txt.pack(pady = 100)
            txt.configure(font = font_title)
            condicion = True 

    #Se crea la FUNCION para el boton NEXT
    def nextFun():
        global cont
        global x
        global txt
        global condicion
        global displ
        if cont < (len(x)-1):
            cont += 1
            txt.destroy()
            txt = Label(framedic, text = x["palabra"][cont])
            txt.configure(font = font_title)
            txt.pack( pady = 100)
            condicion = False

            displ.destroy()
            displ = Label(dic, text = (str(cont+1)+ "/" + str(len(x))))
            displ.place(x= 660, y = 225 )
        else:
            pass

    #FUNCION para el boton PREV
    def prevFun():
        global cont
        global x
        global txt
        global condicion
        global displ
        if cont > 0:
            cont -= 1
            txt.destroy()
            txt = Label(framedic, text = x["palabra"][cont])
            txt.configure(font = font_title)
            txt.pack( pady = 100)
            condicion = False

            displ.destroy()
            displ = Label(dic, text = (str(cont+1)+ "/" + str(len(x))))
            displ.place(x= 660, y = 225 )
        else:
            pass

    #FUNCION para el boton CLEAR
    def clearFun():
        global x
        global txt

        response = messagebox.askyesno(title="Clear", message="Seguro que quiere borrar todos los datos?", icon='info')
        if response == 1:
            miDic = {"palabra": [], "definicion": []}
            n = pd.DataFrame(miDic)
            n.to_csv("proto2.csv", index = False)
            x = n

            txt.destroy()
            txt = Label(framedic, text = "Los datos han sido borrados")
            txt.pack(pady = 100)
            txt.configure(font = font_title)

            global displ
            displ.destroy()
            displ = Label(dic, text = "Na/Na")
            displ.place(x= 660, y = 225 )
        
        else:
            pass

  

    #Se crea la ventana DICCIONARIO
    dic = Toplevel()
    dic.configure(bg="#1a1a1a")
    dic.geometry("1366x768")


    #Se crea boton de REGRESAR
    back = Button(dic, text = "Regresar", pady = 10, padx= 20, command = cerrar)
    back.configure(font = font_text)
    back.place(x=1250,y=10)

    #Se crea el FRAME de la ventana DICCIONARIO
    framedic = LabelFrame(dic)
    framedic.configure(bg= "#1a1a1a")
    framedic.pack(expand = True, fill = X)

    #Se inserta el TEXTO inicial en el FRAME
    global txt
    txt = Label(framedic, text = "Bienvenido a las Flashcards agrega una palabra o usa las que ya tienes")
    txt.configure(font = font_title)
    txt.pack(pady = 100)

    #Se crea le BOTON SWITCH para cambiar entre palabra y definicion
    switch = Button(dic, text = "Switch", command = switchFun)
    switch.place(x=665,y=647)

    #Se crea el BOTON NEXT para cambiar al siguiente indice
    nextb = Button(dic, text = ">>", command = nextFun)
    nextb.place(x=745,y=647)

    #Se crea el BOTON PREV para cambiar al indice anterior
    prev = Button(dic, text = "<<", command = prevFun)
    prev.place(x=615,y=647)

    #Se crea el ENTRY para colocar la PALABRA
    #global ekey
    ekey = Entry(dic)
    ekey.place(x=592, y=496)
    ekey.insert(0, "Inserta tu palabra..." )

    #Se Crea el ENTRY para colocar la DEFINICION
    #global evalue
    evalue = Entry(dic)
    evalue.place(x=592, y=543)
    evalue.insert(0, "Inserta tu definicion..." )

    #BOTON AGREGAR
    add = Button(dic, text = "Agregar", command = agregarFun)
    add.place(x=665,y=597)


    #BOTON CLEAR
    clear = Button(dic, text = "clear", command = clearFun)
    clear.place(x=670,y=677)


    #Se crea el DISPLAY
    global displ
    displ = Label(dic, text = "Na/Na")
    displ.place(x= 660, y = 225 )



#----------------- VENTANA AGENDA -----------------

#Ventana de AGENDA(notas)    
def winAgenda():
    def cerrar():
        agenda.destroy()
    
    #Se Crea la ventana AGENDA
    agenda = Toplevel()
    agenda.configure(bg="#1a1a1a")
    agenda.geometry("1366x768")
    
    #Se crea el FRAME de la ventana AGENDA
    frame = LabelFrame(agenda)
    frame.configure(bg= "#2c2c2c")
    frame.pack(expand = True, fill = BOTH)
        
    #Ventana de TEXTO adentro del frame 
    datos = pd.read_csv("proto1.csv")
    n = datos["0"][0]

    texto = Text(frame)
    texto.pack(expand = True, fill = BOTH)
    texto.insert(INSERT, str(n))

    #Boton REGRESAR que cierra la ventana 
    back = Button(agenda, text = "regresar", pady = 10, padx= 20, command = cerrar)
    back.configure(font = font_text)
    back.place(x=1250,y=10)

    #COMANDO del boton guardar
    def click():
        txt = pd.Series([texto.get('1.0', 'end-1c')])
        txt.to_csv("proto1.csv")

    #Boton GUARDAR
    guardar = Button(agenda, text = "Guardar", pady = 10, padx= 20, command = click)
    guardar.configure(font = font_text)
    guardar.pack(pady = 10)


        

        
#----------------- PAGINA PRINCIPAL -----------------

#Se crea la ventana principal
root = Tk(className = "    Study It    ")
root.configure(bg="#1a1a1a")
root.geometry("1366x768")

def cerrar():
    root.destroy()

#Frame y sus ajustes
frame = LabelFrame(root, padx = 40, pady = 20)
frame.configure(bg= "#2c2c2c")
frame.pack(expand = True, fill = "y", anchor = "w")

#Titulo
label = Label(frame, text = "Study It", bg = "#2c2c2c" , fg = "white", pady = 40)
label.configure(font = font_title)
label.grid(row = 0, column = 0, columnspan=2)

#Boton de CITAS APA
citas = Button(frame, text = "Citas", padx= 50, pady = 10, command=winAPA)
citas.configure(font = font_text)
citas.grid(column=0, row =1, columnspan=2)

#Boton de DICCIONARIO
dic = Button(frame, text = "Diccionario", padx= 20, pady = 10, command = winDic)
dic.configure(font = font_text)
dic.grid(column=0, row =2, pady = 40, columnspan=2)

#Boton de AGENDA(notas)
agenda = Button(frame, text = "Agenda", padx= 40, pady = 10, command = winAgenda)
agenda.configure(font = font_text)
agenda.grid(column=0, row =3, columnspan=2)

# Boton Estadisticas 
estadistica = Button(frame, text = "Estadisticas", padx= 10, pady = 10, command=winEstadistica)
estadistica.configure(font = font_text)
estadistica.grid(column=0, row =5, columnspan=2, pady = 0)


#Boton de informacion
info = Button(frame, text = "info.",padx= 5, pady = 5, command=winInfo)
info.configure(font = font_small)
info.grid(column=0, row =4, pady = 100)

back = Button(root, text = "Salir", pady = 10, padx= 20, command = cerrar)
back.configure(font = font_text)
back.place(x=1250,y=10)


root.mainloop()
