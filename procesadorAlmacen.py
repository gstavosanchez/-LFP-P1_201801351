from io import open
import os
import time
import modulos
import ManejadorAlmacen

def getRuta():
    print("-----------Seleccionar Ruta de Almacen---------------")
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
        rutaAbs = f"{ruta}\{arch}.almacen"
        return rutaAbs
    elif opcion == "2":
        directorioActual = os.getcwd()
        print("Escriba el nombre del archivo")
        nombre = input()
        nombre = nombre.strip()
        rutaAbsoluta = f"{directorioActual}\{nombre}.almacen"
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
        procesadorComando(texto)
    except (FileNotFoundError, IOError):
        print("Error en la lectura")
        getRuta()

def imprimirTexto(texto):
    archivo  = open("archivo.almacen_result","a")
    hora = time.strftime("%H:%M:%S")
    fecha =  time.strftime("%d/%m/%y")
    fechaHora = f"[{fecha} {hora}]"
    tex = f"{fechaHora} {texto} \n"
    archivo.writelines(tex)
    archivo.close()


def procesadorComando(arreglo):
    for indice,valor in enumerate(arreglo):
        if valor.find("Declarar") == 0:
            setDeclarar(valor)
        elif valor.find("Concatenar") == 0:
            pass
        elif valor.find("Posicion_cadena") == 0:
            setPosicionCadena(valor)
        elif valor.find("Tamanio") == 0:
            setTamanioCadena(valor)
        elif valor.find("Imprimir") == 0:
            setImprimirLetras(valor)
        elif valor.find("Generar_grafo") == 0:
            pass
    


def setDeclarar(arreglo):
    particion = arreglo.split(":")
    parametros = particion[1].split(",")
    nombreVariable = parametros[0]
    valorVariable = parametros[1]
    nombreVariable = nombreVariable.strip()
    valorVariable = valorVariable.replace('"',"")
    valorVariable = valorVariable.strip()
    ManejadorAlmacen.crearVariable(nombreVariable,valorVariable)
    
def setPosicionCadena(arreglo):
    particion = arreglo.split(":")
    parametros = particion[1]
    parametros = parametros.strip()
    ManejadorAlmacen.getPosicion(parametros)

def setTamanioCadena(arreglo):
    particion = arreglo.split(":")
    parametros = particion[1]
    parametros = parametros.strip()
    ManejadorAlmacen.getTamanio(parametros)

def setImprimirLetras(arreglo):
    particion = arreglo.split(":")
    parametros = particion[1]
    parametros = parametros.strip()
    ManejadorAlmacen.imprimirLetra(parametros)





