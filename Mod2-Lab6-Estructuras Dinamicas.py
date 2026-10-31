print("." * 52)
print("UNIVERSIDAD DE PANAMÁ")
print("FACULTAD DE INFORMÁTICA, ELECTRÓNICA Y COMUNICACIÓN")
print("TÉCNICO DE COMUNICACIONES - FIEC")
print("ESTRUCTURA DE DATOS - INF222")
print("LABORATORIO N.º 6: LISTA CIRCULAR")
print("Desarrollado por: Justiniano Figueroa")
print("Profesor: Ángel Ávila")
print("Segundo semestre")
print("=" * 52)


class Nodo:
    def __init__(self, dato):
        self.dato = dato
        self.siguiente = None


class ListaCircular:
    def __init__(self):
        self.cabeza = None

    def esta_vacia(self):
        return self.cabeza is None

    def insertar_inicio(self, dato):
        nuevo = Nodo(dato)
        if self.cabeza is None:
            nuevo.siguiente = nuevo
            self.cabeza = nuevo
            return
        ultimo = self.cabeza
        while ultimo.siguiente is not self.cabeza:
            ultimo = ultimo.siguiente
        nuevo.siguiente = self.cabeza
        ultimo.siguiente = nuevo
        self.cabeza = nuevo

    def insertar_final(self, dato):
        nuevo = Nodo(dato)
        if self.cabeza is None:
            nuevo.siguiente = nuevo
            self.cabeza = nuevo
            return
        ultimo = self.cabeza
        while ultimo.siguiente is not self.cabeza:
            ultimo = ultimo.siguiente
        ultimo.siguiente = nuevo
        nuevo.siguiente = self.cabeza

    def eliminar(self, dato):
        if self.cabeza is None:
            return False
        if self.cabeza.siguiente is self.cabeza:
            if self.cabeza.dato == dato:
                self.cabeza = None
                return True
            return False
        ultimo = self.cabeza
        while ultimo.siguiente is not self.cabeza:
            ultimo = ultimo.siguiente
        if self.cabeza.dato == dato:
            self.cabeza = self.cabeza.siguiente
            ultimo.siguiente = self.cabeza
            return True
        anterior = self.cabeza
        actual = self.cabeza.siguiente
        while actual is not self.cabeza:
            if actual.dato == dato:
                anterior.siguiente = actual.siguiente
                return True
            anterior = actual
            actual = actual.siguiente
        return False

    def buscar(self, dato):
        if self.cabeza is None:
            return -1
        actual = self.cabeza
        posicion = 0
        while True:
            if actual.dato == dato:
                return posicion
            actual = actual.siguiente
            posicion += 1
            if actual is self.cabeza:
                return -1

    def longitud(self):
        if self.cabeza is None:
            return 0
        contador = 1
        actual = self.cabeza.siguiente
        while actual is not self.cabeza:
            contador += 1
            actual = actual.siguiente
        return contador

    def recorrer(self):
        datos = []
        if self.cabeza is None:
            return datos
        datos.append(self.cabeza.dato)
        actual = self.cabeza.siguiente
        while actual is not self.cabeza:
            datos.append(actual.dato)
            actual = actual.siguiente
        return datos

    def avanzar(self):
        if self.cabeza is None:
            raise IndexError("La lista está vacía")
        dato = self.cabeza.dato
        self.cabeza = self.cabeza.siguiente
        return dato

    def __str__(self):
        if self.cabeza is None:
            return "(lista vacía)"
        partes = []
        for dato in self.recorrer():
            partes.append(str(dato))
        return " -> ".join(partes) + " -> (vuelve a " + str(self.cabeza.dato) + ")"


aciertos = 0
fallos = 0


def verificar(descripcion, resultado, esperado):
    global aciertos, fallos
    if resultado == esperado:
        aciertos += 1
        print("  OK     ", descripcion)
    else:
        fallos += 1
        print("  FALLO  ", descripcion, "| se obtuvo", resultado, "y se esperaba", esperado)


def lanza_error(funcion):
    try:
        funcion()
    except IndexError:
        return True
    return False


