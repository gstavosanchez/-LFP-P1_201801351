import sys
import re
from Variable import *
import procesadorAlmacen

listaVar = []
listaLetra = []
def crearVariable(nombre,valor):
    nombre = nombre.strip()
    valor = valor.strip()
    va = buscarVariable(nombre)
    if va == None:
        nuevaVariable = Varibale(nombre,valor)
        listaVar.append(nuevaVariable)
        print("Se creo la variable")
        setLetra(valor)



def buscarVariable(nombre):
    for valor in listaVar:
        if nombre == valor.getNombre():
            return valor
    

def getPosicion(nombre):
    nombre = nombre.strip()
    variable = buscarVariable(nombre)
    posicion = 0
    if variable != None:
        for pos,valor in enumerate(listaVar):
            if nombre == valor.getNombre():
                posicion = pos + 1
                texto = f"{nombre}, Pos: {posicion}"
                procesadorAlmacen.imprimirTexto(texto)
                break 
        
    
def getTamanio(nombre):
    nombre = nombre.strip()
    variable = buscarVariable(nombre)
    tamanio = 0
    if variable != None:
        valor = variable.getValor()
        tamanio = len(valor)
        texto = f"{nombre},Tam:{tamanio}"
        procesadorAlmacen.imprimirTexto(texto)
        

def setLetra(palabra):
    longitu = len(palabra)
    listaLetra.append(longitu)
    for i in range(len(palabra)):
        letra = palabra[i]
        listaLetra.append(letra)
    print(listaLetra)

def imprimirLetra(nombre):
    nombre = nombre.strip()
    variable = buscarVariable(nombre)
    print(nombre)
    if variable != None:
        letraInico = ""
        letraFin = ""
        palabra = variable.getValor()
        palabra = palabra.strip()
        longitud = len(palabra)
        for i in range(len(palabra)):
            if i == 0:
                letraInico = palabra[i]
            elif i == len(palabra) - 1:
                letraFin = palabra[i ]
        print(letraInico)
        print(letraFin)
        print("Longitud: ", longitud)
        posicionInicio = 0
        posicionFin = 0
        for i in range(len(listaLetra)):
            if letraInico == listaLetra[i]:
                print(listaLetra[i]," Posicion:",i + 1)
                posicionInicio = i
                print(posicionInicio)
                break
        posicionFin = (posicionInicio + longitud) - 1
        print("Poscion de fin:",posicionFin)
        for i in range(len(listaLetra)):
            if i>= posicionInicio and i<= posicionFin:
                print(listaLetra[i]," Posicion:",i + 1)
                letra = listaLetra[i]
                po = i + 1
                texto = f"{nombre},{po},{letra}"
                procesadorAlmacen.imprimirTexto(texto)

            
            
def generaGrafix():
    

