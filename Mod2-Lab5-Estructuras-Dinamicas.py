import time

print("." * 52)
print("UNIVERSIDAD DE PANAMÁ")
print("FACULTAD DE INFORMÁTICA, ELECTRÓNICA Y COMUNICACIÓN")
print("TÉCNICO DE COMUNICACIONES - FIEC")
print("ESTRUCTURA DE DATOS - INF222")
print("LABORATORIO N.º 5: LISTA ENLAZADA SIMPLE")
print("Desarrollado por: Justiniano Figueroa")
print("Profesor: Ángel Ávila")
print("Segundo semestre")
print("=" * 52)


class Nodo:
    def __init__(self, dato):
        self.dato = dato
        self.siguiente = None


class ListaEnlazada:
    def __init__(self):
        self.cabeza = None

    def esta_vacia(self):
        return self.cabeza is None

    def insertar_inicio(self, dato):
        nuevo = Nodo(dato)
        nuevo.siguiente = self.cabeza
        self.cabeza = nuevo

    def insertar_final(self, dato):
        nuevo = Nodo(dato)
        if self.cabeza is None:
            self.cabeza = nuevo
            return
        actual = self.cabeza
        while actual.siguiente is not None:
            actual = actual.siguiente
        actual.siguiente = nuevo

    def insertar_en_posicion(self, pos, dato):
        if pos < 0 or pos > self.longitud():
            raise IndexError("Posición fuera de rango")
        if pos == 0:
            self.insertar_inicio(dato)
            return
        actual = self.cabeza
        for i in range(pos - 1):
            actual = actual.siguiente
        nuevo = Nodo(dato)
        nuevo.siguiente = actual.siguiente
        actual.siguiente = nuevo

    def eliminar(self, dato):
        if self.cabeza is None:
            return False
        if self.cabeza.dato == dato:
            self.cabeza = self.cabeza.siguiente
            return True
        anterior = self.cabeza
        actual = self.cabeza.siguiente
        while actual is not None:
            if actual.dato == dato:
                anterior.siguiente = actual.siguiente
                return True
            anterior = actual
            actual = actual.siguiente
        return False

    def eliminar_posicion(self, pos):
        if pos < 0 or pos >= self.longitud():
            raise IndexError("Posición fuera de rango")
        if pos == 0:
            dato = self.cabeza.dato
            self.cabeza = self.cabeza.siguiente
            return dato
        anterior = self.cabeza
        for i in range(pos - 1):
            anterior = anterior.siguiente
        borrado = anterior.siguiente
        anterior.siguiente = borrado.siguiente
        return borrado.dato

    def buscar(self, dato):
        actual = self.cabeza
        posicion = 0
        while actual is not None:
            if actual.dato == dato:
                return posicion
            actual = actual.siguiente
            posicion += 1
        return -1

    def longitud(self):
        contador = 0
        actual = self.cabeza
        while actual is not None:
            contador += 1
            actual = actual.siguiente
        return contador

    def recorrer(self):
        datos = []
        actual = self.cabeza
        while actual is not None:
            datos.append(actual.dato)
            actual = actual.siguiente
        return datos

    def obtener(self, indice):
        if indice < 0:
            raise IndexError("Índice fuera de rango")
        actual = self.cabeza
        contador = 0
        while actual is not None:
            if contador == indice:
                return actual.dato
            actual = actual.siguiente
            contador += 1
        raise IndexError("Índice fuera de rango")

    def invertir(self):
        anterior = None
        actual = self.cabeza
        while actual is not None:
            siguiente = actual.siguiente
            actual.siguiente = anterior
            anterior = actual
            actual = siguiente
        self.cabeza = anterior

    def __str__(self):
        if self.cabeza is None:
            return "(lista vacía)"
        partes = []
        actual = self.cabeza
        while actual is not None:
            partes.append(str(actual.dato))
            actual = actual.siguiente
        return " -> ".join(partes) + " -> None"


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


def pruebas_basicas():
    print("\n--- Operaciones básicas ---")
    lista = ListaEnlazada()
    lista.insertar_inicio(20)
    lista.insertar_inicio(10)
    lista.insertar_final(30)
    lista.insertar_final(40)
    lista.insertar_en_posicion(2, 25)
    print("Lista:", lista)
    verificar("insertar al inicio, al final y en posición", lista.recorrer(), [10, 20, 25, 30, 40])
    verificar("longitud", lista.longitud(), 5)
    verificar("buscar un dato que existe", lista.buscar(30), 3)
    verificar("buscar un dato que no existe", lista.buscar(99), -1)

    verificar("eliminar el primero", lista.eliminar(10), True)
    verificar("lista después de eliminar el primero", lista.recorrer(), [20, 25, 30, 40])
    verificar("eliminar uno del medio", lista.eliminar(25), True)
    verificar("lista después de eliminar el del medio", lista.recorrer(), [20, 30, 40])
    verificar("eliminar el último", lista.eliminar(40), True)
    verificar("lista después de eliminar el último", lista.recorrer(), [20, 30])
    verificar("eliminar un dato que no existe", lista.eliminar(99), False)
    verificar("la lista no cambia si el dato no existe", lista.recorrer(), [20, 30])

    verificar("eliminar por posición devuelve el dato", lista.eliminar_posicion(1), 30)
    verificar("lista después de eliminar por posición", lista.recorrer(), [20])
    print("Lista final:", lista)


