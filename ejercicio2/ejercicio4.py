class Bus:
    def __init__(self, placa="", capacidad=0, pasajeros=0):
        self.placa = placa
        self._capacidad = capacidad
        self._pasajeros = pasajeros
        self._costoPasaje = 1.50

    def __str__(self):
        return f"Bus: {self.placa}, Capacidad: {self._capacidad}, Pasajeros: {self._pasajeros}"

    # a) Metod para 1ue los pasajeros suban 
    def subirPasajeros(self, cantidad):
        if self._pasajeros + cantidad <= self._capacidad:
            self._pasajeros += cantidad
        else:
            print("No hay suficientes asientos disponibles")

    # b) metodo para cobrar pasaje
    def cobrarPasaje(self):
        total = self._pasajeros * self._costoPasaje
        return total

    # c) metod para ver cuantos asienyos quedan disponibles
    def asientosDisponibles(self):
        return self._capacidad - self._pasajeros

    # Getters
    def getPlaca(self):
        return self.placa

    def getCapacidad(self):
        return self._capacidad

    def getPasajeros(self):
        return self._pasajeros

    # Setters
    def setPlaca(self, nuevo):
        self.placa = nuevo

    def setCapacidad(self, nuevo):
        self._capacidad = nuevo

    def setPasajeros(self, nuevo):
        self._pasajeros = nuevo


# Bloque principal
class Main():
    bus1 = Bus("1234-ABC", 14, 3)
    bus2 = Bus("5678-DFG", 40, 20)

    print("--- Buses ---")
    print(bus1)
    print(bus2)

    print("...Subiendo pasajeros al bus1...")
    bus1.subirPasajeros(10)

    print("Pasaje recaudado bus1:", bus1.cobrarPasaje(), "Bs")
    print("Asientos disponibles bus1:", bus1.asientosDisponibles())

    print("...Subiendo pasajeros al bus2...")
    bus2.subirPasajeros(4)

    print("Pasaje recaudado bus2:", bus2.cobrarPasaje(), "Bs")
    print("Asientos disponibles bus2:", bus2.asientosDisponibles())