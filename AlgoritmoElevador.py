from heapq import heappop, heappush

def algoritmoElevador(arregloPisos, pisoActual, mapaPisos, sentido):
    """
    Simula el movimiento de un elevador en un edificio.
    
    :param arregloPisos: lista de pisos a visitar
    :param pisoActual: piso actual del elevador
    :param mapaPisos: diccionario de pisos con nuevos destinos
    :param sentido: dirección del elevador (1: subiendo, 0: descendiendo)
    """
    altos, bajos = [], []  # Colas para pisos encima y debajo de mi piso actual
    for p in arregloPisos:
        heappush((altos if (p > pisoActual or (p == pisoActual and sentido)) else bajos),
                 (p if (p > pisoActual or (p == pisoActual and sentido)) else -p))
    print("Elevador en piso %d" % (pisoActual))
    while(len(bajos) or len(altos)):
        if(sentido):
            if(len(altos)):
                print("Elevador subiendo")
                for p in range(pisoActual + 1, altos[0] + 1):
                    print("Elevador en piso %d" % (p))
                pisoActual = heappop(altos)
                while(len(altos) and pisoActual == altos[0]):
                    heappop(altos)
            else:
                sentido = 0
        else:
            if(len(bajos)):
                print("Elevador descendiendo")
                for p in range(pisoActual - 1, -bajos[0] - 1, -1):
                    print("Elevador en piso %d" % (p))
                pisoActual = -heappop(bajos)
                while(len(bajos) and pisoActual == -bajos[0]):
                    heappop(bajos)
            else:
                sentido = 1
        print("Elevador se detiene")
        if(pisoActual in mapaPisos):
            pisoNuevo = mapaPisos[pisoActual]
            mapaPisos.pop(pisoActual)
            print("Piso ingresado %d" % (pisoNuevo))
            heappush((altos if (pisoNuevo > pisoActual or (pisoNuevo == pisoActual and sentido)) else bajos),
                (pisoNuevo if (pisoNuevo > pisoActual or (pisoNuevo == pisoActual and sentido)) else -pisoNuevo))

def main():
    """
    Ejecución principal del algoritmo del elevador.
    
    Configura los parámetros iniciales del elevador y llama a la función algoritmoElevador.
    """
    arregloPisos = [5, 29, 13, 10]                          # Lista de pisos a visitar
    pisoInicial = 4                                         # Piso en el que se encuentra el elevador al inicio
    mapaPisos = {5 : 2, 29 : 10, 13 : 1, 10 :1}             # Mapa de pisos con nuevos destinos
    sentido = (1 if pisoInicial < arregloPisos[0] else 0)   # Dirección del elevador (1: subiendo, 0: descendiendo)
    algoritmoElevador(arregloPisos, pisoInicial, mapaPisos, sentido)

if __name__ == "__main__":
    main()