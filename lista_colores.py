from nodo import nodo

class lista_colores:
    def __init__(self):
        self.primero = None
        self.size = 0

    def agregar_color(self, color):
        nuevo_nodo = nodo(dato = color)

        if self.size == 0:
            self.primero = nuevo_nodo
            self.ultimo = nuevo_nodo
        else:
            actual = self.primero
            anterior = None
            while actual is not None and (int(actual.dato.fila), int(actual.dato.columna)) < (int(nuevo_nodo.dato.fila), int(nuevo_nodo.dato.columna)):
                anterior = actual
                actual = actual.siguiente
            if anterior is None:
                nuevo_nodo.siguiente = self.primero
                self.primero = nuevo_nodo
            else:
                nuevo_nodo.siguiente = actual
                anterior.siguiente = nuevo_nodo

        self.size += 1

    def buscar_color(self, fila, columna):
        actual = self.primero
        while actual is not None:
            if int(actual.dato.fila) == int(fila) and int(actual.dato.columna) == int(columna):
                return actual.dato
            actual = actual.siguiente
        return None

    def generar_text_grafica(self):
        datos = ""
        actual = self.primero
        contador = 1
        datos += f"""<TR>\n<TD border="1" bgcolor="white">{contador}</TD>\n"""
        sentinela = actual.dato.fila
        fila_ = False
        while actual != None:
            if int(sentinela) != int(actual.dato.fila):
                contador += 1
                sentinela = actual.dato.fila
                fila_ = False
                datos += f"""</TR>\n<TR>\n<TD border="1" bgcolor="white">{contador}</TD>\n"""
            if fila_ == False:
                fila_ = True
                datos += f"""<TD border="1" bgcolor="{actual.dato.codigo}"> </TD>\n"""
            else:
                datos += f"""<TD border="1" bgcolor="{actual.dato.codigo}"> </TD>\n"""
            
            actual = actual.siguiente
        datos += "</TR>"
        return datos

    def __iter__(self):
        self.actual = self.primero
        return self

    def __next__(self):
        if self.actual is not None:
            valor_actual = self.actual.dato
            self.actual = self.actual.siguiente
            return valor_actual
        else:
            raise StopIteration

    

    def size(self):
        return self.size

    def mostrar_lista(self):
        actual = self.primero
        print("TOTAL:", self.size)
        while actual != None:
            
            print("Color:", actual.dato.color, "| Fila:", actual.dato.fila, "| Columna:", actual.dato.columna)
            actual = actual.siguiente