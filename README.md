# Algoritmo Elevador

Este proyecto simula el funcionamiento de un elevador en un edificio de 29 pisos. El objetivo es optimizar el tiempo de desplazamiento del elevador, respetando su dirección de movimiento actual (subiendo o bajando).

## Descripción

El algoritmo permite al elevador atender un conjunto de pisos en un orden definido, comenzando desde un piso inicial. A medida que el elevador se mueve, imprime en consola su piso actual, la dirección en la que se desplaza, el piso en el que se detiene y el piso ingresado.

## Características

- Simulación del movimiento del elevador.
- Impresión en consola de las iteraciones del elevador.
- Manejo eficiente de la dirección de desplazamiento.

## Instalación

Para ejecutar la aplicación, asegúrate de tener Python instalado en tu sistema. Luego, sigue estos pasos:

1. Clona el repositorio:

   ```bash
   git clone https://github.com/Lordrap2002/Test-9.git
   ```

2. Navega al directorio del proyecto:

   ```bash
   cd Test-9
   ```

3. Ejecuta el script de Python:

   ```bash
   python AlgoritmoElevador.py
   ```

## Uso

El script `AlgoritmoElevador.py` contiene la función `algoritmoElevador`, que recibe los siguientes parámetros:

- `arregloPisos`: lista de pisos a visitar.
- `pisoActual`: piso inicial del elevador.
- `mapaPisos`: diccionario que mapea pisos a nuevos destinos.
- `sentido`: dirección del elevador (1 para subir, 0 para bajar).