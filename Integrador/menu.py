import funciones

print("Menú de opciones: \n\n")

salir = False

while salir == False:
    opcion = int(input("Ingrese una opción: \n"
        "1= Agregar un nuevo país con todos sus datos \n"
        "2= Actualizar datos de Población o Superficie \n"
        "3= Buscar país por nombre \n"
        "4= Filtrar países\n"
        "5= Ordenar países  \n"
        "6= Mostrar estadísticas \n"
        "7= Salir \n"
        ": "
    ))

    if opcion == 1:
        funciones.agregar_pais()

    elif opcion == 2:
        funciones.actualizar_pais()

    elif opcion == 3:
        funciones.buscar_pais()

    elif opcion == 4:
        formato = input(
            "1= Por continente\n"
            "2= Por rango de población\n"
            "3= Por rango de superficie\n"
            ": "
        )

        if formato == "1":
            funciones.filtrar_por_continente()
        elif formato == "2":
            funciones.filtrar_por_poblacion()
        elif formato == "3":
            funciones.filtrar_por_superficie()
        else:
            print("Opción inválida")

    elif opcion == 5:
        formato = input(
            "1= Por nombre\n"
            "2= Por población\n"
            "3= Por superficie\n"
            ": "
        )

        if formato == "1":
            funciones.ordenar_por_nombre()
        elif formato == "2":
            funciones.ordenar_por_poblacion()
        elif formato == "3":
            funciones.ordenar_por_superficie()
        else:
            print("Opción inválida")

    elif opcion == 6:
        funciones.mostrar_estadisticas()

    elif opcion == 7:
        salir = True

    else:
        print("Opción incorrecta, ingrese una opción válida")
