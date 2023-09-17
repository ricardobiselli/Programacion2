import libro as l
import bibloteca as biblioteca

# Crear una lista vacía para almacenar los libros
libros = []

# Añadir los diccionarios a la lista
libros.append(l.libro1)
libros.append(l.libro2)
libros.append(l.libro3)


def menu():
    print("--------------------------------------")
    print("1 - Gestionar Prestamo")
    print("2 - Gestionar Devolucion")
    print("3 - Registrar nuevo libro")
    print("4 - Elimiar ejemplar")
    print("5 - Mostrar ejemplares perstados")
    print("6 - Salir")
    print("--------------------------------------")


def ejemplares_prestados():
    libros_prestados = False

    for libro in libros:
        if int(libro["cant_ej_pr"]) > 0:
            print("--------------------------------------------------------------------------------")
            print(
                f"Libro: {libro['titulo']}, Ejemplares prestados: {libro['cant_ej_pr']}"
            )
            print("--------------------------------------------------------------------------------")

            libros_prestados = True

    if not libros_prestados:
        print("No hay ningún libro prestado")

    return None


def registrar_nuevo_libro():
    # pedir al usuario losdatos del nuevo libro
    titulo = input("Ingresar el título del nuevo libro: ")
    autor = input("Ingresar el nombre del autor: ")
    cant_ej_ad = int(input("Ingrese la cantidad de ejemplares adquiridos: "))

    codigo_libro = l.generar_codigo()

    libro = {
        "cod": codigo_libro,
        "cant_ej_ad": cant_ej_ad,
        "cant_ej_pr": 0,
        "titulo": titulo,
        "autor": autor,
    }

    l.nuevo_libro(libros, libro)

    print("|-------------------------------------------|")
    print("Nuevo libro registrado: ")
    print("Código: ", codigo_libro)
    print("Título: ", titulo)
    print("Autor: ", autor)
    print("Cantidad de ejemplares adquiridos: ", cant_ej_ad)
    print("|-------------------------------------------|")


    return None


def eliminar_ejemplar_libro():
    codigo_libro = input("Ingrese el código del libro: ")

    for libro in libros:
        if codigo_libro == libro["cod"]:
            nueva_cantidad = int(
                input("Ingrese la nueva cantidad de ejemplares disponibles: ")
            )
            libro["cant_ej_ad"] = nueva_cantidad
            print(
                "------------------------------------------------------------------------------------------"
            )
            print(
                "La cantidad de ejemplares para el libro",
                libro["titulo"],
                "se ha actualizado a: ",
                libro["cant_ej_ad"],
            )
            print(
                "------------------------------------------------------------------------------------------"
            )
            break
    else:
        print("--------------------------------------------------------------")
        print("El libro que estas buscando no existe en nuestra base de datos")
        print("--------------------------------------------------------------")

    return None


def prestar_ejemplar_libro():
    codigo_libro = input("Ingrese el código del libro: ")
    libro_encontrado = None

    for libro in libros:
        if libro["cod"] == codigo_libro:
            libro_encontrado = libro
            break

    if libro_encontrado:
        print("--------------------------------------------------------")
        print("El código de libro ha sido encontrado:")
        print("Título:", libro_encontrado["titulo"])
        print("Autor:", libro_encontrado["autor"])
        print("--------------------------------------------------------")
        if (
            int(libro_encontrado["cant_ej_ad"]) - int(libro_encontrado["cant_ej_pr"])
            <= 0
        ):
            print("no hay ejemplares disponibles para prestar...")
        else:
            print(
                "cantidad de ejemplares para préstamo:",
                int(libro_encontrado["cant_ej_ad"])
                - int(libro_encontrado["cant_ej_pr"]),
            )
            prestamo = input("¿Desea gestionar el préstamo de 1 unidad? (s/n): \n")
            if prestamo.lower() == "s":
                libro["cant_ej_pr"] += 1
                print(
                    "Cantidad restante de ejemplares disponibles para préstamo: ",
                    int(libro["cant_ej_ad"]) - int(libro["cant_ej_pr"]),
                )
            else:
                print("--------------------------------------------------------")
                print("         ...NO SE HAN HECHO MODIFICACIONES...           ")
                print("--------------------------------------------------------")
    else:
        print("El libro no existe.")
    return None


def devolver_ejemplar_libro():
    codigo_libro = input("Ingrese el código del libro: ")
    libro_encontrado = None

    for libro in libros:
        if libro["cod"] == codigo_libro:
            if int(libro["cant_ej_pr"]) > 0:
                libro_encontrado = libro
                print(
                    "El código del libro es válido, y hay: ",
                    libro_encontrado["cant_ej_pr"],
                    "ejemplares prestados",
                )
                devolucion = input("¿Desea gestionar la devolución? (s/n): \n\n")
                if devolucion.lower() == "s":
                    libro["cant_ej_pr"] = str(int(libro["cant_ej_pr"]) - 1)
                    libro["cant_ej_ad"] = str(int(libro["cant_ej_ad"]) + 1)
                    print("--------------------------------------------------------")
                    print("         ...Devolución gestionada con éxito...")
                    print("--------------------------------------------------------")
                break
            else:
                print(
                    "El código del libro es válido, pero no hay ejemplares prestados en este momento"
                )
                break
    else:
        print("--------------------------------------------------------------")
        print("ERROR, No ha ingresado un código válido")
        print("--------------------------------------------------------------")

    return None
