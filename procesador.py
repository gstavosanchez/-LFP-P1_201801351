from io import open
import os
from Gato import *
import escribir

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
            crearPajaro(nombreAnimal)    


def proceso(arreglo):
    for indice,valor in enumerate(arreglo):
        print("Este es el arreglo:", valor," En la poscion: ",indice)
        gato = valor.find("Crear_Gato")
        pajaro = valor.find("Crear_Pajaro")
        conviene = valor.find("Conviene_Comer_Raton")
        enviar = valor.find("Enviar_Comer_Raton")
        comer = valor.find("Dar_de_Comer")
        resumenPersonal = valor.find("Resumen_Mascota")
        enviarMensaje = valor.find("Puede_Entregar_Mensaje")
        siEnviarMensaje = valor.find("Enviar_Mensaje")
        res = valor.find("Resumen_Global")
        if gato != -1:
            print("Se va crear gato")
            creaAnimalGato(valor)
        elif pajaro != -1:
            print("Se va crear pajaro")
            creaAnimalPajaro(valor)
        elif conviene !=-1:
            print("Conviene")
            convieneComer(valor)
        elif enviar != -1:
            print("Enviar")
            enviarComer(valor)
        elif comer != -1:
            print("comer")
            darComer(valor)
        elif resumenPersonal != -1:
            print ("Resumen Personal")
            resumen(valor)
        elif enviarMensaje != -1:
            print ("Entregar Mensaje")
            puedeEntregar(valor)
        elif siEnviarMensaje != -1:
            print("Enviar mensaje")
            enviarMensajePajaro(valor)
        elif res != -1:
            print("Resumen Global")
            resumenGlobal()
        else:
            print("Comando incorrecto")




        
def convieneComer(arreglo):
    comando = arreglo.split(",")
    posUno = comando[0]
    nombre = posUno[posUno.find('<') + 1 :posUno.find('>')]
    nombreGato = buscarGato(nombre)
    if nombreGato != None and nombreGato.getTipo() == "Gato":
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
            if nombreGato.getEnergia() == 0:
                nombreGato.setEstado("Muerto")
                text = f"{nombre}, Ya me mori."
                escribir.imprimirConviene(text)
            else :
                if  diferencia > 0:
                    print("Ganara un total de energia: ",diferencia)
                    text = f"{nombre}, Si me conviene comer el raton."
                    print(text)
                    escribir.imprimirConviene(text)
                elif diferencia == 0:
                    print("No ganara pero tampoco perdera energia: ",diferencia)
                else:
                    print("Perdera una energia de: ",diferencia)
                    text = f"{nombre}, Esta muy lejos.No me conviene"
                    print(text)
                    escribir.imprimirConviene(text)
                    

    else:
        print("No se encotro el gato")

def puedeEntregar(arreglo):
    comando = arreglo.split(",")
    posUno = comando[0]
    nombre = posUno[posUno.find('<') + 1 :posUno.find('>')]
    print(f"{nombre}")
    pajaro = buscarGato(nombre)
    if pajaro != None and pajaro.getTipo() == "Pajaro":
        posDos = comando[1]
        posTres = comando[2]
        ejeX = posDos[posDos.find('<') + 1 :posDos.find('>')]
        ejeY = posTres[posTres.find('<') + 1 :posTres.find('>')]
        
        if isInteger(ejeX) and  isInteger(ejeY):
            gastarEnergia = ((int(ejeX) + int(ejeY)) / 100) + 10
            if (pajaro.getEnergia() - gastarEnergia) <= 15:
                    total = int(ejeX) + int(ejeY)
                    texto = f"{nombre}, Estoy exhausto.Dame de comer {total} para ir."
                    escribir.imprimirConviene(texto)
            elif (pajaro.getEnergia() - gastarEnergia) >= 16:
                texto = f"{nombre}, Si puedo ir a dejar el mensaje."
                escribir.imprimirConviene(texto)
            elif pajaro.getEnergia() <= 0 : 
                texto = f"{nombre}, Ya me mori.  :("
                escribir.imprimirConviene(texto)
        else:
            print("No se puede reconcer las cordenas")
            
def enviarMensajePajaro(arreglo):
    comando = arreglo.split(",")
    posUno = comando[0]
    nombre = posUno[posUno.find('<') + 1 :posUno.find('>')]
    print(f"{nombre}")
    pajaro = buscarGato(nombre)
    if pajaro != None and pajaro.getTipo() == "Pajaro":
        posDos = comando[1]
        posTres = comando[2]
        ejeX = posDos[posDos.find('<') + 1 :posDos.find('>')]
        ejeY = posTres[posTres.find('<') + 1 :posTres.find('>')]
        if isInteger(ejeX) and  isInteger(ejeY):
            pajaro.setEjeX(int(ejeX))
            pajaro.setEjeY(int(ejeY))
            gastarEnergia = ((int(ejeX) + int(ejeY)) / 100) + 10    
            if (pajaro.getEnergia() - gastarEnergia) <= 15 :
                    total = int(ejeX) + int(ejeY)
                    texto = f"{nombre}, Estoy exhausto.Dame de comer {total} para ir."
                    pajaro.setEnergia((pajaro.getEnergia()+ total))
                    escribir.imprimirConviene(texto)
            elif (pajaro.getEnergia() - gastarEnergia) >= 16:
                texto = f"{nombre}, Ya me fui a dejar el mensaje a ({ejeX},{ejeY})"
                pajaro.setEnergia((pajaro.getEnergia() - gastarEnergia))
                escribir.imprimirConviene(texto)
            elif pajaro.getEnergia() <= 0 : 
                texto = f"{nombre}, Ya me mori.  :("
                pajaro.setEstado("Muerto")
                pajaro.setEnergia(0)
                escribir.imprimirConviene(texto)
        else:
            print("No se puede reconcer las cordenas")

