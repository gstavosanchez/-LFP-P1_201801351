import sys
import re
from Variable import *
import procesadorCalcu


listaVariable = []

def nuevaVarible(nombre,valor):
    varExiste = buscarVariable(nombre)
    if varExiste == None:
        arreglo = valor.split(" ")
        print("Este es el arreglo: ", arreglo)
        for val in arreglo:
            buscado = buscarVariable(val.strip())
            if buscado != None:
                print("Buscado:", buscado.getValor())
                valor = valor.replace(val,str(buscado.getValor()).strip())
                valor = int(analizar(valor))
                
    if varExiste == None:
        nuevaVariable = Varibale(nombre,valor)
        listaVariable.append(nuevaVariable)
        verDatos()

def analizar(arreglo):
    print("Arreglo: ",arreglo)
    array = arreglo.split(" ")
    for i in range(len(array)):
        arreglo = arreglo.replace("  "," ")
        if array[i]== "*":
            total = int(array[i - 1]) * int(array[i + 1])
            arreglo = arreglo.replace((array[i - 1]),str(total))
            arreglo = arreglo.replace((array[i]),"")
            arreglo = arreglo.replace((array[i + 1]),"")
            arreglo = arreglo.replace("  "," ")
            print(arreglo)
        elif array[i]== "/":
            total = int(array[i - 1]) * int(array[i + 1])
            arreglo = arreglo.replace((array[i - 1]),str(total))
            arreglo = arreglo.replace((array[i]),"")
            arreglo = arreglo.replace((array[i + 1]),"")
            arreglo = arreglo.replace("  "," ")
        elif array[i] == "*" and array[i + 2] == "/" or array[i] == "/" and array[i + 2] == "*":
            return extrar(arreglo.strip())
        else:
            return extrar(arreglo.strip())
    print("Nuevo Arreglo:", arreglo)
    for i in range(len(arreglo)):
        arreglo = arreglo.replace("  "," ")
    print("-->:",arreglo)
    
    totales = extrar(arreglo.strip())
    print(totales)
    return totales


def extrar(exp):
    exp = exp.replace(" ", "")
    exp = exp.replace("  ", "")
    exp = exp.strip()
    patron = "[0-9]*[.]?[0-9]+|[a-z]+[(][^)]+[)]"
    operandos = re.findall(patron, exp)
    operadores = re.sub(patron, "", exp)
    total = operar(operandos, operadores)
    return total

def operar(operandos, operadores):
    
    print(operandos)
    print(operadores)

    for operador in operadores:

        op1 = float(str(operandos.pop(0)))
        op2 = float(str(operandos.pop(0)))

        if operador == '+':
            operandos.insert(0, op1 + op2)
        elif operador == '-':
            operandos.insert(0, op1 - op2)
        elif operador == '*':
            operandos.insert(0, op1 * op2)
        elif operador == '/':
            operandos.insert(0, op1 / op2)

    print(operandos[0])
    return operandos[0]




def buscarVariable(nombre):
    for valor in listaVariable:
        if nombre == valor.getNombre():
            return valor
    

def verDatos():
    for valor in listaVariable:
        print("Variable: ",valor.getNombre()," Expresion: ",valor.getValor())

def separar(arreglo):
    array = arreglo.split(" ")
    setPostifijo(array)

def setPostifijo(array):
    contador = 0
    bandera = False
    while bandera == False:
        bandera = True
    for i in range(len(array)-1):
        if (array[i] == "*") and isInteger((array[i + 1])) == True or ((array[i] == "/") and isInteger((array[i + 1])) == True):
            contador = i
            aux = array[contador]
            array[contador] = array[contador + 1]
            array[contador + 1] = aux
            print("Valor de i:",i)
            bandera = False
        elif(array[i] == "+") and isInteger((array[i + 1])) == True or ((array[i] == "-") and isInteger((array[i + 1])) == True):
            contador = i
            aux = array[contador]
            array[contador] = array[contador + 1]
            array[contador + 1] = aux
            print("Valor de i:",i)
            bandera = False
        print("valor de i a fuera del if: ",i)
        i = 0
    print(array)
    cont = 0
     
    for y in range(len(array) - 1):
        if((array[y] == "+") and isInteger((array[y + 1] ))== True and isInteger(array[y + 2]) != True) or ((array[y] == "-") and isInteger((array[y + 1] )) == True and isInteger(array[y + 2]) != True):
            cont = y
            temp = array[cont]
            array[cont] = array[cont + 1]
            array[cont + 1] = temp
    print(array)
    
    co = 0   
    for x in range(len(array) - 1):
        if ((array[x] ) == "+" and (array[x + 1] ) == "*") or ((array[x] ) == "-" and (array[x + 1] ) == "*") or ((array[x] ) == "+" and (array[x + 1] ) == "/") or ((array[x] ) == "-" and (array[x + 1] ) == "/"):
            co = x
            tem = array[co]
            array[co] = array[co + 1]
            array[co + 1] = tem
    print(array)
    tex = ""
    for j in range(len(array)):
        tex += f"{array[j]} "
    texto = f"Postifijo:{tex}"
    procesadorCalcu.imprimirTexto(texto)
    
        

def isInteger(val):
    try:
        isinstance(int(val), int)
        return True
    except ValueError as error:
        return False



