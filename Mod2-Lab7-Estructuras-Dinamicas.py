print("." * 52)
print("UNIVERSIDAD DE PANAMÁ")
print("FACULTAD DE INFORMÁTICA, ELECTRÓNICA Y COMUNICACIÓN")
print("TÉCNICO DE COMUNICACIONES - FIEC")
print("ESTRUCTURA DE DATOS - INF222")
print("LABORATORIO N.º 7: LISTA DOBLEMENTE ENLAZADA")
print("Desarrollado por: Justiniano Figueroa")
print("Profesor: Ángel Ávila")
print("Segundo semestre")
print("=" * 52)


class Nodo:
    def __init__(self, dato):
        self.dato = dato
        self.anterior = None
        self.siguiente = None


class ListaDoblementeEnlazada:
    def __init__(self):
        self.cabeza = None
        self.cola = None

    def esta_vacia(self):
        return self.cabeza is None

    def insertar_inicio(self, dato):
        nuevo = Nodo(dato)
        if self.cabeza is None:
            self.cabeza = nuevo
            self.cola = nuevo
        else:
            nuevo.siguiente = self.cabeza
            self.cabeza.anterior = nuevo
            self.cabeza = nuevo

    def insertar_final(self, dato):
        nuevo = Nodo(dato)
        if self.cola is None:
            self.cabeza = nuevo
            self.cola = nuevo
        else:
            nuevo.anterior = self.cola
            self.cola.siguiente = nuevo
            self.cola = nuevo

    def insertar_en_posicion(self, pos, dato):
        total = self.longitud()
        if pos < 0 or pos > total:
            raise IndexError("Posición fuera de rango")
        if pos == 0:
            self.insertar_inicio(dato)
            return
        if pos == total:
            self.insertar_final(dato)
            return
        actual = self.cabeza
        for i in range(pos):
            actual = actual.siguiente
        nuevo = Nodo(dato)
        nuevo.anterior = actual.anterior
        nuevo.siguiente = actual
        actual.anterior.siguiente = nuevo
        actual.anterior = nuevo

    def quitar_nodo(self, nodo):
        if nodo.anterior is None:
            self.cabeza = nodo.siguiente
        else:
            nodo.anterior.siguiente = nodo.siguiente
        if nodo.siguiente is None:
            self.cola = nodo.anterior
        else:
            nodo.siguiente.anterior = nodo.anterior

    def eliminar_inicio(self):
        if self.cabeza is None:
            raise IndexError("La lista está vacía")
        dato = self.cabeza.dato
        self.quitar_nodo(self.cabeza)
        return dato

    def eliminar_final(self):
        if self.cola is None:
            raise IndexError("La lista está vacía")
        dato = self.cola.dato
        self.quitar_nodo(self.cola)
        return dato

    def eliminar(self, dato):
        actual = self.cabeza
        while actual is not None:
            if actual.dato == dato:
                self.quitar_nodo(actual)
                return True
            actual = actual.siguiente
        return False

    def eliminar_posicion(self, pos):
        if pos < 0 or pos >= self.longitud():
            raise IndexError("Posición fuera de rango")
        actual = self.cabeza
        for i in range(pos):
            actual = actual.siguiente
        dato = actual.dato
        self.quitar_nodo(actual)
        return dato

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

    def recorrer_adelante(self):
        datos = []
        actual = self.cabeza
        while actual is not None:
            datos.append(actual.dato)
            actual = actual.siguiente
        return datos

    def recorrer_atras(self):
        datos = []
        actual = self.cola
        while actual is not None:
            datos.append(actual.dato)
            actual = actual.anterior
        return datos

    def __str__(self):
        if self.cabeza is None:
            return "(lista vacía)"
        partes = []
        for dato in self.recorrer_adelante():
            partes.append(str(dato))
        return "None <-> " + " <-> ".join(partes) + " <-> None"


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


def enlaces_bien(lista):
    if lista.cabeza is None:
        return lista.cola is None
    if lista.cabeza.anterior is not None:
        return False
    if lista.cola.siguiente is not None:
        return False
    actual = lista.cabeza
    while actual.siguiente is not None:
        if actual.siguiente.anterior is not actual:
            return False
        actual = actual.siguiente
    return actual is lista.cola


def pruebas_basicas():
    print("\n--- Operaciones básicas ---")
    lista = ListaDoblementeEnlazada()
    lista.insertar_final(2)
    lista.insertar_final(3)
    lista.insertar_inicio(1)
    print("Lista:", lista)
    verificar("recorrer hacia adelante", lista.recorrer_adelante(), [1, 2, 3])
    verificar("recorrer hacia atrás", lista.recorrer_atras(), [3, 2, 1])
    verificar("enlaces correctos", enlaces_bien(lista), True)

    lista.insertar_inicio(0)
    verificar("insertar 0 al inicio", lista.recorrer_adelante(), [0, 1, 2, 3])
    lista.insertar_en_posicion(2, 15)
    verificar("insertar en posición intermedia", lista.recorrer_adelante(), [0, 1, 15, 2, 3])
    verificar("hacia atrás después de insertar en el medio", lista.recorrer_atras(), [3, 2, 15, 1, 0])
    verificar("enlaces correctos después de insertar", enlaces_bien(lista), True)
    verificar("longitud", lista.longitud(), 5)
    verificar("buscar un dato que existe", lista.buscar(2), 3)
    verificar("buscar un dato que no existe", lista.buscar(99), -1)

    verificar("eliminar un nodo del medio", lista.eliminar(15), True)
    verificar("lista después de eliminar el del medio", lista.recorrer_adelante(), [0, 1, 2, 3])
    verificar("eliminar el nodo 2", lista.eliminar(2), True)
    verificar("lista después de eliminar el 2", lista.recorrer_adelante(), [0, 1, 3])
    verificar("hacia atrás después de eliminar el 2", lista.recorrer_atras(), [3, 1, 0])
    verificar("eliminar un dato que no existe", lista.eliminar(99), False)
    verificar("eliminar_inicio devuelve el dato", lista.eliminar_inicio(), 0)
    verificar("eliminar_final devuelve el dato", lista.eliminar_final(), 3)
    verificar("lista después de eliminar los extremos", lista.recorrer_adelante(), [1])
    verificar("enlaces correctos después de eliminar", enlaces_bien(lista), True)

    otra = ListaDoblementeEnlazada()
    for numero in (10, 20, 30, 40):
        otra.insertar_final(numero)
    verificar("eliminar por posición devuelve el dato", otra.eliminar_posicion(2), 30)
    verificar("lista después de eliminar por posición", otra.recorrer_adelante(), [10, 20, 40])
    verificar("eliminar la posición 0", otra.eliminar_posicion(0), 10)
    verificar("eliminar la última posición", otra.eliminar_posicion(1), 40)
    verificar("queda un solo dato", otra.recorrer_adelante(), [20])
    verificar("enlaces correctos al final", enlaces_bien(otra), True)


