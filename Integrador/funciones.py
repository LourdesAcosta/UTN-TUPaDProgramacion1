# Devuelve el contenido completo actual del archivo de países
def lista_act():
    with open("Gestion.csv", "r") as archivo:
        ver = archivo.read()
        return ver


# Pide un texto por consola y valida que NO esté vacío
def pedir_no_vacio(mensaje):
    while True:
        valor = input(mensaje).strip()
        if valor:  # si no está vacío
            return valor
        print("⚠️ Este campo no puede estar vacío.")


# Pide un número entero por consola y valida que:
# - no esté vacío
# - sea dígito
# - no sea negativo
def pedir_entero(mensaje):
    while True:
        dato = input(mensaje).strip()

        # si el parámetro no es un dígito, vuelvo a pedirlo
        if not dato.isdigit():
            print("⚠️ Debe ingresar un número entero.")
            continue

        numero = int(dato)

        if numero < 0:
            print("⚠️ El número no puede ser negativo.")
            continue

        return numero


# Agregar un país nuevo al archivo
def agregar_pais():
    # Uso la función de validación para asegurar que el nombre no esté vacío
    nombre = pedir_no_vacio("Nombre del país: ")

    # Recorro el archivo para verificar si el país ya existe
    with open("Gestion.csv", "r") as archivo:
        for linea in archivo:
            linea = linea.strip()
            if not linea:
                continue

            partes = linea.split(",")

            # Si la primera columna es "nombre", asumo que es la fila de encabezado y la salto
            if partes[0].lower() == "nombre":
                continue

            # Verifico que el país no esté repetido
            if partes[0].lower() == nombre.lower():
                print(f"Error: el país '{nombre}' ya existe.")
                return

    # Pido el resto de los datos, reutilizando las funciones de validación
    continente = pedir_no_vacio("Continente: ")
    poblacion = pedir_entero("Población (entero): ")
    superficie = pedir_entero("Superficie en km² (entero): ")

    # Armo la línea en formato CSV
    linea = f"{nombre},{poblacion},{superficie},{continente}\n"

    # Abro el archivo en modo agregar y escribo el nuevo país al final
    with open("Gestion.csv", "a") as archivo:
        archivo.write(linea)

    print("✅ País agregado correctamente.\n")
    print(lista_act())


# Actualizar la población y la superficie de un país existente
def actualizar_pais():
    # Pido el nombre del país a actualizar y valido que no esté vacío
    nombre = pedir_no_vacio("Ingrese el nombre del país a actualizar: ")

    # Leo todas las líneas del archivo para poder reescribirlo luego
    with open("Gestion.csv", "r") as archivo:
        lineas = archivo.readlines()

    nuevas_lineas = []   # acá voy a guardar las líneas actualizadas
    encontrado = False   # bandera para saber si encontré el país

    for linea in lineas:
        linea_limpia = linea.strip()
        if not linea_limpia:
            continue

        partes = linea_limpia.split(",")

        # Si la primera columna es "nombre", considero que es encabezado y lo copio tal cual
        if partes[0].lower() == "nombre":
            nuevas_lineas.append(linea_limpia)
            continue

        # Si es el país buscado, muestro datos actuales y pido los nuevos
        if partes[0].lower() == nombre.lower():
            print(f"Datos actuales de {partes[0]}:")
            print(f"  Población: {partes[1]}")
            print(f"  Superficie: {partes[2]} km²")

            nueva_poblacion = pedir_entero("Nueva población (entero): ")
            nueva_superficie = pedir_entero("Nueva superficie en km² (entero): ")

            # Actualizo los campos de población y superficie
            partes[1] = str(nueva_poblacion)
            partes[2] = str(nueva_superficie)

            # Vuelvo a unir la lista en una sola línea CSV
            linea_limpia = ",".join(partes)
            encontrado = True

        # Guardo la línea (sea la original o la actualizada)
        nuevas_lineas.append(linea_limpia)

    if not encontrado:
        print(f"Error: el país '{nombre}' no existe.")
        return

    # Rescribo el archivo completo con las nuevas líneas
    with open("Gestion.csv", "w") as archivo:
        for linea_limpia in nuevas_lineas:
            archivo.write(linea_limpia + "\n")

    print("✅ Datos actualizados correctamente.\n")
    print(lista_act())


# Buscar país por nombre (coincidencia exacta o parcial)
def buscar_pais():
    # Reutilizo la función para asegurar que el término de búsqueda no esté vacío
    termino = pedir_no_vacio("Ingrese el nombre (o parte del nombre) del país a buscar: ")
    termino_min = termino.lower()

    encontrado = False

    with open("Gestion.csv", "r") as archivo:
        for linea in archivo:
            linea = linea.strip()
            if not linea:
                continue

            partes = linea.split(",")

            # Salto encabezado si existe
            if partes[0].lower() == "nombre":
                continue

            nombre_pais = partes[0].strip()
            poblacion = partes[1].strip()
            superficie = partes[2].strip()
            continente = partes[3].strip()

            nombre_min = nombre_pais.lower()

            # Coincidencia exacta del nombre
            if nombre_min == termino_min:
                print(f"[EXACTA] {nombre_pais} | Población: {poblacion} | Superficie: {superficie} | Continente: {continente}")
                encontrado = True

            # Coincidencia parcial: el término está contenido en el nombre
            elif termino_min in nombre_min:
                print(f"[PARCIAL] {nombre_pais} | Población: {poblacion} | Superficie: {superficie} | Continente: {continente}")
                encontrado = True

    if not encontrado:
        print(f"No se encontraron países que coincidan con '{termino}'.")


