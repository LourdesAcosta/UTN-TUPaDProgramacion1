def lista_act():
    with open("Gestion.csv", "r") as archivo:
        ver = archivo.read()
        return ver


def pedir_no_vacio(mensaje):
    while True:
        valor = input(mensaje).strip()
        if valor:
            return valor
        print("⚠️ Este campo no puede estar vacío.")


def pedir_entero(mensaje):
    while True:
        dato = input(mensaje).strip()

        if not dato.isdigit():
            print("⚠️ Debe ingresar un número entero.")
            continue

        numero = int(dato)

        if numero < 0:
            print("⚠️ El número no puede ser negativo.")
            continue

        return numero

#Agregar el país
def agregar_pais():
    nombre = pedir_no_vacio("Nombre del país: ")

    with open("Gestion.csv", "r") as archivo:
        for linea in archivo:
            linea = linea.strip()
            if not linea:
                continue

            partes = linea.split(",")

            if partes[0].lower() == "nombre":
                continue

            if partes[0].lower() == nombre.lower():
                print(f"Error: el país '{nombre}' ya existe.")
                return 

    continente = pedir_no_vacio("Continente: ")
    poblacion = pedir_entero("Población (entero): ")
    superficie = pedir_entero("Superficie en km² (entero): ")

    linea = f"{nombre},{poblacion},{superficie},{continente}\n"

    with open("Gestion.csv", "a") as archivo:
        archivo.write(linea)

    print("✅ País agregado correctamente.\n")
    print(lista_act())


#Actualizar pais
def actualizar_pais():
    nombre = pedir_no_vacio("Ingrese el nombre del país a actualizar: ")

    # leo las líneas 
    with open("Gestion.csv", "r") as archivo:
        lineas = archivo.readlines()

    nuevas_lineas = []
    encontrado = False

    for linea in lineas:
        linea_limpia = linea.strip()
        if not linea_limpia:
            continue

        partes = linea_limpia.split(",")

        if partes[0].lower() == "nombre":
            nuevas_lineas.append(linea_limpia)
            continue

        # si es el pais
        if partes[0].lower() == nombre.lower():
            print(f"Datos actuales de {partes[0]}:")
            print(f"  Población: {partes[1]}")
            print(f"  Superficie: {partes[2]} km²")

            nueva_poblacion = pedir_entero("Nueva población (entero): ")
            nueva_superficie = pedir_entero("Nueva superficie en km² (entero): ")

            partes[1] = str(nueva_poblacion)
            partes[2] = str(nueva_superficie)

            linea_limpia = ",".join(partes)
            encontrado = True

        nuevas_lineas.append(linea_limpia)

    if not encontrado:
        print(f"Error: el país '{nombre}' no existe.")
        return

    #rescribo el archivo con los datos
    with open("Gestion.csv", "w") as archivo:
        for linea_limpia in nuevas_lineas:
            archivo.write(linea_limpia + "\n")

    print("✅ Datos actualizados correctamente.\n")
    print(lista_act())

#Busco el país
def buscar_pais():
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

            if nombre_min == termino_min:
                # Coincidencia EXACTA
                print(f"[EXACTA] {nombre_pais} | Población: {poblacion} | Superficie: {superficie} | Continente: {continente}")
                encontrado = True

            elif termino_min in nombre_min:
                # Coincidencia PARCIAL
                print(f"[PARCIAL] {nombre_pais} | Población: {poblacion} | Superficie: {superficie} | Continente: {continente}")
                encontrado = True

    if not encontrado:
        print(f"No se encontraron países que coincidan con '{termino}'.")


#Filtro por continente
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
                continue

            nombre = partes[0].strip()
            poblacion = partes[1].strip()
            superficie = partes[2].strip()
            continente = partes[3].strip()

            if continente.lower() == continente_buscado:
                print(f"{nombre} | Población: {poblacion} | Superficie: {superficie} km² | Continente: {continente}")
                encontrado = True

    if not encontrado:
        print(f"No se encontraron países en el continente '{continente_buscado}'.")


#Filtro por población
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
                continue  # por si hay alguna línea rara

            nombre = partes[0].strip()
            poblacion = int(partes[1].strip())
            superficie = partes[2].strip()
            continente = partes[3].strip()

            mostrar = False

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


#Filtro por superficie
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

            superficie_valor = int(superficie_texto)

            mostrar = False

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


#ordenar por nombre
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

            pais = (nombre, poblacion, superficie, continente)
            paises.append(pais)

    # orden alfabético A–Z por nombre (posición 0 del tuple)
    paises.sort(key=lambda p: p[0].lower())

    print("=== Países ordenados por NOMBRE (A-Z) ===")
    for p in paises:
        print(f"{p[0]} | Población: {p[1]} | Superficie: {p[2]} km² | Continente: {p[3]}")

#ORDENAR POR POBLACIÓN
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
        paises.sort(key=lambda p: p[1])        
        print("=== Países ordenados por POBLACIÓN (menor a mayor) ===")
    else:
        paises.sort(key=lambda p: p[1], reverse=True)
        print("=== Países ordenados por POBLACIÓN (mayor a menor) ===")

    for p in paises:
        print(f"{p[0]} | Población: {p[1]} | Superficie: {p[2]} km² | Continente: {p[3]}")

#ORDENAR POR SUPERFICIE
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
        paises.sort(key=lambda p: p[2])        # p[2] = superficie
        print("=== Países ordenados por SUPERFICIE (menor a mayor) ===")
    else:
        paises.sort(key=lambda p: p[2], reverse=True)
        print("=== Países ordenados por SUPERFICIE (mayor a menor) ===")

    for p in paises:
        print(f"{p[0]} | Población: {p[1]} | Superficie: {p[2]} km² | Continente: {p[3]}")

#promedios
def mostrar_estadisticas():
    with open("Gestion.csv", "r") as archivo:
        max_poblacion = None
        pais_max = ""
        min_poblacion = None
        pais_min = ""

        suma_poblacion = 0
        suma_superficie = 0
        cantidad_paises = 0

        conteo_continentes = {}  # ej: {"America": 3, "Europa": 2}

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

            # Mayor y menor población
            if max_poblacion is None or poblacion > max_poblacion:
                max_poblacion = poblacion
                pais_max = nombre

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
