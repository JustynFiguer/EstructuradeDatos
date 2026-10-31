class NodoArbol:
    def __init__(self, dato):
        self.dato = dato
        self.hijo_izq = None
        self.hijo_der = None


class ArbolBinarioBusqueda:
    def __init__(self):
        self.raiz = None

    def insertar(self, dato):
        nuevo = NodoArbol(dato)
        if self.raiz is None:
            self.raiz = nuevo
            return
        actual = self.raiz
        while True:
            if dato == actual.dato:
                return
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

    def buscar(self, dato):
        actual = self.raiz
        while actual is not None:
            if dato == actual.dato:
                return True
            if dato < actual.dato:
                actual = actual.hijo_izq
            else:
                actual = actual.hijo_der
        return False

    def eliminar(self, dato):
        self.raiz = self._eliminar(self.raiz, dato)

    def _eliminar(self, nodo, dato):
        if nodo is None:
            return None
        if dato < nodo.dato:
            nodo.hijo_izq = self._eliminar(nodo.hijo_izq, dato)
        elif dato > nodo.dato:
            nodo.hijo_der = self._eliminar(nodo.hijo_der, dato)
        else:
            if nodo.hijo_izq is None:
                return nodo.hijo_der
            if nodo.hijo_der is None:
                return nodo.hijo_izq
            sucesor = nodo.hijo_der
            while sucesor.hijo_izq is not None:
                sucesor = sucesor.hijo_izq
            nodo.dato = sucesor.dato
            nodo.hijo_der = self._eliminar(nodo.hijo_der, sucesor.dato)
        return nodo

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

    def altura(self):
        return self._altura(self.raiz)

    def _altura(self, nodo):
        if nodo is None:
            return -1
        return 1 + max(self._altura(nodo.hijo_izq), self._altura(nodo.hijo_der))

    def tamano(self):
        return len(self.inorden())

    def dibujar(self):
        lineas = []
        self._dibujar(self.raiz, 0, lineas)
        return lineas

    def _dibujar(self, nodo, nivel, lineas):
        if nodo is None:
            return
        self._dibujar(nodo.hijo_der, nivel + 1, lineas)
        lineas.append("    " * nivel + str(nodo.dato))
        self._dibujar(nodo.hijo_izq, nivel + 1, lineas)


def mostrar_presentacion():
    print("=" * 60)
    print("UNIVERSIDAD DE PANAMÁ")
    print("Facultad de Informática, Electrónica y Comunicaciones (FIEC)")
    print("Asignatura: Estructura de Datos")
    print("Profesor: Ángel Ávila")
    print("Desarrollado por: Justiniano Figueroa")
    print("-" * 60)
    print("Laboratorio 11 - Árbol Binario de Búsqueda (BST)")
    print("=" * 60)
    print()
    print("Instrucciones:")
    print("  1. Se arma un BST con insertar, buscar y eliminar.")
    print("  2. Se prueban los tres casos de eliminación.")
    print("  3. Se compara un árbol balanceado con uno degenerado.")
    print("  4. Se mide la altura en los dos casos.")
    print("  5. Al final hay un menú para probar con tus datos.")
    print()


def construir(valores):
    arbol = ArbolBinarioBusqueda()
    for v in valores:
        arbol.insertar(v)
    return arbol


def mostrar_estado(arbol):
    print("Inorden :", arbol.inorden())
    print("Nodos   :", arbol.tamano())
    print("Altura  :", arbol.altura())
    print()


def prueba_basica():
    print("--- 1. Insertar y buscar ---")
    arbol = construir([10, 5, 20, 3, 7, 12, 30, 15])
    print("Valores insertados: 10, 5, 20, 3, 7, 12, 30, 15")
    print("(el árbol se dibuja de lado, la raíz está a la izquierda)")
    print()
    for linea in arbol.dibujar():
        print(linea)
    print()
    mostrar_estado(arbol)
    for buscado in [7, 15, 99]:
        if arbol.buscar(buscado):
            print(f"Buscar {buscado}: encontrado")
        else:
            print(f"Buscar {buscado}: no está en el árbol")
    print()


