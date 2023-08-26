from nodo import nodo
import os

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

    def generar_grafica(self, nombre_grafica):
        text = ""
        f = open('bb.dot', 'w')
        actual = self.primero

        text = """digraph G {
	            a0 [ label="Colorealo Guatemattel" fontname="Courier New" ] 

                a2 [ shape="none" fontname="Courier New" label=< <TABLE  border="0" cellspacing="10" cellpadding="10" bgcolor="white">
                <TR>
                    <TD shape="circle" border="1" bgcolor="white">0</TD>\n"""
        
        for col in range(1, int(actual.dato.columnas)+1):
            text += f"""<TD shape="circle" border="1" bgcolor="white">{col}</TD>\n"""

        text += "</TR>"

        text += actual.dato.colores.generar_text_grafica()+"\n"+"""</TABLE>>]
                        a0 -> a2;
                }"""
        f.write(text)
        f.close()
        os.environ["PATH"] += os.pathsep + 'C:/Program Files/Graphviz/bin'
        os.system(f'dot -Tpng bb.dot -o {nombre_grafica}.png')
        print("## GRAFICA DEL TABLERO CREADA #")

    def mostrar_lista(self):
        actual = self.primero
        while actual != None:
            print("TABLERO")
            print("Filas:", actual.dato.filas, "| Columnas:", actual.dato.columnas)
            print("Colores:")
            actual.dato.colores.mostrar_lista()
            actual = actual.siguiente