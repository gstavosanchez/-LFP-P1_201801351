
class Gato():
    nombre = ""
    energia = 0
    estado = ""
    tipo = ""
    ejeX = 0
    ejeY = 0
    def __init__(self,nombre,energia,estado,tipo,ejeX,ejeY):
        self.nombre = nombre
        self.energia = energia
        self.estado = estado
        self.tipo = tipo
        self.ejeX = ejeX
        self.ejeY = ejeY
    
    def getNombre(self):
        return self.nombre
    def getEnergia(self):
        return self.energia
    def getEstado(self):
        return self.estado

    def getEjeX(self):
        return self.ejeX
    
    def getEjeY(self):
        return self.ejeY

    def getTipo(self):
        return self.tipo

    def setNombre(self,nombre):
        self.nombre = nombre
    def setEnergia(self,energia):
        self.energia = energia
    def setEstado(self,estado):
        self.estado = estado
    def setEjeX(self,ejeX):
        self.ejeX = ejeX
    def setEjeY(self,ejeY):
        self.ejeY = ejeY

    def setTipo(self,tipo):
        self.tipo = tipo
