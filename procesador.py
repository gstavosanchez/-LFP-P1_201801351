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
    print("-----------Seleccionar Ruta---------------")
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
        conviene = valor.find("Conviene_Comer_Raton")
        enviar = valor.find("Enviar_Comer_Raton")
        comer = valor.find("Dar_de_Comer")
        if gato != -1:
            print("Se va crear gato")
            creaAnimalGato(valor)
        if pajaro != -1:
            print("Se va crear pajaro")
            creaAnimalPajaro(valor)
        if conviene !=-1:
            print("Conviene")
            convieneComer(valor)
        if enviar != -1:
            print("Enviar")
            enviarComer(valor)
        if comer != -1:
            print("comer")


        
def convieneComer(arreglo):
    comando = arreglo.split(",")
    posUno = comando[0]
    nombre = posUno[posUno.find('<') + 1 :posUno.find('>')]
    nombreGato = buscarGato(nombre)
    if nombreGato != None:
        print("Se encontro el gato:",nombreGato.getNombre())
        posDos = comando[1]
        posTres = comando[2]
        ejeX = posDos[posDos.find('<') + 1 :posDos.find('>')]
        ejeY = posTres[posTres.find('<') + 1 :posTres.find('>')]
        posCuatro = comando[3]
        pesoRaton = posCuatro[posCuatro.find('<') + 1 :posCuatro.find('>')]
        if isInteger(ejeX) and isInteger(ejeY) and isInteger(pesoRaton):
            gastarEnergia = int(ejeX) + int(ejeY)
            ganarEnergia = int(pesoRaton) + 12
            print("Energia a gastar es :",(gastarEnergia))
            print("Energia a ganar es: ",ganarEnergia)
            diferencia = ganarEnergia - gastarEnergia
            if  diferencia > 0:
                print("Ganara un total de energia: ",diferencia)
            elif diferencia == 0:
                print("No ganara pero tampoco perdera energia: ",diferencia)
            else:
                print("Perdera una energia de: ",diferencia)

    else:
        print("No se encotro el gato")

def enviarComer(arreglo):
    comando = arreglo.split(",")
    posUno = comando[0]
    nombre = posUno[posUno.find('<') + 1 :posUno.find('>')]
    nombreGato = buscarGato(nombre)
    if nombreGato != None:
        print("Se encontro el gato:",nombreGato.getNombre())
        posDos = comando[1]
        posTres = comando[2]
        ejeX = posDos[posDos.find('<') + 1 :posDos.find('>')]
        ejeY = posTres[posTres.find('<') + 1 :posTres.find('>')]
        posCuatro = comando[3]
        pesoRaton = posCuatro[posCuatro.find('<') + 1 :posCuatro.find('>')]
        if isInteger(ejeX) and isInteger(ejeY) and isInteger(pesoRaton):
            print("Energia actual: ",nombreGato.getEnergia())
            gastarEnergia = int(ejeX) + int(ejeY)
            ganarEnergia = int(pesoRaton) + 12
            diferencia = ganarEnergia - gastarEnergia
            total = nombreGato.getEnergia() + (diferencia)
            nombreGato.setEnergia(total)
            print("Se modifico la energia de: ",nombreGato.getNombre(),"la energia actualmete es: ", nombreGato.getEnergia())
            if  nombreGato.getEnergia() < 11 and nombreGato.getEnergia() > 0:
                print("Esto exhasuto. Dame de comer mi energia es:",nombreGato.getEnergia())
            elif nombreGato.getEnergia() > 10:
                print("Ya comiii, ahora mi energia es:", nombreGato.getEnergia())
            elif nombreGato.getEnergia() <= 0:
                nombreGato.setEnergia(0)
                nombreGato.setEstado("Muerto")
                print("Ya me mori :(")

           
    else:
        print("No se encotro el gato")

def crearGato(nombre):
    gatoCrear = Gato(nombre,50,"Vivo")
    listaGato.append(gatoCrear)
    
    
def verGatos():
    for valor in listaGato:
        print(" nombre:",valor.nombre)
        
def buscarGato(nombre):
    for valor in listaGato:
        if nombre == valor.getNombre():
            return valor
    


def isInteger(val):
    try:
        isinstance(int(val), int)
        return True
    except ValueError as error:
        return False