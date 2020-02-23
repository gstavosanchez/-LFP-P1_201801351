
class Gato():
    nombre = ""
    energia = 0
    estado = ""
    def __init__(self,nombre,energia,estado):
        self.nombre = nombre
        self.energia = energia
        self.estado = estado
    
    def getNombre(self):
        return self.nombre
    def getEnergia(self):
        return self.energia
    def getEstado(self):
        return self.estado
    

    def setNombre(self,nombre):
        self.nombre = nombre
    def setEnergia(self,energia):
        self.energia = energia
    def setEstado(self,estado):
        self.estado = estado