def resumenGlobal():
    titulo = "---------------------Resumen Global---------------------"
    escribir.imprimirConviene(titulo)
    for valor in listaGato:
        nombre = valor.getNombre()
        energia = valor.getEnergia()
        ejeX = valor.getEjeX()
        ejeY = valor.getEjeY()
        tipo = valor.getTipo()
        estado = valor.getEstado()
        text = f"{nombre}, Energia: {energia}, X:{ejeX}, Y:{ejeY}, {tipo}, {estado}"
        escribir.imprimirConviene(text)



def enviarComer(arreglo):
    comando = arreglo.split(",")
    posUno = comando[0]
    nombre = posUno[posUno.find('<') + 1 :posUno.find('>')]
    nombreGato = buscarGato(nombre)
    if nombreGato != None and nombreGato.getTipo() == "Gato":
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
            nombreGato.setEjeX(int(ejeX))
            nombreGato.setEjeY(int(ejeY))
            print("Se modifico la energia de: ",nombreGato.getNombre(),"la energia actualmete es: ", nombreGato.getEnergia())
            if  nombreGato.getEnergia() < 11 and nombreGato.getEnergia() > 0:
                print("Esto exhasuto. Dame de comer mi energia es:",nombreGato.getEnergia())
                tex = f"{nombre}, Estoy exhausto.Dame de comer 20 gramos para ir"
                escribir.imprimirConviene(tex)
            elif nombreGato.getEnergia() > 10:
                print("Ya comiii, ahora mi energia es:", nombreGato.getEnergia())
                energi = nombreGato.getEnergia()
                tex = f"{nombre}, Ya me comi al  raton, ahora mi energia es {energi}." 
                escribir.imprimirConviene(tex)
            elif nombreGato.getEnergia() <= 0:
                nombreGato.setEnergia(0)
                nombreGato.setEstado("Muerto")
                print("Ya me mori :(")
                tex = f"{nombre}, Ya me mori."
                escribir.imprimirConviene(tex) 
    
    else:
        print("No se encotro el gato")

def darComer(arreglo):
    comado = arreglo.split(",")
    posUno = comado[0]
    nombre = posUno[posUno.find('<') + 1 :posUno.find('>')]
    gato = buscarGato(nombre)
    if gato != None and gato.getTipo() == "Gato":
        posDos = comado[1]
        pesoRato = posDos[posDos.find('<') + 1 :posDos.find('>')]
        comida = int(pesoRato) + 12
        if  gato.getEstado() == "Muerto":
            print("Muy tarde estoy muerto")
            tex = f"{nombre}, Muy tarde. Ya me mori." 
            escribir.imprimirConviene(tex)
        else:
            energia = comida + gato.getEnergia()
            gato.setEnergia(energia)
            print("Gracias ahora mi energia es :", gato.getEnergia())
            tex = f"{nombre}, Gracias. Ahora mi energia es {energia}" 
            escribir.imprimirConviene(tex)
    elif gato != None and gato.getTipo() == "Pajaro":
        posDos = comado[1]
        pesoRato = posDos[posDos.find('<') + 1 :posDos.find('>')]
        comida = int(pesoRato) + 12
        if  gato.getEstado() == "Muerto":
            print("Muy tarde estoy muerto")
            tex = f"{nombre}, Muy tarde. Ya me mori." 
            escribir.imprimirConviene(tex)
        else:
            energia = comida + gato.getEnergia()
            gato.setEnergia(energia)
            print("Gracias ahora mi energia es :", gato.getEnergia())
            tex = f"{nombre}, Gracias. Ahora mi energia es {energia}" 
            escribir.imprimirConviene(tex)


    

def crearGato(nombre):
    gatoExiste = buscarGato(nombre)
    if gatoExiste == None or (nombre == gatoExiste.getNombre() and gatoExiste.getTipo() != "Gato"):
        gatoCrear = Gato(nombre,50,"Vivo","Gato",0,0)
        listaGato.append(gatoCrear)
        escribir.imprimirCrearGato(gatoCrear)
    else:
        print("Ya existe el gato")

def crearPajaro(nombre):
    pajaro = buscarGato(nombre)
    if pajaro == None or (nombre == pajaro.getNombre() and pajaro.getTipo() != "Pajaro"):
        nuevoPajaro = Gato(nombre,50,"Vivo","Pajaro",0,0)
        listaGato.append(nuevoPajaro)
        text = f"Se creo el pajaro {nombre}"
        escribir.imprimirConviene(text)


def resumen(arreglo):
    comando = arreglo.split(":")
    porDos = comando[1]
    nombre = porDos[porDos.find('<') + 1 :porDos.find('>')]
    gato = buscarGato(nombre)
    if gato != None and gato.getTipo()== "Gato":
        print("Imprimir resumen del gato")
        energia = gato.getEnergia()
        ejeX = gato.getEjeX()
        ejeY = gato.getEjeY()
        estado = gato.getEstado()
        tipo = gato.getTipo()
        text = f"{nombre}, Energia: {energia}, X:{ejeX}, Y:{ejeY}, {tipo}, {estado}"
        escribir.imprimirConviene(text)
    elif gato != None and gato.getTipo()== "Pajaro":
        print("Imprimir resumen del Pajaro")
        energia = gato.getEnergia()
        ejeX = gato.getEjeX()
        ejeY = gato.getEjeY()
        estado = gato.getEstado()
        tipo = gato.getTipo()
        text = f"{nombre}, Energia: {energia}, X:{ejeX}, Y:{ejeY}, {tipo}, {estado}"
        escribir.imprimirConviene(text)

    
    
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