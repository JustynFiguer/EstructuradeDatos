class NodoDoble:
    def __init__(self, dato):
        self.dato = dato
        self.anterior = None
        self.siguiente = None


class ListaDoblementeEnlazada:
    def __init__(self):
        self._cabeza = None
        self._cola = None
        self._tamanio = 0

    def insertar_inicio(self, dato):
        nuevo = NodoDoble(dato)
        if self._cabeza is None:
            self._cabeza = nuevo
            self._cola = nuevo
        else:
            nuevo.siguiente = self._cabeza
            self._cabeza.anterior = nuevo
            self._cabeza = nuevo
        self._tamanio += 1

    def insertar_final(self, dato):
        nuevo = NodoDoble(dato)
        if self._cola is None:
            self._cabeza = nuevo
            self._cola = nuevo
        else:
            nuevo.anterior = self._cola
            self._cola.siguiente = nuevo
            self._cola = nuevo
        self._tamanio += 1

    def insertar_en_posicion(self, posicion, dato):
        if posicion < 0:
            raise IndexError("La posición no puede ser negativa")
        if posicion == 0:
            self.insertar_inicio(dato)
            return
        if posicion >= self._tamanio:
            self.insertar_final(dato)
            return

        actual = self._cabeza
        for _ in range(posicion):
            actual = actual.siguiente

        nuevo = NodoDoble(dato)
        anterior = actual.anterior
        nuevo.anterior = anterior
        nuevo.siguiente = actual
        anterior.siguiente = nuevo
        actual.anterior = nuevo
        self._tamanio += 1

    def eliminar_inicio(self):
        if self._cabeza is None:
            raise IndexError("La lista está vacía")

        dato = self._cabeza.dato
        if self._cabeza == self._cola:
            self._cabeza = None
            self._cola = None
        else:
            self._cabeza = self._cabeza.siguiente
            self._cabeza.anterior = None

        self._tamanio -= 1
        return dato

    def eliminar_final(self):
        if self._cola is None:
            raise IndexError("La lista está vacía")

        dato = self._cola.dato
        if self._cabeza == self._cola:
            self._cabeza = None
            self._cola = None
        else:
            self._cola = self._cola.anterior
            self._cola.siguiente = None

        self._tamanio -= 1
        return dato

    def eliminar(self, dato):
        actual = self._cabeza

        while actual is not None:
            if actual.dato == dato:
                if actual == self._cabeza:
                    self.eliminar_inicio()
                elif actual == self._cola:
                    self.eliminar_final()
                else:
                    actual.anterior.siguiente = actual.siguiente
                    actual.siguiente.anterior = actual.anterior
                    self._tamanio -= 1
                return True
            actual = actual.siguiente

        return False

    def recorrer_adelante(self):
        resultado = []
        actual = self._cabeza
        while actual is not None:
            resultado.append(actual.dato)
            actual = actual.siguiente
        return resultado

    def recorrer_atras(self):
        resultado = []
        actual = self._cola
        while actual is not None:
            resultado.append(actual.dato)
            actual = actual.anterior
        return resultado

    def tamanio(self):
        return self._tamanio

    def es_vacia(self):
        return self._cabeza is None

    def __str__(self):
        datos = self.recorrer_adelante()
        return "None <- " + " <-> ".join(str(dato) for dato in datos) + " -> None"


def ejecutar_pruebas():
    print("=" * 68)
    print("                 UNIVERSIDAD DE PANAMÁ")
    print(" FACULTAD DE INFORMÁTICA, ELECTRÓNICA Y COMUNICACIÓN (FIEC)")
    print("         DESARROLLADO POR: JUSTINIANO FIGUEROA")
    print("             ASIGNATURA: ESTRUCTURA DE DATOS")
    print("                 PROFESOR: ÁNGEL ÁVILA")
    print("=" * 68)
    print("          LABORATORIO 7 - LISTA DOBLEMENTE ENLAZADA")
    print("=" * 68)

    lista = ListaDoblementeEnlazada()

    print("\n1. Insertar al inicio y al final")
    lista.insertar_inicio(20)
    lista.insertar_inicio(10)
    lista.insertar_final(30)
    lista.insertar_final(40)
    print("Lista:", lista)
    print("Recorrido hacia atrás:", lista.recorrer_atras())

    print("\n2. Insertar en la posición 2")
    lista.insertar_en_posicion(2, 25)
    print("Lista:", lista)

    print("\n3. Consultar tamaño")
    print("Tamaño:", lista.tamanio())

    print("\n4. Eliminar el primer elemento")
    print("Eliminado:", lista.eliminar_inicio())
    print("Lista:", lista)

    print("\n5. Eliminar el último elemento")
    print("Eliminado:", lista.eliminar_final())
    print("Lista:", lista)

    print("\n6. Eliminar el valor 25")
    print("¿Se encontró?:", lista.eliminar(25))
    print("Lista:", lista)

    print("\n7. Buscar un valor que no existe")
    print("¿Se encontró el 99?:", lista.eliminar(99))

    print("\n8. Verificar recorridos")
    adelante = lista.recorrer_adelante()
    atras = lista.recorrer_atras()
    print("Hacia adelante:", adelante)
    print("Hacia atrás:", atras)
    print("¿La lista está consistente?:", adelante == list(reversed(atras)))
    print("Tamaño final:", lista.tamanio())


if __name__ == "__main__":
    try:
        ejecutar_pruebas()
    except Exception as error:
        print("\nOcurrió un error:", error)
    finally:
        print("\nEjecución finalizada.")
        try:
            input("Presiona ENTER para cerrar...")
        except EOFError:
            pass