def dar_vueltas(lista, pasos):
    resultado = []
    for i in range(pasos):
        resultado.append(lista.avanzar())
    return resultado


def pruebas_basicas():
    print("\n--- Operaciones básicas ---")
    lista = ListaCircular()
    lista.insertar_final(20)
    lista.insertar_final(30)
    lista.insertar_inicio(10)
    print("Lista:", lista)
    verificar("insertar al inicio y al final", lista.recorrer(), [10, 20, 30])
    verificar("longitud", lista.longitud(), 3)
    verificar("buscar un dato que existe", lista.buscar(30), 2)
    verificar("buscar un dato que no existe", lista.buscar(99), -1)
    verificar("el último apunta a la cabeza (dos vueltas)", dar_vueltas(lista, 6), [10, 20, 30, 10, 20, 30])

    verificar("eliminar uno del medio", lista.eliminar(20), True)
    verificar("lista después de eliminar el del medio", lista.recorrer(), [10, 30])
    verificar("eliminar el último", lista.eliminar(30), True)
    verificar("lista después de eliminar el último", lista.recorrer(), [10])
    verificar("eliminar un dato que no existe", lista.eliminar(99), False)
    verificar("eliminar el único elemento", lista.eliminar(10), True)
    verificar("la lista queda vacía", lista.esta_vacia(), True)

    otra = ListaCircular()
    for numero in (1, 2, 3):
        otra.insertar_final(numero)
    verificar("eliminar la cabeza", otra.eliminar(1), True)
    verificar("lista después de eliminar la cabeza", otra.recorrer(), [2, 3])
    verificar("sigue siendo circular después de eliminar la cabeza", dar_vueltas(otra, 4), [2, 3, 2, 3])
    print("Lista final:", otra)


def pruebas_casos_borde():
    print("\n--- Casos borde ---")
    vacia = ListaCircular()
    print("Lista vacía:", vacia)
    verificar("lista vacía: esta_vacia", vacia.esta_vacia(), True)
    verificar("lista vacía: longitud", vacia.longitud(), 0)
    verificar("lista vacía: buscar", vacia.buscar(5), -1)
    verificar("lista vacía: eliminar", vacia.eliminar(5), False)
    verificar("lista vacía: recorrer", vacia.recorrer(), [])
    verificar("lista vacía: avanzar da error", lanza_error(vacia.avanzar), True)

    uno = ListaCircular()
    uno.insertar_inicio(5)
    print("Un solo elemento:", uno)
    verificar("un elemento: longitud", uno.longitud(), 1)
    verificar("un elemento: apunta a sí mismo", uno.cabeza.siguiente is uno.cabeza, True)
    verificar("un elemento: avanzar siempre da el mismo", dar_vueltas(uno, 3), [5, 5, 5])
    verificar("un elemento: buscar", uno.buscar(5), 0)
    verificar("un elemento: eliminar", uno.eliminar(5), True)
    verificar("un elemento: queda vacía", uno.esta_vacia(), True)

    uno.insertar_final(8)
    verificar("insertar_final en lista vacía", uno.recorrer(), [8])
    verificar("insertar_final en lista vacía es circular", uno.cabeza.siguiente is uno.cabeza, True)

    repetidos = ListaCircular()
    for numero in (4, 7, 4):
        repetidos.insertar_final(numero)
    verificar("datos repetidos: eliminar quita el primero", repetidos.eliminar(4), True)
    verificar("datos repetidos: queda el otro", repetidos.recorrer(), [7, 4])


def demo_turnos():
    print("\n--- Demostración: turnos con lista circular ---")
    turnos = ListaCircular()
    for nombre in ("Ana", "Luis", "Marta"):
        turnos.insertar_final(nombre)
    print("Participantes:", turnos)
    for numero in range(1, 8):
        print("Turno", numero, "->", turnos.avanzar())


if __name__ == "__main__":
    pruebas_basicas()
    pruebas_casos_borde()
    demo_turnos()

    print("\n" + "=" * 52)
    print("Pruebas correctas:", aciertos)
    print("Pruebas con fallo:", fallos)
    print("=" * 52)
    input("\nPresiona ENTER para salir...")