# Filtrar países por continente
def filtrar_por_continente():
    continente_buscado = pedir_no_vacio("Ingrese el continente a filtrar: ").lower()
    encontrado = False

    with open("Gestion.csv", "r") as archivo:
        for linea in archivo:
            linea = linea.strip()
            if not linea:
                continue

            partes = linea.split(",")
            if len(partes) != 4:
                continue  # si la línea no tiene 4 campos, la ignoro

            nombre = partes[0].strip()
            poblacion = partes[1].strip()
            superficie = partes[2].strip()
            continente = partes[3].strip()

            # Comparo el continente de la línea con el buscado, sin distinguir mayúsculas
            if continente.lower() == continente_buscado:
                print(f"{nombre} | Población: {poblacion} | Superficie: {superficie} km² | Continente: {continente}")
                encontrado = True

    if not encontrado:
        print(f"No se encontraron países en el continente '{continente_buscado}'.")


# Filtrar países por rango de población (pequeño/mediano/grande)
def filtrar_por_poblacion():
    print("Rangos disponibles: pequeño / mediano / grande")
    while True:
        tipo = pedir_no_vacio("Filtrar por población (pequeño/mediano/grande): ").lower()
        if tipo in ("pequeño", "mediano", "grande"):
            break
        print("⚠️ Opción inválida. Escriba: pequeño, mediano o grande.")

    encontrado = False

    with open("Gestion.csv", "r") as archivo:
        for linea in archivo:
            linea = linea.strip()
            if not linea:
                continue

            partes = linea.split(",")
            if len(partes) != 4:
                continue  # por si hay alguna línea incompleta

            nombre = partes[0].strip()
            poblacion = int(partes[1].strip())
            superficie = partes[2].strip()
            continente = partes[3].strip()

            mostrar = False

            # Clasificación por rangos de población
            if tipo == "pequeño" and poblacion < 10000000:
                mostrar = True
            elif tipo == "mediano" and 10000000 <= poblacion <= 50000000:
                mostrar = True
            elif tipo == "grande" and poblacion > 50000000:
                mostrar = True

            if mostrar:
                print(f"{nombre} | Población: {poblacion} | Superficie: {superficie} km² | Continente: {continente}")
                encontrado = True

    if not encontrado:
        print(f"No se encontraron países en el rango de población '{tipo}'.")


# Filtrar países por rango de superficie (pequeño/mediano/grande)
def filtrar_por_superficie():
    print("Rangos disponibles: pequeño / mediano / grande")
    while True:
        tipo = pedir_no_vacio("Filtrar por superficie (pequeño/mediano/grande): ").lower()
        if tipo in ("pequeño", "mediano", "grande"):
            break
        print("⚠️ Opción inválida. Escriba: pequeño, mediano o grande.")

    encontrado = False

    with open("Gestion.csv", "r") as archivo:
        for linea in archivo:
            linea = linea.strip()
            if not linea:
                continue

            partes = linea.split(",")
            if len(partes) != 4:
                continue

            nombre = partes[0].strip()
            poblacion = partes[1].strip()
            superficie_texto = partes[2].strip()
            continente = partes[3].strip()

            # Convierto la superficie a entero para poder comparar rangos
            superficie_valor = int(superficie_texto)

            mostrar = False

            # Clasificación por rangos de superficie
            if tipo == "pequeño" and superficie_valor < 100000:
                mostrar = True
            elif tipo == "mediano" and 100000 <= superficie_valor <= 1000000:
                mostrar = True
            elif tipo == "grande" and superficie_valor > 1000000:
                mostrar = True

            if mostrar:
                print(f"{nombre} | Población: {poblacion} | Superficie: {superficie_valor} km² | Continente: {continente}")
                encontrado = True

    if not encontrado:
        print(f"No se encontraron países en el rango de superficie '{tipo}'.")


# Ordenar países por nombre (alfabéticamente A-Z)
def ordenar_por_nombre():
    paises = []

    with open("Gestion.csv", "r") as archivo:
        for linea in archivo:
            linea = linea.strip()
            if not linea:
                continue

            partes = linea.split(",")
            if len(partes) != 4:
                continue

            nombre = partes[0].strip()
            poblacion = int(partes[1].strip())
            superficie = int(partes[2].strip())
            continente = partes[3].strip()

            # Uso una tupla para representar cada país
            pais = (nombre, poblacion, superficie, continente)
            paises.append(pais)

    # Orden alfabético A–Z por nombre (posición 0 de la tupla)
    paises.sort(key=lambda p: p[0].lower())

    print("=== Países ordenados por NOMBRE (A-Z) ===")
    for p in paises:
        print(f"{p[0]} | Población: {p[1]} | Superficie: {p[2]} km² | Continente: {p[3]}")


