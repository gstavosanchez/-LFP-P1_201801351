from io import open
import os
from Gato import *

listaGato = []
def leerArchivo(archivoCompeto):
    try:
        archivo = open(f"{archivoCompeto}","r")
        texto = archivo.readlines()
        archivo.close()
        print(texto)
        proceso(texto)
    except (FileNotFoundError, IOError):
        print("Error en la lectura")
        obetenerRuta()



def obetenerRuta():
    print("1.Ingrese la ruta")
    print("2.El archivo esta en la misma carpeta")
    opcion = input()
    if opcion == "1":
        print("Por favor ingrese sola la ruta")
        ruta = input()
        print("Escriba el nombre del archivo")
        arch = input()
        rutaAbs = f"{ruta}\{arch}.mascotas"
        return rutaAbs
    elif opcion == "2":
        directorioActual = os.getcwd()
        print("Escriba el nombre del archivo")
        nombre = input()
        rutaAbsoluta = f"{directorioActual}\{nombre}.mascotas"
        print(f"Es es nombre del archivo: {rutaAbsoluta}")
        return rutaAbsoluta
    else:
        print("Opcion Incorreta")
        obetenerRuta()


# ruta = obetenerRuta()   
# arreglo=leerArchivo(ruta)



def creaAnimalGato(animal):
    comando = animal.split(":")
    for indice,valor in enumerate(comando):
        if valor== "Crear_Gato" and indice== 0:
            print("El valor es :",valor," De la posicion ", indice)            
        elif indice == 1:
            print("Posicion de <:", valor.find('<'))
            print("Posicion de <:", valor.find('>'))
            nombreAnimal = valor[valor.find('<') + 1 :valor.find('>')]
            print(nombreAnimal)
            print("Se creo el gato: ",nombreAnimal)
            crearGato(nombreAnimal)
    
def creaAnimalPajaro(animal):
    comando = animal.split(":")
    for indice,valor in enumerate(comando):
        if valor== "Crear_Pajaro" and indice== 0:
            print("El valor es :",valor," De la posicion ", indice)            
        elif indice == 1:
            print("Posicion de <:", valor.find('<'))
            print("Posicion de <:", valor.find('>'))
            nombreAnimal = valor[valor.find('<') + 1 :valor.find('>')]
            print(nombreAnimal)
            print("Se creo el Pajaro: ",nombreAnimal)    


def proceso(arreglo):
    for indice,valor in enumerate(arreglo):
        print("Este es el arreglo:", valor," En la poscion: ",indice)
        gato = valor.find("Crear_Gato")
        pajaro = valor.find("Crear_Pajaro")
        if gato != -1:
            print("Se va crear gato")
            creaAnimalGato(valor)
        if pajaro != -1:
            print("Se va crear pajaro")
            creaAnimalPajaro(valor)

        
idGato = 1
contador = 1
def crearGato(nombre):
    gatoCrear = Gato(idGato,nombre,100,"Vivo")
    listaGato.append(gatoCrear)
    contador = contador + 1
    
    verGatos()
    
def verGatos():
    for valor in listaGato:
        print("Id:",valor.idGato," nombre:",valor.nombre)
        



