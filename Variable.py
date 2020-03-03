class Varibale():
    nombre =  ""
    valor = ""

    def __init__(self,nombre,valor):
        self.nombre = nombre
        self.valor = valor

    def getNombre(self):
        return self.nombre
    def getValor(self):
        return self.valor
    def setNombre(self,nombre):
        self.nombre = nombre
    def setValor(self,valor):
        self.valor = valor
    