def pruebas_casos_borde():
    print("\n--- Casos borde ---")
    vacia = ListaDoblementeEnlazada()
    print("Lista vacía:", vacia)
    verificar("lista vacía: esta_vacia", vacia.esta_vacia(), True)
    verificar("lista vacía: longitud", vacia.longitud(), 0)
    verificar("lista vacía: buscar", vacia.buscar(5), -1)
    verificar("lista vacía: eliminar", vacia.eliminar(5), False)
    verificar("lista vacía: adelante", vacia.recorrer_adelante(), [])
    verificar("lista vacía: atrás", vacia.recorrer_atras(), [])
    verificar("lista vacía: eliminar_inicio da error", lanza_error(vacia.eliminar_inicio), True)
    verificar("lista vacía: eliminar_final da error", lanza_error(vacia.eliminar_final), True)
    verificar("lista vacía: eliminar_posicion da error", lanza_error(lambda: vacia.eliminar_posicion(0)), True)

    uno = ListaDoblementeEnlazada()
    uno.insertar_final(7)
    print("Un solo elemento:", uno)
    verificar("un elemento: cabeza y cola son el mismo nodo", uno.cabeza is uno.cola, True)
    verificar("un elemento: adelante y atrás iguales", uno.recorrer_adelante() == uno.recorrer_atras(), True)
    verificar("un elemento: eliminar_final", uno.eliminar_final(), 7)
    verificar("un elemento: queda vacía", uno.esta_vacia() and uno.cola is None, True)

    uno.insertar_inicio(8)
    verificar("insertar_inicio en lista vacía", uno.recorrer_adelante(), [8])
    verificar("un elemento: eliminar_inicio", uno.eliminar_inicio(), 8)
    verificar("queda vacía otra vez", uno.esta_vacia(), True)

    lista = ListaDoblementeEnlazada()
    for numero in (1, 2, 3):
        lista.insertar_final(numero)
    verificar("insertar en posición mayor a la longitud da error", lanza_error(lambda: lista.insertar_en_posicion(5, 99)), True)
    verificar("insertar en posición negativa da error", lanza_error(lambda: lista.insertar_en_posicion(-1, 99)), True)
    verificar("eliminar_posicion fuera de rango da error", lanza_error(lambda: lista.eliminar_posicion(3)), True)
    lista.insertar_en_posicion(3, 4)
    verificar("insertar justo al final con insertar_en_posicion", lista.recorrer_adelante(), [1, 2, 3, 4])
    lista.insertar_en_posicion(0, 0)
    verificar("insertar en la posición 0", lista.recorrer_adelante(), [0, 1, 2, 3, 4])
    verificar("enlaces correctos", enlaces_bien(lista), True)

    repetidos = ListaDoblementeEnlazada()
    for numero in (4, 7, 4):
        repetidos.insertar_final(numero)
    verificar("datos repetidos: eliminar quita el primero", repetidos.eliminar(4), True)
    verificar("datos repetidos: queda el otro", repetidos.recorrer_adelante(), [7, 4])
    verificar("datos repetidos: enlaces correctos", enlaces_bien(repetidos), True)


def demo_reproduccion():
    print("\n--- Demostración: lista de reproducción ---")
    canciones = ListaDoblementeEnlazada()
    for nombre in ("Cancion A", "Cancion B", "Cancion C", "Cancion D"):
        canciones.insertar_final(nombre)
    print("Lista de canciones:")
    print(" ", canciones)
    print("Reproducir hacia adelante:", canciones.recorrer_adelante())
    print("Reproducir hacia atrás:   ", canciones.recorrer_atras())
    canciones.insertar_en_posicion(2, "Cancion Nueva")
    print("Se agrega una canción en la posición 2:")
    print(" ", canciones)
    canciones.eliminar("Cancion B")
    print("Se quita la Cancion B:")
    print(" ", canciones)
    print("Hacia atrás ahora:", canciones.recorrer_atras())


if __name__ == "__main__":
    pruebas_basicas()
    pruebas_casos_borde()
    demo_reproduccion()

    print("\n" + "=" * 52)
    print("Pruebas correctas:", aciertos)
    print("Pruebas con fallo:", fallos)
    print("=" * 52)
    input("\nPresiona ENTER para salir...")
