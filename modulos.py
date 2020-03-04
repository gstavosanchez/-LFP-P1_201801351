import procesador
import procesadorCalcu
import procesadorAlmacen
def menuPrinpal():
    while True:
        print("-----------Menu Principal---------------")
        print("1) Menu Entretenimiento")
        print("2) Menu Educacion")
        print("Presione SALIR si lo desea")
        print("Seleccione una opcion:")
        opcion = input()
        print(f"Usted selecciono: {opcion} ")
        if opcion == "1":
            menuEntretimineto()
        elif opcion == "2":
          menuEducacion()
        else:
            if opcion != "SALIR":
                print("Opcion Incorrecta")
        
        if opcion == "SALIR":
            break 


def menuEntretimineto():
    while True:
        print("-----------Menu Entretenimiento---------------")
        print("1) Cargar Archivo")
        print("2) Menu Principal")
        print("Presione SALIR si lo desea")
        print("Seleccione una opcion:")
        opcion = input()
        print(f"Usted selecciono: {opcion} ")
        if opcion == "1":
            ruta = procesador.obetenerRuta()   
            arreglo= procesador.leerArchivo(ruta)
        elif opcion == "2":
           menuPrinpal()
        else:
            if opcion != "SALIR":
                print("Opcion Incorrecta")
        
        if opcion == "SALIR":
            break 


def menuEducacion():
    while True:
        print("-----------Menu Educacion---------------")
        print("1) Educacion Calculadora")
        print("2) Almacen de Caracteres")
        print("3) Menu Principal")
        print("Presione SALIR si lo desea")
        print("Seleccione una opcion:")
        opcion = input()
        print(f"Usted selecciono: {opcion} ")
        if opcion == "1":
            ruta = procesadorCalcu.getRuta()
            procesadorCalcu.leerArchivo(ruta)
        elif opcion == "2":
            ruta = procesadorAlmacen.getRuta()
            procesadorAlmacen.leerArchivo(ruta)
        elif opcion == "3":
            menuPrinpal()
        else:
            if opcion != "SALIR":
                print("Opcion Incorrecta")
        
        if opcion == "SALIR":
            break 


