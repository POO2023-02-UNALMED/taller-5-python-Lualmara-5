from zooAnimales.animal import Animal

class Pez(Animal):

    _listado = []
    salmones = 0
    bacalaos = 0

    def __init__(self, nombre, edad, habitat, genero, colorEscamas, cantidadAletas):
        super().__init__(nombre, edad, habitat, genero)
        self._colorEscamas = colorEscamas
        self._cantidadAletas = cantidadAletas
        Pez._listado.append(self)
    
    def setColorEscamas(self, colorEscamas):
        self._colorEscamas = colorEscamas

    def getColorEscamas(self):
        return self._colorEscamas
    
    def setCantidadAletas(self, cantidadAletas):
        self._cantidadAletas = cantidadAletas
        
    def getCantidadAletas(self):
        return self._cantidadAletas
    
    @classmethod
    def crearSalmon(cls, nombre, edad, genero):
        salmon = cls(nombre, edad, "oceano", genero, "rojos", 6)
        cls.salmones += 1
        return salmon
    
    @classmethod
    def crearBacalao(cls, nombre, edad, genero):
        bacalao = cls(nombre, edad, "oceano", genero, "gris", 6)
        cls.bacalaos += 1
        return bacalao
    
    @staticmethod
    def cantidadPeces():
        return len(Pez._listado)