def incrementar(nombre):
    nombre = nombre.strip()
    buscado = buscarVariable(nombre)
    if buscado != None:
        if isInteger(buscado.getValor()) == True:
            incre = int(buscado.getValor()) + 1
            buscado.setValor(incre)
            print("Se modficio:",buscado.getNombre()," ",buscado.getValor())
        else:
            va = buscado.getValor()
            con = f"({va})+ 1"
            buscado.setValor(con)
            print("Se modficio:",buscado.getNombre()," ",buscado.getValor())

    print("Datos Actuales:",buscado.getNombre()," ",buscado.getValor())
    

def mitad(nombre):
    nombre = nombre.strip()
    buscado = buscarVariable(nombre)
    if buscado != None:
        if isInteger(buscado.getValor()) == True:
            incre = int(buscado.getValor()) / 2
            buscado.setValor(incre)
            print("Se modficio:",buscado.getNombre()," ",buscado.getValor())
        else:
            va = buscado.getValor()
            con = f"({va})/ 2"
            buscado.setValor(con)
            print("Se modficio:",buscado.getNombre()," ",buscado.getValor())

    print("Datos Actuales:",buscado.getNombre()," ",buscado.getValor())



def triple(nombre):
    nombre = nombre.strip()
    buscado = buscarVariable(nombre)
    if buscado != None:
        if isInteger(buscado.getValor()) == True:
            incre = int(buscado.getValor()) * 3
            buscado.setValor(incre)
            print("Se modficio:",buscado.getNombre()," ",buscado.getValor())
        else:
            va = buscado.getValor()
            con = f"({va}) * 3"
            buscado.setValor(con)
            print("Se modficio:",buscado.getNombre()," ",buscado.getValor())

    print("Datos Actuales:",buscado.getNombre()," ",buscado.getValor())




def postivo(nombre):
    nombre = nombre.strip()
    buscado = buscarVariable(nombre)
    if buscado != None:
        if isInteger(buscado.getValor()) == True:
            if int(buscado.getValor()) < 0:
                incre = int(buscado.getValor()) * (-1)
                buscado.setValor(incre)
                print("Se modficio:",buscado.getNombre()," ",buscado.getValor())
            else:
                incre = int(buscado.getValor()) * (1)
                buscado.setValor(incre)
                print("Se modficio:",buscado.getNombre()," ",buscado.getValor())
        else:
            va = buscado.getValor()
            con = f"({va}) * 1"
            buscado.setValor(con)
            print("Se modficio:",buscado.getNombre()," ",buscado.getValor())

    print("Datos Actuales:",buscado.getNombre()," ",buscado.getValor())


def negativo(nombre):
    nombre = nombre.strip()
    buscado = buscarVariable(nombre)
    if buscado != None:
        if isInteger(buscado.getValor()) == True:
            if int(buscado.getValor()) > 0:
                incre = int(buscado.getValor()) * (-1)
                buscado.setValor(incre)
                print("Se modficio:",buscado.getNombre()," ",buscado.getValor())
            else:
                incre = int(buscado.getValor()) * (-1)
                buscado.setValor(incre)
                print("Se modficio:",buscado.getNombre()," ",buscado.getValor())
        else:
            va = buscado.getValor()
            con = f"({va}) * -1"
            buscado.setValor(con)
            print("Se modficio:",buscado.getNombre()," ",buscado.getValor())

    print("Datos Actuales:",buscado.getNombre()," ",buscado.getValor())

def potencia(base,exponente):
    if isInteger(base) == True and isInteger(exponente) == True:
        base = int(base)
        exponente = int(exponente)
        total = pow(base,exponente)
        print(total)
        texto = f"Potencia: {total}"
        procesadorCalcu.imprimirTexto(texto)
    elif isInteger(base) == False and isInteger(exponente) == True:
        base = buscarEnCararter(base)
        exponente = int(exponente)
        total = pow(base,exponente)
        print(total)
        texto = f"Potencia: {total}"
        procesadorCalcu.imprimirTexto(texto)
    elif isInteger(base) == True and isInteger(exponente) == False:
        base = int(base)
        exponente = buscarEnCararter(exponente)
        total = pow(base,exponente)
        print(total)
        texto = f"Potencia: {total}"
        procesadorCalcu.imprimirTexto(texto)
    elif isInteger(base) == False and isInteger(exponente) == False:
        base = buscarEnCararter(base)
        exponente = buscarEnCararter(exponente)
        total = pow(base,exponente)
        print(total)
        texto = f"Potencia: {total}"
        procesadorCalcu.imprimirTexto(texto)
    else:
        print("No se puede realizar la operacion")    

def buscarEnCararter(arreglo):
    arreglo = arreglo.strip()
    array = arreglo.split(" ")
    for valor in array:
        buscado = buscarVariable(valor)
        if buscado != None:
            arreglo = arreglo.replace(valor,str(buscado.getValor()).strip())
    arreglo = arreglo.strip()
    total = extrar(arreglo)
    total = int(total)
    return total
    

def imprimirVariable(nombre):
    nombre = nombre.strip()
    variable = buscarVariable(nombre)
    if variable != None:
        texto = variable.getValor()
        procesadorCalcu.imprimirTexto(texto)


def imprimirMensaje(texto):
    texto = texto.strip()
    texto = texto.replace('"',"")
    texto = texto.replace('"',"")
    procesadorCalcu.imprimirTexto(texto)