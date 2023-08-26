from nodo import nodo

class lista_tablero:
    def __init__(self):
        self.primero = None
        self.size = 0

    def agregar_tablero(self, tablero_):
        nuevo_nodo = nodo(dato = tablero_)

        if self.primero is None:
            self.primero = nuevo_nodo
            self.size += 1
            return
        
        actual = self.primero
        while actual.siguiente:
            actual = actual.siguiente
        
        actual.siguiente = nuevo_nodo
        self.size += 1

    def mostrar_lista(self):
        actual = self.primero
        while actual != None:
            print("TABLERO")
            print("Filas:", actual.dato.filas, "| Columnas:", actual.dato.columnas)
            actual = actual.siguiente