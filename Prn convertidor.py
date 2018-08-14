# -*- coding: utf-8 -*-
#Importacion de librerias 
import re                                              #Expresiones Regulares, para buscar mejor en el archivo
from Tkinter import *                                  #Paquete grafico con los dialogos
import Tkinter, Tkconstants, tkFileDialog,tkMessageBox #Librerias especificas para el explorador
import sqlite3
#Creacion de Ventana
root = Tk()
root.geometry('300x300')

#Menu de opciones
var1 = StringVar()
var1.set('Convertir TXT a PRN')
opt1 = OptionMenu(root,var1, 'Convertir TXT a PRN', 'Convertir TXT al Banco').pack(fill=X)
def state():
        if var1.get() == 'Convertir TXT a PRN':
                #Codigo para las nominas en PRN
                        #Definicion de columnas
                        col1 = list()
                        col2 = list()
                        col3 = list()

                        #Seleccion de archivo
                        fname = tkFileDialog.askopenfilename(initialdir = "/",title = "Seleccione Archivo",filetypes = (("Archivo de Texto","*.txt"),("Archivo de EXCEL", "*.CSV")))
                        #Codigos guardianes en caso de seleccionar cancelar
                        try:
                        #Procesamiento del mismo
                                entrada = str(fname)
                                fopen = open(entrada,'r')
                                for i in fopen:
                        	       col = re.findall("[0-9]+", i)
                                       if len(col) < 2: continue
                                       col1.append(col[0].lstrip('0'))
                                       col2.append(col[1].lstrip('0'))
                                       decimal = col[2]+'.'+col[3]
                                       col3.append(decimal)
                                fopen.close()
                                #Confirmacion de archivo
                                ans = tkMessageBox.showinfo("Confirmacion", "Archivo cargado con exito\nPulse Aceptar para continuar")
                                fexit = tkFileDialog.asksaveasfilename(initialdir = "/",title = "Select file",filetypes = (("Archivo del sistema BOX","*.PRN"),("all files","*.*")))
                                salida = str(fexit)
                                salida = salida + '.prn'
                                archivo_salida = open(salida, 'a')
                                cont = 0
                                while cont < len(col1):
                                        separador = " "
                                        sp1 = separador * (10 - len(col1[cont]))
                                        sp2 = separador * (10 - len(col2[cont]))
                                        sp3 = separador * (10 - len(col3[cont]))
                                        prn = sp1 + col1[cont] + sp2 + col2[cont] + sp3 + col3[cont] + "\n"
                                        cont = cont + 1
                                        archivo_salida.write(prn)
                                comp = tkMessageBox.showinfo("Confirmacion", "Archivo creado con exito\nPulse Aceptar para continuar")
                        #Salida si no se selecciona ningun archivo
                        except:
                                errores = tkMessageBox.showinfo("Aviso", "No se ha seleccionado ningun archivo")
        elif var1.get() == 'Convertir TXT al Banco':
                #Seleccion de archivo
                fname = tkFileDialog.askopenfilename(initialdir = "/",title = "Seleccione Archivo",filetypes = (("Archivo de Texto","*.txt"),("Archivo de EXCEL", "*.CSV")))
                archivo_apertura = str(fname)
                #Definicion de columnas
                lista_cedulas = list()
                lista_nombres = list()
                lista_cuentas = list()
                lista_montos = list()
                try:
                        fopen = open(archivo_apertura,'r')
                        cont = 0
                        for i in fopen:
                                cedula = i[3:11]
                                cedula = cedula.lstrip('0')
                                lista_cedulas.append(cedula)
                                nombre =  i[11:44]
                                nombre = nombre.rstrip(" ")
                                lista_nombres.append(nombre)
                                cuenta = i[59:79]
                                lista_cuentas.append(cuenta)
                                monto =  i[45:58]
                                monto = monto.lstrip('0')
                                monto = float(monto)
                                monto = monto / 100
                                lista_montos.append(monto)
                        aviso = tkMessageBox.showinfo("Confirmacion", "Archivo cargado con exito\nPulse Aceptar para continuar")
                        salida = tkFileDialog.asksaveasfilename(initialdir = "/",title = "Select file",filetypes = (("Archivo de texto","*.txt"),("all files","*.*")))
                        fexit = str(salida)
                        fexit = fexit + '.txt'
                        cont = 0
                        while cont < len(lista_cedulas):
                                txt = lista_cedulas[cont] + ";" + lista_nombres[cont] + ";" + lista_cuentas[cont] + ";" + lista_montos[cont] + "\n"
                                fexit.write(txt)
                                cont = cont + 1
                        terminado = tkMessageBox.showinfo("Confirmacion", "Archivo creado con exito\nRecuerde 3 pasos:\n1. Abrir el archivo con EXCEL\n 2. Seleccionar la opcion 'Texto en Columnas'\n 3. Seleccionar la opcion 'Delimitados'\n 4. Seleccione el atributo Texto\nPresione Aceptar para continuar")
                except:
                        errores = tkMessageBox.showinfo("Aviso", "No se ha seleccionado ningun archivo")

                
Button(root,command=state,text='Lanzar programa').pack()
root.mainloop()
