from lista_tablero import lista_tablero
from lista_colores import lista_colores
from tablero import tablero
from colores import colores

class funciones:
    def __init__(self):
        self.lista_tab = lista_tablero()

    def agregar_tablero(self, filas_, columnas_):

        lista_colors = lista_colores()
        
        print("¡TABLERO CREADO!\n")

        print("## TABLERO INICIAL ##")
        self.mostrar_trablero_inicial(filas_, columnas_)

        self.agregar_piezas(lista_colors, filas_, columnas_)
        nuevo = tablero(filas_, columnas_, lista_colors)
        self.lista_tab.agregar_tablero(nuevo)
        #self.lista_tab.mostrar_lista()
        print("")
        print("-> GENERANDO GRAFICA DEL TABLERO...\n")
        nombre_grafica = input("INGRESE EL NOMBRE PARA GUARDAR LA GRAFICA: ")
        print()
        self.lista_tab.generar_grafica(nombre_grafica)

    def agregar_piezas(self, lista_colors, filas_, columnas_):
        resp_ = "SI"

        while resp_ == "SI":
            print("## ELIGE UN COLOR ##")
            self.colores()
            color_ingresado = input(" INGRESA EL NUMERO DEL COLOR: ")
            color_guardar, color, codigo_c = self.obtener_color(color_ingresado)
            
            print("TURNO DE COLOR:", color+"\n")
            print(f"INGRESA LA FILA EN DONDE QUIERES COLOCAR LA PIEZA (RANGO: 1 - {filas_})")
            fila_colocar = input("->")

            if self.validar_fila_columna("fila", fila_colocar, filas_) == True:
                print(f"INGRESA LA COLUMNA EN DONDE QUIERES COLOCAR LA PIEZA (RANGO: 1 - {columnas_})")
                columna_colocar = input("->")

                if self.validar_fila_columna("columna", columna_colocar, columnas_) == True:
                    nuevo_color = colores(color_guardar, fila_colocar, columna_colocar, codigo_c)
                    lista_colors.agregar_color(nuevo_color)
                    self.mostrar_posicion_pieza(filas_, columnas_, color_guardar, fila_colocar, columna_colocar, lista_colors)
            else:
                print("## ERROR ##")
            
            print("")
            print("¿DESEAS AGREGAR OTRA PIEZA?\n")
            resp = input("INGRESA TU RESPUESTA (SI/NO): ")
            resp_ = resp.upper()

        self.llenar_lista(filas_, columnas_, lista_colors)

    def llenar_lista(self, filas, columnas, lista_colors):
        for columnas_ in range(1, int(columnas)+1):
            for filas_ in range(1, int(filas)+1):

                nuevo_color = colores(" ", filas_, columnas_, "white")
                color_existente = lista_colors.buscar_color(filas_, columnas_)

                if color_existente is None:
                    lista_colors.agregar_color(nuevo_color)

    def mostrar_posicion_pieza(self, fila_inicial, columna_inicial, color, fila, columna, lista_colors):
        
        print("## PIEZA COLOCADA CON EXITO EN: ##\n")
        print("## TABLERO ##")

        
        for columnas in range(1, int(fila_inicial) + 1):
            tablero = ""
            for filas in range(1, int(columna_inicial) + 1):
                piece_found = False
                for colores in lista_colors:
                    if int(colores.fila) == columnas and int(colores.columna) == filas:
                        tablero += f"| {colores.color} "
                        piece_found = True
                        break
                
                if not piece_found:
                    tablero += "|   "
            print(tablero + "|")


    def mostrar_trablero_inicial(self, fila_inicial, columna_inicial):
        tablero = ""
            
        for columnas in range(1, int(fila_inicial)+1):
            for filas in range(0, int(columna_inicial)+1):
                    #if filas  < int(fila_inicial):
                        #tablero += "-----"
                tablero += "|   "

            tablero += "\n"

        print(tablero)

    def agregar_piezasasd(self):
        pass

    def validar_fila_columna(self, tipo, valor, rango):
        if tipo == "fila":
            if int(valor) >= 1 and int(valor) <= int(rango):
                return True
            return False
        elif tipo == "columna":
            if int(valor) >= 1 and int(valor) <= int(rango):
                return True
            return False

    def obtener_color(self, color):
        if color == "1":
            return "A", "AZUL", "#84b6f4"
        elif color == "2":
            return "R", "ROJO", "#ff6961"
        elif color == "3":
            return "V", "VERDE", "#77dd77"
        elif color == "4":
            return "P", "PÚRPURA", "#b0c2f2"
        elif color == "5":
            return "N", "NARANJA", "#ffda9e"
        else:
            print("DATO INGRESADO NO VALIDO")
            return False, False

    def colores(self):
        print(" 1. AZUL")
        print(" 2. ROJO")
        print(" 3. VERDE")
        print(" 4. PÚRPURA")
        print(" 5. NARANJA")