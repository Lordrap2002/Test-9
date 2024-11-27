def buscarPalabras(matriz, palabras):
    """
    Busca palabras en una matriz de letras y las imprime con sus posiciones.
    
    :param matriz: Matriz de letras como un arreglo de strings, cada string representa una fila.
    :param palabras: Arreglo de strings, cada string es una palabra a buscar.
    """
    matriz1 = []
    respuestas = []
    posiciones = []
    # Convertir la matriz de strings a una matriz de listas de letras
    for fila in matriz:
        matriz1.append(fila.split())
    # Iterar sobre cada palabra a buscar
    for palabra in palabras:
        ind = 0
        respuestas = []
        print("Searching \"%s\"" % (palabra))
        # Iterar sobre la matriz para buscar la palabra
        for fila in range(len(matriz1)):
            for i in range(2):
                ind = 0
                posiciones = []
                for col in range(len(matriz1[0])):
                    if(ind == len(palabra)):
                        break
                    if(matriz1[(col if i else fila)][(fila if i else col)] == palabra[ind]):
                        posiciones.append((palabra[ind], (col if i else fila), (fila if i else col)))
                        ind += 1
                    else:
                        ind = 0
                        posiciones = []
                if(ind == len(palabra)):
                        break
            if(ind != len(palabra)):
                for d in range(len(matriz1)):
                    ind = 0
                    posiciones = []
                    for diag in range(len(matriz1) - d):
                        if(ind == len(palabra)):
                            break
                        if(d + diag < len(matriz1) and diag < len(matriz1[0]) and matriz1[d + diag][diag] == palabra[ind]):
                            posiciones.append((palabra[ind], d + diag, diag))
                            ind += 1
                        else:
                            ind = 0
                            posiciones = []
                    if(ind == len(palabra)):
                        break
            if(ind == len(palabra)):
                for (letra, fila, col) in posiciones:
                    print("%c - [%d, %d]" % (letra, fila, col))
                break
        if(not ind):
            print("\"%s\" Not found" % (palabra))

def main():
    """
    Ejecución principal del algoritmo del juego de sopa de letras.
    
    Configura los parámetros iniciales del juego y llama a la función buscarPalabras.
    """
    matriz = ["S O L", "U N O", "N U T"]
    palabras = ["SUN", "SOL", "LOT", "ONU", "RAY", "SNT"]
    buscarPalabras(matriz, palabras)

if __name__ == "__main__":
    main()