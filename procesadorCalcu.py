from io import open
import os
import time
import ManejadorMate
import modulos

def getRuta():
    print("-----------Seleccionar Ruta de Educacion---------------")
    print("1.Ingrese la ruta")
    print("2.El archivo esta en la misma carpeta")
    print("3.Regresar a Menu anterior")
    opcion = input()
    if opcion == "1":
        print("Por favor ingrese sola la ruta")
        ruta = input()
        ruta = ruta.strip()
        print("Escriba el nombre del archivo")
        arch = input()
        arch = arch.strip()
        rutaAbs = f"{ruta}\{arch}.mascotas"
        return rutaAbs
    elif opcion == "2":
        directorioActual = os.getcwd()
        print("Escriba el nombre del archivo")
        nombre = input()
        nombre = nombre.strip()
        rutaAbsoluta = f"{directorioActual}\{nombre}.edu"
        print(f"Es es nombre del archivo: {rutaAbsoluta}")
        return rutaAbsoluta
    elif opcion == "3":
        modulos.menuEducacion()
    else:
        print("Opcion Incorreta")
        getRuta()

def leerArchivo(archivoCompeto):
    try:
        archivo = open(f"{archivoCompeto}","r")
        texto = archivo.readlines()
        archivo.close()
        print(texto)
        procesadorComando(texto)
    except (FileNotFoundError, IOError):
        print("Error en la lectura")
        getRuta()

def procesadorComando(arreglo):
    for indice,valor in enumerate(arreglo):
        if valor.find("Variable") == 0:
            setVariable(valor)
        elif valor.find("Imprimir_Mensaje") == 0:
            setImprimirMensaje(valor)
        elif valor.find("Postfija") == 0:
            setPostFija(valor)
        elif valor.find("Incrementar") == 0:
            setIncrementar(valor)
        elif valor.find("Mitad") == 0:
            setMitad(valor)
        elif valor.find("Triple") == 0:
            setTriple(valor)
        elif valor.find("Positivo") == 0:
            setPositivo(valor)
        elif valor.find("Negativo") == 0:
            setNegativo(valor)
        elif valor.find("Imprimir") == 0:
            setImprimir(valor)
        elif valor.find("Potencia") == 0:
            setPotencia(valor)


def setVariable(arreglo):
    array = arreglo.split(":")
    posOne = array[1]
    valores = posOne.split(",")
    variable = valores[0]
    operacion = valores[1]
    print(f"La variable es {variable} y la operacoin es {operacion}")
    ManejadorMate.nuevaVarible(variable,operacion)

def setPostFija(arreglo):
    array = arreglo.split(":")
    expresionMat = array[1]
    print(f"La postfija y la expresion es {expresionMat}")
    ManejadorMate.separar(expresionMat)

def setIncrementar(arreglo):
    array = arreglo.split(":")
    nombreVariable = array[1]
    print(f"Incrementar en 1 la variable {nombreVariable}")
    ManejadorMate.incrementar(nombreVariable)

def setMitad(arreglo):
    array = arreglo.split(":")
    nombreVariable = array[1]
    print(f"Mitad en la variable {nombreVariable}")
    ManejadorMate.mitad(nombreVariable)

def setTriple(arreglo):
    array = arreglo.split(":")
    nombreVariable = array[1]
    print(f"Triplica la variable {nombreVariable}")
    ManejadorMate.triple(nombreVariable)

def setPositivo(arreglo):
    array = arreglo.split(":")
    nombreVariable = array[1]
    print(f"Positivo  la variable {nombreVariable}")
    ManejadorMate.postivo(nombreVariable)

def setNegativo(arreglo):
    array = arreglo.split(":")
    nombreVariable = array[1]
    print(f"Negativa la variable {nombreVariable}")
    ManejadorMate.negativo(nombreVariable)

def setPotencia(arreglo):
    array = arreglo.split(":")
    posOne = array[1]
    valores = posOne.split(",")
    expresionUno = valores[0]
    expresionDos = valores[1]
    expresionUno = expresionUno.strip()
    expresionDos = expresionDos.strip()
    print(f"La potencia es {expresionUno} y  {expresionDos}")
    ManejadorMate.potencia(expresionUno,expresionDos)

def setImprimir(arreglo):
    array = arreglo.split(":")
    nombreVariable = array[1]
    nombreVariable = nombreVariable.strip()
    print(f"Imprime la variable {nombreVariable}")
    ManejadorMate.imprimirVariable(nombreVariable)

def setImprimirMensaje(arreglo):
    array = arreglo.split(":")
    cadena = array[1]
    cadena = cadena.strip()
    print(f"Imprime la cadena {cadena}")
    ManejadorMate.imprimirMensaje(cadena)


def imprimirTexto(texto):
    archivo  = open("archivo.edu_result","a")
    hora = time.strftime("%H:%M:%S")
    fecha =  time.strftime("%d/%m/%y")
    fechaHora = f"[{fecha} {hora}]"
    tex = f"{fechaHora} {texto} \n"
    archivo.writelines(tex)
    archivo.close()