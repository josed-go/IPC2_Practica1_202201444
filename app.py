from funciones import funciones
func = funciones()

def main():
    print("---------------------------------------------------")
    print("** PRACTICA 1 - INTRODUCCIÓN A LA PROGRAMACIÓN 2 **")
    print("---------------------------------------------------")
    menu()

def datos_estudiante():
    print("------------------------------------------------")
    print("############# DATOS DEL ESTUDIANTE #############")
    print("------------------------------------------------")
    print("-> José David Góngora Olmedo ")
    print("-> 202201444 ")
    print("-> Introducción a la Programación y Computación 2 sección ""D"" ")
    print("-> Ingenieria en Ciencias y Sistemas ")
    print("-> 4to Semestre ")

def menu():
    print("")
    print("-------------------------------------------------------")
    print("############### COLORÉALO - GUATEMATTEL ###############")
    print("-------------------------------------------------------")

    print("-------------------------------------------------------")
    print("| 1. CREAR TRABLERO                                   |")
    print("| 2. DATOS DEL ESTUDIANTE                             |")
    print("| 3. SALIR                                            |")
    print("-------------------------------------------------------")

    print("")
    print("## INGRESE UNA OPCION: ##")
    opcion = input()
    print("")

    if opcion == "1":
        filas = input("INGRESA EL NUMERO DE FILAS PARA EL TABLERO: ")
        print("------------------------------------------------------")
        colum = input("INGRESA EL NUMERO DE COLUMNAS PARA EL TABLERO: ")
        print("------------------------------------------------------")

        if filas.isdigit() and colum.isdigit() and int(filas) > 0 and int(colum) > 0:
            func.agregar_tablero(filas, colum)
        else :
            print("** POR FAVOR SOLO INGRESA NUMEROS **")
        #menu()
    elif opcion == "2":
        datos_estudiante()
        
        menu()
    elif opcion == "3":
        print("## SALIENDO... ##")

    else:
        print("** OPCIÓN NO VÁLIDA **")
        menu()

main()