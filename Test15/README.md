# Test 15 - Buscador de Palabras en Sopa de Letras

## Descripción

Este proyecto consiste en un algoritmo que encuentra palabras en una sopa de letras. Dada una matriz de dos dimensiones y una lista de palabras, el algoritmo lista la ubicación en la matriz de cada una de las letras en cada palabra. Las palabras pueden ser construidas a partir de letras adyacentes, ya sea horizontal o verticalmente.

## Consigna

- Cada palabra debe ser construida de letras inmediatamente adyacentes.
- La misma letra solo puede ser usada una vez para la misma palabra, pero puede ser utilizada múltiples veces para diferentes palabras.
- El orden alfabético de las palabras debe seguir las reglas del español (de izquierda a derecha o de arriba a abajo).
- La matriz es ingresada como un arreglo de textos donde cada string representa una fila de la matriz y las letras están separadas por espacios. (ej.: `["S O L", "U N O", "N U T"]`)
- Las palabras a buscar son ingresadas como un arreglo de textos. (ej.: `["SUN", "SOL", "LOT", "ONU", "RAY"]`)

## Instalación

1. Clona el repositorio:
   ```bash
   git clone https://github.com/Lordrap2002/Test-9
   ```
2. Navega al directorio del proyecto:
   ```bash
   cd Test15
   ```
3. Ejecuta el script de Python:

   ```bash
   python AlgoritmoJuego.py
   ```