def prueba_eliminar():
    print("--- 2. Eliminar (los tres casos) ---")

    arbol = construir([10, 5, 20, 3, 7, 12, 30, 15])
    print("Caso 1: eliminar una hoja (3)")
    arbol.eliminar(3)
    mostrar_estado(arbol)

    arbol = construir([10, 5, 20, 3, 7, 12, 30, 15])
    print("Caso 2: eliminar un nodo con un solo hijo (12, tiene el 15)")
    arbol.eliminar(12)
    mostrar_estado(arbol)

    arbol = construir([10, 20, 5, 12, 30, 15])
    print("Caso 3: eliminar un nodo con dos hijos (10)")
    print("Antes:")
    for linea in arbol.dibujar():
        print(linea)
    arbol.eliminar(10)
    print("Después (el 12 es el sucesor inorden y toma su lugar):")
    for linea in arbol.dibujar():
        print(linea)
    print()
    mostrar_estado(arbol)


def prueba_balance():
    print("--- 3. Balanceado contra degenerado ---")
    balanceado = construir([40, 20, 60, 10, 30, 50, 70])
    degenerado = construir([10, 20, 30, 40, 50, 60, 70])

    print("Balanceado (insertando 40, 20, 60, 10, 30, 50, 70):")
    for linea in balanceado.dibujar():
        print(linea)
    print("Altura:", balanceado.altura())
    print()

    print("Degenerado (insertando 10, 20, 30, 40, 50, 60, 70 en orden):")
    for linea in degenerado.dibujar():
        print(linea)
    print("Altura:", degenerado.altura())
    print()

    print("Con los mismos 7 datos, uno queda de altura",
          balanceado.altura(), "y el otro de altura", degenerado.altura())
    print("El degenerado parece una lista enlazada, por eso buscar,")
    print("insertar y eliminar pasan de O(log n) a O(n).")
    print()

    print("Con 300 datos:")
    bueno = construir(orden_balanceado(1, 300))
    malo = construir(range(1, 301))
    print("  Altura insertando de forma balanceada:", bueno.altura())
    print("  Altura insertando en orden creciente :", malo.altura())
    print()


def orden_balanceado(inicio, fin):
    if inicio > fin:
        return []
    medio = (inicio + fin) // 2
    return [medio] + orden_balanceado(inicio, medio - 1) + orden_balanceado(medio + 1, fin)


def menu():
    arbol = ArbolBinarioBusqueda()
    while True:
        print("--- Menú ---")
        print("1. Insertar")
        print("2. Buscar")
        print("3. Eliminar")
        print("4. Ver árbol")
        print("5. Salir")
        opcion = input("Elige una opción: ").strip()
        if opcion == "5":
            print("Fin del programa.")
            break
        if opcion not in ("1", "2", "3", "4"):
            print("Opción no válida.")
            print()
            continue
        if opcion == "4":
            if arbol.raiz is None:
                print("El árbol está vacío.")
            else:
                for linea in arbol.dibujar():
                    print(linea)
                mostrar_estado(arbol)
            continue
        try:
            numero = int(input("Escribe un número entero: "))
        except ValueError:
            print("Eso no es un número entero.")
            print()
            continue
        if opcion == "1":
            arbol.insertar(numero)
            print("Insertado.")
        elif opcion == "2":
            if arbol.buscar(numero):
                print("Sí está en el árbol.")
            else:
                print("No está en el árbol.")
        else:
            if arbol.buscar(numero):
                arbol.eliminar(numero)
                print("Eliminado.")
            else:
                print("Ese número no está en el árbol.")
        print()


def main():
    mostrar_presentacion()
    prueba_basica()
    prueba_eliminar()
    prueba_balance()
    respuesta = input("¿Quieres probar el menú? (s/n): ").strip().lower()
    print()
    if respuesta == "s":
        menu()
    else:
        print("Fin del programa.")


if __name__ == "__main__":
    main()
