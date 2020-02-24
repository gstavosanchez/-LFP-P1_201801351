from io import open
import time






def imprimirCrearGato(gato):
    archivo  = open("archivo.mascotas_result","a")
    hora = time.strftime("%H:%M:%S")
    fecha =  time.strftime("%d/%m/%y")
    fechaHora = f"[{fecha} {hora}]"
    cat = gato.getNombre()
    texto = f"{fechaHora} Se creo el gato {cat} \n"
    archivo.writelines(texto)
    archivo.close()
    

def imprimirConviene(texto):
    archivo  = open("archivo.mascotas_result","a")
    hora = time.strftime("%H:%M:%S")
    fecha =  time.strftime("%d/%m/%y")
    fechaHora = f"[{fecha} {hora}]"
    tex = f"{fechaHora} {texto} \n"
    archivo.writelines(tex)
    archivo.close()
    




