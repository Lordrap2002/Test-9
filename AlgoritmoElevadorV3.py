from heapq import heappop, heappush

class Elevador:
    def __init__(self, id, pisoActual, sentido):
        self.id = id
        self.pisoActual = pisoActual
        self.altos, self.bajos = [], []
        self.sentido = sentido
    
    def agregarSolicitud(self, pisoNuevo):
        heappush((self.altos if (pisoNuevo > self.pisoActual or (pisoNuevo == self.pisoActual and self.sentido)) else self.bajos),
                (pisoNuevo if (pisoNuevo > self.pisoActual or (pisoNuevo == self.pisoActual and self.sentido)) else -pisoNuevo))
    
    def mover(self):
        movimiento = 0
        if(len(self.bajos) or len(self.altos)):
            if(self.sentido):
                if(len(self.altos)):
                    print("Elevador %d en piso %d" % (self.id, self.pisoActual))
                    if(self.pisoActual == self.altos[0]):
                        print("Elevador se detiene")
                        heappop(self.altos)
                    else:
                        print("Elevador %d subiendo" % (self.id))
                        self.pisoActual += 1
                    while(len(self.altos) and self.pisoActual == self.altos[0]):
                        heappop(self.altos)
                else:
                    self.sentido = 0
            else:
                if(len(self.bajos)):
                    print("Elevador %d en piso %d" % (self.id, self.pisoActual))
                    if(self.pisoActual == -self.bajos[0]):
                        print("Elevador se detiene")
                        heappop(self.bajos)
                    else:
                        print("Elevador %d bajando" % (self.id))
                        self.pisoActual -= 1
                    while(len(self.bajos) and self.pisoActual == -self.bajos[0]):
                        heappop(self.bajos)
                else:
                    self.sentido = 1
            movimiento += 1
        return movimiento

def verificarPiso(n):
    return (0 if n > 0 and n < 30 else 1)

def algoritmoElevador(arregloPisos, pisoActual1, pisoActual2):
    """
    Simula el movimiento de dos elevadores en un edificio en tiempo real.
    
    :param arregloPisos: lista de pisos a visitar
    :param pisoActual1: piso actual del elevador1
    :param pisoActual2: piso actual del elevador2
    """
    elevador1 = Elevador(pisoActual1, pisoActual1, 1)
    elevador2 = Elevador(pisoActual2, pisoActual2, 1)
    print("Elevador 1 en piso %d" % (pisoActual1))
    print("Elevador 2 en piso %d" % (pisoActual2))
    for p in arregloPisos:
        if abs(elevador1.pisoActual - p) < abs(elevador2.pisoActual - p):
            elevador1.agregarSolicitud(p)
        else:
            elevador2.agregarSolicitud(p)
    flag1, flag2 = elevador1.mover(), elevador2.mover()
    while(flag1 or flag2):
        nuevaSolicitud = int(input("Se va a ingresar una nueva solicitud? (Si: Ingrese 1, No: Ingrese 0): "))
        if(nuevaSolicitud):
            p = int(input("Ingrese el piso objetivo: "))
            while(verificarPiso(p)):
                p = int(input("Ese piso no existe.\nIngrese el piso objetivo: "))
            print("Piso ingresado %d" % (p))
            if abs(elevador1.pisoActual - p) < abs(elevador2.pisoActual - p):
                elevador1.agregarSolicitud(p)
            else:
                elevador2.agregarSolicitud(p)
        flag1, flag2 = elevador1.mover(), elevador2.mover()

def main():
    """
    Ejecución principal del algoritmo del elevador.
    
    Configura los parámetros iniciales del elevador y llama a la función algoritmoElevador.
    """
    arregloPisos = [5, 29, 13, 10]                          # Lista de pisos a visitar
    pisoInicial1 = 1                                        # Piso en el que se encuentra el elevador1 al inicio
    pisoInicial2 = 20                                       # Piso en el que se encuentra el elevador2 al inicio
    algoritmoElevador(arregloPisos, pisoInicial1, pisoInicial2)

if __name__ == "__main__":
    main()