# Ordenar países por población (ascendente o descendente)
def ordenar_por_poblacion():
    paises = []

    with open("Gestion.csv", "r") as archivo:
        for linea in archivo:
            linea = linea.strip()
            if not linea:
                continue

            partes = linea.split(",")
            if len(partes) != 4:
                continue

            nombre = partes[0].strip()
            poblacion = int(partes[1].strip())
            superficie = int(partes[2].strip())
            continente = partes[3].strip()

            pais = (nombre, poblacion, superficie, continente)
            paises.append(pais)

    print("Ordenar población de forma:")
    print("  a) Ascendente (menor a mayor)")
    print("  d) Descendente (mayor a menor)")

    while True:
        opcion = pedir_no_vacio("Elija (a/d): ").lower()
        if opcion in ("a", "d"):
            break
        print("⚠️ Opción inválida. Ingrese 'a' o 'd'.")

    if opcion == "a":
        # Ordeno por población (posición 1 de la tupla), de menor a mayor
        paises.sort(key=lambda p: p[1])
        print("=== Países ordenados por POBLACIÓN (menor a mayor) ===")
    else:
        # Ordeno por población de mayor a menor
        paises.sort(key=lambda p: p[1], reverse=True)
        print("=== Países ordenados por POBLACIÓN (mayor a menor) ===")

    for p in paises:
        print(f"{p[0]} | Población: {p[1]} | Superficie: {p[2]} km² | Continente: {p[3]}")


# Ordenar países por superficie (ascendente o descendente)
def ordenar_por_superficie():
    paises = []

    with open("Gestion.csv", "r") as archivo:
        for linea in archivo:
            linea = linea.strip()
            if not linea:
                continue

            partes = linea.split(",")
            if len(partes) != 4:
                continue

            nombre = partes[0].strip()
            poblacion = int(partes[1].strip())
            superficie = int(partes[2].strip())
            continente = partes[3].strip()

            pais = (nombre, poblacion, superficie, continente)
            paises.append(pais)

    print("Ordenar superficie de forma:")
    print("  a) Ascendente (menor a mayor)")
    print("  d) Descendente (mayor a menor)")

    while True:
        opcion = pedir_no_vacio("Elija (a/d): ").lower()
        if opcion in ("a", "d"):
            break
        print("⚠️ Opción inválida. Ingrese 'a' o 'd'.")

    if opcion == "a":
        # Ordeno por superficie (posición 2 de la tupla), de menor a mayor
        paises.sort(key=lambda p: p[2])
        print("=== Países ordenados por SUPERFICIE (menor a mayor) ===")
    else:
        # Ordeno por superficie de mayor a menor
        paises.sort(key=lambda p: p[2], reverse=True)
        print("=== Países ordenados por SUPERFICIE (mayor a menor) ===")

    for p in paises:
        print(f"{p[0]} | Población: {p[1]} | Superficie: {p[2]} km² | Continente: {p[3]}")


# Mostrar estadísticas generales sobre los países cargados
def mostrar_estadisticas():
    with open("Gestion.csv", "r") as archivo:
        max_poblacion = None
        pais_max = ""
        min_poblacion = None
        pais_min = ""

        suma_poblacion = 0
        suma_superficie = 0
        cantidad_paises = 0

        # Diccionario para contar países por continente, ej: {"America": 3, "Europa": 2}
        conteo_continentes = {}

        for linea in archivo:
            linea = linea.strip()
            if not linea:
                continue

            partes = linea.split(",")
            if len(partes) != 4:
                continue

            nombre = partes[0].strip()
            poblacion = int(partes[1].strip())
            superficie = int(partes[2].strip())
            continente = partes[3].strip()

            # Actualizo contadores generales
            cantidad_paises += 1
            suma_poblacion += poblacion
            suma_superficie += superficie

            # Mayor población
            if max_poblacion is None or poblacion > max_poblacion:
                max_poblacion = poblacion
                pais_max = nombre

            # Menor población
            if min_poblacion is None or poblacion < min_poblacion:
                min_poblacion = poblacion
                pais_min = nombre

            # Conteo por continente
            if continente in conteo_continentes:
                conteo_continentes[continente] += 1
            else:
                conteo_continentes[continente] = 1

    if cantidad_paises == 0:
        print("No hay datos de países en Gestion.csv.")
        return

    # Cálculo de promedios
    promedio_poblacion = suma_poblacion / cantidad_paises
    promedio_superficie = suma_superficie / cantidad_paises

    print("=== ESTADÍSTICAS ===")
    print(f"País con MAYOR población: {pais_max} ({max_poblacion} habitantes)")
    print(f"País con MENOR población: {pais_min} ({min_poblacion} habitantes)")
    print(f"Promedio de población: {promedio_poblacion}")
    print(f"Promedio de superficie: {promedio_superficie} km²")

    print("\nCantidad de países por continente:")
    for cont, cant in conteo_continentes.items():
        print(f"  {cont}: {cant}")
