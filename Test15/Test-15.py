def buscarPalabras(matriz, palabras):
    matriz1 = []
    posiciones = []
    for fila in matriz:
        matriz1.append(fila.split())
    for palabra in palabras:
        ind = 0
        print("Searching \"%s\"" % (palabra))
        for fila in range(len(matriz1)):
            ind = 0
            posiciones = []
            for col in range(len(matriz1[0])):
                if(ind == len(palabra)):
                    break
                if(matriz1[fila][col] == palabra[ind]):
                    posiciones.append((palabra[ind], fila, col))
                    ind += 1
                else:
                    ind = 0
                    posiciones = []
            if(ind == len(palabra)):
                for (letra, fila, col) in posiciones:
                    print("%c - [%d, %d]" % (letra, fila, col))
                break
            ind = 0
            posiciones = []
            for col in range(len(matriz1[0])):
                if(ind == len(palabra)):
                    break
                elif(matriz1[col][fila] == palabra[ind]):
                    posiciones.append((palabra[ind], col, fila))
                    ind += 1
                else:
                    ind = 0
                    posiciones = []
            if(ind == len(palabra)):
                for (letra, fila, col) in posiciones:
                    print("%c - [%d, %d]" % (letra, fila, col))
                break
        if(not ind):
            print("\"%s\" Not found" % (palabra))

def main():
    matriz = ["S O L", "U N O", "N U T"]
    palabras = ["SUN", "SOL", "LOT", "ONU", "RAY"]
    buscarPalabras(matriz, palabras)

if __name__ == "__main__":
    main()