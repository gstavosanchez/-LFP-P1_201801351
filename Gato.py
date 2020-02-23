
class Gato():
    idGato = 0
    nombre = ""
    energia = 0
    estado = ""
    def __init__(self,idGato,nombre,energia,estado):
        self.idGato = idGato
        self.nombre = nombre
        self.energia = energia
        self.estado = estado
    
    def getIdGato(self):
        return self.idGato
    def getNombre(self):
        return self.nombre
    def getEnergia(self):
        return self.energia
    def getEstado(self):
        return self.estado
    
    def setIdGato(self,idGato):
        self.idGato = idGato
    def setNombre(self,nombre):
        self.nombre = nombre
    def setEnergia(self,energia):
        self.energia = energia
    def setEstado(self,estado):
        self.estado = estado
