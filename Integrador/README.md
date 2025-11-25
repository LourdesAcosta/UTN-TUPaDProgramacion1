***Descripción del programa***
El siguiente programa es un menú que permite gestionar información de países.
Cada país se guarda con su nombre, continente, cantidad de habitantes y superficie en km².

El programa da la posibilidad de agregar un país nuevo con todos sus datos, o actualizar la población y la superficie de un país que ya existe.
También permite buscar un país por su nombre, ya sea con una coincidencia exacta o parcial.

Además, se pueden filtrar países por continente, por rango de población o por rango de superficie (clasificados como países pequeños, medianos o grandes según el criterio definido en el programa).

Otra opción del menú es ordenar los países:
-Alfabéticamente por nombre
-Por población
-Por superficie
pudiendo elegir si se ordena de menor a mayor o de mayor a menor.

Finalmente, el programa puede mostrar estadísticas, como:
-Cuál es el país con mayor población,
-Cuál es el país con menor población,
-El promedio de población,
-El promedio de superficie de los países cargados,
-La cantidad de países por continente.


***Instrucciones de uso del programa***

Para utilizar el programa, primero se debe ejecutar el archivo del menú principal (por ejemplo, desde Visual Studio Code, haciendo Run / Start sobre el archivo que contiene el while con las opciones).

Al iniciar, se muestra un menú numerado del 1 al 7. El usuario debe escribir el número de la opción que quiere usar y presionar Enter.
Si el archivo Gestion.csv está vacío (sin países cargados), se recomienda comenzar por la opción 1 para agregar al menos un país. Si ya hay datos cargados, se puede usar cualquier opción.

Las opciones funcionan de la siguiente manera:

///Opción 1 – Agregar un nuevo país///
El programa pide:
-Nombre del país (no puede estar vacío y no puede repetirse).
-Continente.
-Población (entero, no negativo).
-Superficie en km² (entero, no negativo).
Si los datos son válidos y el país no existe, se guarda una nueva línea en Gestion.csv con el formato:
nombre,población,superficie,continente
Luego muestra la lista actualizada de países.

///Opción 2 – Actualizar datos de población o superficie///
Primero pide el nombre del país a actualizar.
Si el país no existe en el archivo, muestra un mensaje de error.
Si el país existe, muestra la población y superficie actuales, y luego pide:
-Nueva población.
-Nueva superficie.
Esos valores se reemplazan en el archivo y se vuelve a mostrar la lista actualizada.

///Opción 3 – Buscar país por nombre///
Pide al usuario que ingrese un texto de búsqueda (por ejemplo, el nombre completo o parte del nombre).
El programa recorre todos los países:
-Si el nombre coincide exactamente, muestra la coincidencia como [EXACTA].
-Si el texto aparece dentro del nombre del país (coincidencia parcial), la muestra como [PARCIAL].
-Si no hay coincidencias, muestra un mensaje indicando que no se encontraron países.

///Opción 4 – Filtrar países///
Al elegir esta opción, aparece un submenú:

1 = Por continente

2 = Por rango de población

3 = Por rango de superficie

Según la elección:
4.1 Por continente
Pide el nombre de un continente y muestra solo los países que pertenecen a ese continente.

4.2 Por rango de población (pequeño / mediano / grande)
Pide un tipo de rango de población:
-pequeño: menos de 10.000.000 de habitantes
-mediano: entre 10.000.000 y 50.000.000
-grande: más de 50.000.000
Luego muestra los países que entran en la categoría elegida.

4.3 Por rango de superficie (pequeño / mediano / grande)
Pide un tipo de rango de superficie:
-pequeño: menos de 100.000 km²
-mediano: entre 100.000 y 1.000.000 km²
-grande: más de 1.000.000 km²
Luego muestra los países que cumplen ese rango.
Esta opción solo muestra resultados filtrados, no modifica el archivo.

///Opción 5 – Ordenar países///
Al elegir esta opción, aparece otro submenú:

1 = Por nombre

2 = Por población

3 = Por superficie

5.1 Ordenar por nombre
Muestra todos los países ordenados alfabéticamente (A–Z).

5.2 Ordenar por población
Primero pregunta si se quiere ordenar:
-a = Ascendente (de menor a mayor población)
-d = Descendente (de mayor a menor población)
Luego muestra los países en ese orden.

5.3 Ordenar por superficie
También permite elegir:
-a = Ascendente (de menor a mayor superficie)
-d = Descendente (de mayor a menor superficie)
Y muestra la lista ordenada según la elección.
Igual que en el filtrado, acá solo se ordena y se muestra por pantalla, el archivo base no se altera.

///Opción 6 – Mostrar estadísticas///
Esta opción calcula y muestra:
-El país con mayor población.
-El país con menor población.
-El promedio de población de todos los países cargados.
-El promedio de superficie.
-La cantidad de países por continente.
Si no hay países cargados, informa que no hay datos para mostrar.

///Opción 7 – Salir///
Finaliza el bucle del menú y termina la ejecución del programa.

***Ejemplos de entradas y salidas ***
Agregar un país (Opción 1)
--Entrada de usuario:
Ingrese una opción:
1= Agregar un nuevo país con todos sus datos
2= Actualizar datos de Población o Superficie
3= Buscar país por nombre
4= Filtrar países
5= Ordenar países
6= Mostrar estadísticas
7= Salir
: 1

--Luego el programa pregunta:
Nombre del país: Chile
Continente: America
Población (entero): 19000000
Superficie en km² (entero): 756000

--Salida del programa:
✅ País agregado correctamente.

Nombre,Poblacion,Superficie,Continente
Argentina,46000000,2780000,America
España,48000000,505990,Europa
Chile,19000000,756000,America
--------------------------------------

Buscar país por nombre (Opción 3)
--Suponiendo que el archivo ya contiene:
Nombre,Poblacion,Superficie,Continente
Argentina,46000000,2780000,America
España,48000000,505990,Europa
Chile,19000000,756000,America

--Entrada del usuario:
Ingrese una opción:
1= Agregar un nuevo país con todos sus datos
2= Actualizar datos de Población o Superficie
3= Buscar país por nombre
4= Filtrar países
5= Ordenar países
6= Mostrar estadísticas
7= Salir
: 3

--Luego el programa pregunta:
Ingrese el nombre (o parte del nombre) del país a buscar: chi

--Salida del programa:
[PARCIAL] Chile | Población: 19000000 | Superficie: 756000 | Continente: America

