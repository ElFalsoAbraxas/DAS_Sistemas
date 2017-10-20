class Videojuego:
    
    def __init__(self, nombre, genero):
        self._nombre = nombre
        self._genero = genero

    def getGenero(self):
        return self._genero

    def setGenero(self, genero):
        self._genero = genero

    def getNombre(self):
        return self._nombre

class Prueba(Videojuego):

    def __init__(self, nombre, genero, company):
        super().__init__(nombre, genero)
        self._company = company

    def getDescripcion(self):
        return self.getNombre() + self._company + " de genero " + self.getGenero()


if __name__ == '__main__':
    
    x = Prueba(" The legend of zelda OoT ", " Aventuras " , " Nintendo ")
    print(x.getDescripcion())

