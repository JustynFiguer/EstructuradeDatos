from collections import deque


class NodoArbol:
    def __init__(self, dato):
        self.dato = dato
        self.hijo_izq = None
        self.hijo_der = None


class ArbolBinario:
    def __init__(self):
        self.raiz = None

    def insertar(self, dato):
        nuevo = NodoArbol(dato)
        if self.raiz is None:
            self.raiz = nuevo
            return
        actual = self.raiz
        while True:
            if dato < actual.dato:
                if actual.hijo_izq is None:
                    actual.hijo_izq = nuevo
                    return
                actual = actual.hijo_izq
            else:
                if actual.hijo_der is None:
                    actual.hijo_der = nuevo
                    return
                actual = actual.hijo_der

    def preorden(self):
        resultado = []
        self._preorden(self.raiz, resultado)
        return resultado

    def _preorden(self, nodo, resultado):
        if nodo is None:
            return
        resultado.append(nodo.dato)
        self._preorden(nodo.hijo_izq, resultado)
        self._preorden(nodo.hijo_der, resultado)

    def inorden(self):
        resultado = []
        self._inorden(self.raiz, resultado)
        return resultado

    def _inorden(self, nodo, resultado):
        if nodo is None:
            return
        self._inorden(nodo.hijo_izq, resultado)
        resultado.append(nodo.dato)
        self._inorden(nodo.hijo_der, resultado)

    def postorden(self):
        resultado = []
        self._postorden(self.raiz, resultado)
        return resultado

    def _postorden(self, nodo, resultado):
        if nodo is None:
            return
        self._postorden(nodo.hijo_izq, resultado)
        self._postorden(nodo.hijo_der, resultado)
        resultado.append(nodo.dato)

    def por_niveles(self):
        resultado = []
        if self.raiz is None:
            return resultado
        cola = deque([self.raiz])
        while cola:
            nodo = cola.popleft()
            resultado.append(nodo.dato)
            if nodo.hijo_izq is not None:
                cola.append(nodo.hijo_izq)
            if nodo.hijo_der is not None:
                cola.append(nodo.hijo_der)
        return resultado

    def altura(self):
        return self._altura(self.raiz)

    def _altura(self, nodo):
        if nodo is None:
            return -1
        return 1 + max(self._altura(nodo.hijo_izq), self._altura(nodo.hijo_der))

    def tamano(self):
        return self._tamano(self.raiz)

    def _tamano(self, nodo):
        if nodo is None:
            return 0
        return 1 + self._tamano(nodo.hijo_izq) + self._tamano(nodo.hijo_der)


def mostrar_presentacion():
    print("=" * 60)
    print("UNIVERSIDAD DE PANAMÁ")
    print("Facultad de Informática, Electrónica y Comunicaciones (FIEC)")
    print("Asignatura: Estructura de Datos")
    print("Profesor: Ángel Ávila")
    print("Desarrollado por: Justiniano Figueroa")
    print("-" * 60)
    print("Laboratorio 10 - Árbol binario con tres recorridos")
    print("=" * 60)
    print()
    print("Instrucciones:")
    print("  1. El programa construye un árbol binario de ejemplo.")
    print("  2. Muestra el árbol y sus datos básicos.")
    print("  3. Imprime los recorridos preorden, inorden y postorden.")
    print("  4. Compara las salidas sobre el mismo árbol.")
    print("  5. Al final puedes insertar tus propios números.")
    print()


def mostrar_arbol():
    print("Árbol de ejemplo:")
    print()
    print("        10")
    print("       /  \\")
    print("      5    20")
    print("     / \\     \\")
    print("    3   7    30")
    print()


def mostrar_recorridos(arbol):
    print("Recorridos del árbol:")
    print("  Preorden   (raíz-izq-der):", arbol.preorden())
    print("  Inorden    (izq-raíz-der):", arbol.inorden())
    print("  Postorden  (izq-der-raíz):", arbol.postorden())
    print("  Por niveles (con cola)   :", arbol.por_niveles())
    print()


def main():
    mostrar_presentacion()

    arbol = ArbolBinario()
    for valor in [10, 5, 20, 3, 7, 30]:
        arbol.insertar(valor)

    mostrar_arbol()
    print("Cantidad de nodos:", arbol.tamano())
    print("Altura del árbol :", arbol.altura())
    print()

    mostrar_recorridos(arbol)

    print("El inorden sale ordenado porque el árbol es de búsqueda.")
    print()

    print("Ahora prueba con tus propios números.")
    texto = input("Escribe números separados por espacios (Enter para salir): ").strip()
    if texto == "":
        print("Fin del programa.")
        return

    propio = ArbolBinario()
    try:
        for parte in texto.split():
            propio.insertar(int(parte))
    except ValueError:
        print("Solo se permiten números enteros.")
        return

    print()
    print("Cantidad de nodos:", propio.tamano())
    print("Altura del árbol :", propio.altura())
    print()
    mostrar_recorridos(propio)


if __name__ == "__main__":
    main()
