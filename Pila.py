import sys
import re

def main():
    print("LFP 2S2020 - Practica 1 ")

    while True:
        print(">> ", end="")

        entrada = input()

        if entrada.lower() == "exit":
            sys.exit()

        analizarComando(entrada.strip())


def analizarComando(entrada):
    comando = entrada.lower()

    if "solve" in comando:
        exp = comando.replace("solve", "")
        exp = exp.replace("[", "").replace("]", "")
        exp = exp.replace(" ", "")

        patron = "[0-9]*[.]?[0-9]+|[a-z]+[(][^)]+[)]"

        operandos = re.findall(patron, exp)
        operadores = re.sub(patron, "", exp)

            
        operar(operandos, operadores)

def anali(exp):
    
    exp = exp.replace(" ", "")

    patron = "[0-9]*[.]?[0-9]+|[a-z]+[(][^)]+[)]"

    operandos = re.findall(patron, exp)
    operadores = re.sub(patron, "", exp)

            
    operar(operandos, operadores)


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
        

    print(operandos[0])

main()
