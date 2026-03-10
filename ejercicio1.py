class Anime:
    def __init__(self, nombre="", genero="", nroEpisodios=0,episodios=""):
        self.nombre = nombre
        self.genero = genero
        self._nroEpisodios = nroEpisodios
        self._episodios = []
       

class Televisor:
    def __init__(self, marca="", resolucion=0, tipo=""):
        self._marca = marca
        self._resolucion = resolucion
        self._tipo = tipo

    def __str__(self):
        return f"TV: {self._marca}, Resolucion: {self._resolucion},Tipo{self._tipo}"

class Instrumento:
    def __init__(self, nombre="", material="", tipo=""):
        self.nombre = nombre
        self._material = material
        self._tipo = tipo

    def __str__(self):
        return f"Nombre: {self.nombre},Materia:{self._material},Tipi:{self._tipo})"
    
    def getNombre(self):
        return self.nombre
    def getMaterial(self):
        return self._material
    def getTipo(self):
        return self._tipo
    
    def setNombre(self,nuevo):
        self.nombre=nuevo
    
    def setMaterial(self,nuevo):
        self._material=nuevo
    
    def setTipo(self,nuevo):
        self._tipo=nuevo
   


# Bloque principal
class Main ():
    anime1 = Anime("One Piece", "Shonen", 1100)
    anime2 = Anime("Evangelion", "Mecha", 26)

    tv1 = Televisor("Samsung", 4, "OLED")
    tv2 = Televisor("LG", 2, "IPS")

    inst1 = Instrumento("Guitarra", "Madera", "Cuerda")
    inst2 = Instrumento("Flauta", "Metal", "Aire")

    print("--- Anime ---")
    print(anime1)
    print(anime2)

    print("--- Televisores ---")
    print(tv1)
    print(tv2)

    print("\n--- Instrumentos ---")
    print(inst1)
    print(inst2)