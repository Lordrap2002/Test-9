# Algoritmo Elevador

Este proyecto simula el funcionamiento de un elevador en un edificio de 29 pisos. El objetivo es optimizar el tiempo de desplazamiento del elevador, respetando su dirección de movimiento actual (subiendo o bajando).

## Descripción

El algoritmo permite al elevador atender un conjunto de pisos en un orden definido, comenzando desde un piso inicial. A medida que el elevador se mueve, imprime en consola su piso actual, la dirección en la que se desplaza, el piso en el que se detiene y el piso ingresado.

## Características

- Simulación del movimiento del elevador.
- Impresión en consola de las iteraciones del elevador.
- Manejo eficiente de la dirección de desplazamiento.

### Versión 2

- Se ha creado una nueva versión de la aplicación donde la entrada inicial solo incluye el arreglo de pisos y el piso inicial.
- El usuario puede solicitar el ascensor en cualquier momento de ejecución de la aplicación, teniendo en cuenta la dirección actual del ascensor para manejar la cola de solicitudes.

### Versión 3

- Se ha implementado una versión de la aplicación donde hay 2 elevadores que manejan las solicitudes de pisos de la forma más eficiente, minimizando el recorrido posible.

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