def pruebas_casos_borde():
    print("\n--- Casos borde ---")
    vacia = ListaEnlazada()
    print("Lista vacía:", vacia)
    verificar("lista vacía: esta_vacia", vacia.esta_vacia(), True)
    verificar("lista vacía: longitud", vacia.longitud(), 0)
    verificar("lista vacía: buscar", vacia.buscar(5), -1)
    verificar("lista vacía: eliminar", vacia.eliminar(5), False)
    verificar("lista vacía: recorrer", vacia.recorrer(), [])
    verificar("lista vacía: obtener da error", lanza_error(lambda: vacia.obtener(0)), True)
    verificar("lista vacía: eliminar_posicion da error", lanza_error(lambda: vacia.eliminar_posicion(0)), True)
    vacia.invertir()
    verificar("lista vacía: invertir no falla", vacia.recorrer(), [])

    uno = ListaEnlazada()
    uno.insertar_final(7)
    print("Un solo elemento:", uno)
    verificar("un elemento: longitud", uno.longitud(), 1)
    uno.invertir()
    verificar("un elemento: invertir", uno.recorrer(), [7])
    verificar("un elemento: obtener(0)", uno.obtener(0), 7)
    verificar("un elemento: eliminar", uno.eliminar(7), True)
    verificar("un elemento: queda vacía", uno.esta_vacia(), True)

    lista = ListaEnlazada()
    for numero in (1, 2, 3):
        lista.insertar_final(numero)
    verificar("insertar en posición mayor a la longitud da error", lanza_error(lambda: lista.insertar_en_posicion(5, 99)), True)
    verificar("insertar en posición negativa da error", lanza_error(lambda: lista.insertar_en_posicion(-1, 99)), True)
    verificar("eliminar_posicion fuera de rango da error", lanza_error(lambda: lista.eliminar_posicion(3)), True)
    lista.insertar_en_posicion(3, 4)
    verificar("insertar justo al final con insertar_en_posicion", lista.recorrer(), [1, 2, 3, 4])
    lista.insertar_en_posicion(0, 0)
    verificar("insertar en la posición 0", lista.recorrer(), [0, 1, 2, 3, 4])


def pruebas_tarea():
    print("\n--- Tarea: invertir() y obtener() ---")
    lista = ListaEnlazada()
    for numero in (1, 2, 3, 4, 5):
        lista.insertar_final(numero)
    print("Antes de invertir:", lista)

    nodos_antes = []
    actual = lista.cabeza
    while actual is not None:
        nodos_antes.append(actual)
        actual = actual.siguiente

    lista.invertir()
    print("Después de invertir:", lista)
    verificar("invertir deja la lista al revés", lista.recorrer(), [5, 4, 3, 2, 1])

    nodos_despues = []
    actual = lista.cabeza
    while actual is not None:
        nodos_despues.append(actual)
        actual = actual.siguiente
    mismos = [id(n) for n in nodos_despues] == [id(n) for n in reversed(nodos_antes)]
    verificar("invertir usa los mismos nodos (no crea nuevos)", mismos, True)

    lista.invertir()
    verificar("invertir dos veces deja la lista original", lista.recorrer(), [1, 2, 3, 4, 5])

    verificar("obtener(0)", lista.obtener(0), 1)
    verificar("obtener(2)", lista.obtener(2), 3)
    verificar("obtener(4)", lista.obtener(4), 5)
    verificar("obtener(5) da error", lanza_error(lambda: lista.obtener(5)), True)
    verificar("obtener(-1) da error", lanza_error(lambda: lista.obtener(-1)), True)


def comparar_tiempos():
    print("\n--- Tiempos: insertar al inicio ---")
    print("Lista de Python (insert(0, x)) contra lista enlazada (insertar_inicio)")
    print()
    print(f"{'Cantidad':>10} {'Lista Python (s)':>18} {'Lista enlazada (s)':>20} {'Más rápida':>14}")
    for cantidad in (5000, 10000, 20000, 50000, 100000):
        inicio = time.perf_counter()
        lista_python = []
        for i in range(cantidad):
            lista_python.insert(0, i)
        tiempo_python = time.perf_counter() - inicio

        inicio = time.perf_counter()
        lista_enlazada = ListaEnlazada()
        for i in range(cantidad):
            lista_enlazada.insertar_inicio(i)
        tiempo_enlazada = time.perf_counter() - inicio

        if tiempo_enlazada < tiempo_python:
            ganadora = "enlazada"
        else:
            ganadora = "Python"
        print(f"{cantidad:>10} {tiempo_python:>18.4f} {tiempo_enlazada:>20.4f} {ganadora:>14}")


if __name__ == "__main__":
    pruebas_basicas()
    pruebas_casos_borde()
    pruebas_tarea()
    comparar_tiempos()

    print("\n" + "=" * 52)
    print("Pruebas correctas:", aciertos)
    print("Pruebas con fallo:", fallos)
    print("=" * 52)
    input("\nPresiona ENTER para salir...")
