# clase 1 
class Jugador:
    def __init__(self, nombre="", diamantes=0):
        self.nombre = nombre
        self._diamantes = diamantes

    def __str__(self):
        return f"Jugador: {self.nombre}, Diamantes: {self._diamantes}"

    def getNombre(self):
        return self.nombre

    def getDiamantes(self):
        return self._diamantes

#clase 2
class ServidorMinecraft:
    def __init__(self, nombre="", capacidad=10):
        self.nombre = nombre
        self._capacidad = capacidad
        self._jugadores = []

    def __str__(self):
        return f"Servidor: {self.nombre}, Jugadores conectados: {len(self._jugadores)}"

    # a) Con este metodo agragamos los jugadores
    def agregarJugador(self, jugador):
        if len(self._jugadores) < self._capacidad:
            self._jugadores.append(jugador)
            print("Jugador agregado:", jugador.getNombre())
        else:
            print("El servidor está lleno")

    # b) con este metodo se muestra los staks
    def stacksDiamantes(self):
        for j in self._jugadores:
            stacks = j.getDiamantes() // 64
            print(f"{j.getNombre()} tiene {stacks} stack(s) de diamantes")

    # c) este metodo muestra al jugador que tiene mas diamntes 
    def jugadorMasDiamantes(self):
        mayor = self._jugadores[0]
        for j in self._jugadores:
            if j.getDiamantes() > mayor.getDiamantes():
                mayor = j
        print("Jugador con más diamantes:", mayor.getNombre())

    # d) este muestra la canrtidad de diamnate sque hay en el juego
    def totalDiamantes(self):
        total = 0
        for j in self._jugadores:
            total += j.getDiamantes()
        print("Total de diamantes en el servidor:", total)



class Main():
    j1 = Jugador("Steve", 120)
    j2 = Jugador("Alex", 65)
    j3 = Jugador("Herobrine", 300)

    servidor = ServidorMinecraft("Tortilla Land")

    servidor.agregarJugador(j1)
    servidor.agregarJugador(j2)
    servidor.agregarJugador(j3)

    print("--- Jugadores ---")
    print(j1)
    print(j2)
    print(j3)

    print("--- Stacks de diamantes ---")
    servidor.stacksDiamantes()

    print("--- Jugador con más diamantes ---")
    servidor.jugadorMasDiamantes()

    print("--- Total de diamantes ---")
    servidor.totalDiamantes()