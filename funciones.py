from lista_tablero import lista_tablero
from tablero import tablero
class funciones:
    def __init__(self):
        self.lista_tab = lista_tablero()

    def agregar_tablero(self, filas_, columnas_):
        
        nuevo = tablero(filas_, columnas_, "lolo")
        self.lista_tab.agregar_tablero(nuevo)
        print("¡TABLERO CREADO!")
        self.lista_tab.mostrar_lista()
