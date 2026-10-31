from collections import deque


class Grafo:
    def __init__(self):
        self.lista = {}

    def agregar_vertice(self, v):
        if v not in self.lista:
            self.lista[v] = []

    def agregar_arista(self, a, b):
        self.agregar_vertice(a)
        self.agregar_vertice(b)
        if b not in self.lista[a]:
            self.lista[a].append(b)
        if a not in self.lista[b]:
            self.lista[b].append(a)

    def bfs(self, inicio):
        if inicio not in self.lista:
            return []
        visitados = [inicio]
        cola = deque([inicio])
        while cola:
            actual = cola.popleft()
            for vecino in self.lista[actual]:
                if vecino not in visitados:
                    visitados.append(vecino)
                    cola.append(vecino)
        return visitados

    def dfs(self, inicio):
        if inicio not in self.lista:
            return []
        visitados = []
        pila = [inicio]
        while pila:
            actual = pila.pop()
            if actual in visitados:
                continue
            visitados.append(actual)
            for vecino in self.lista[actual]:
                if vecino not in visitados:
                    pila.append(vecino)
        return visitados

    def matriz(self):
        vertices = list(self.lista)
        filas = []
        for a in vertices:
            filas.append([1 if b in self.lista[a] else 0 for b in vertices])
        return vertices, filas

    def mostrar_lista(self):
        for v in self.lista:
            print(f"  {v}: {self.lista[v]}")

    def mostrar_matriz(self):
        vertices, filas = self.matriz()
        ancho = max(len(str(v)) for v in vertices) + 2
        print(" " * ancho + "".join(str(v).ljust(ancho) for v in vertices))
        for v, fila in zip(vertices, filas):
            print(str(v).ljust(ancho) + "".join(str(x).ljust(ancho) for x in fila))


def mostrar_presentacion():
    print("=" * 60)
    print("UNIVERSIDAD DE PANAMÁ")
    print("Facultad de Informática, Electrónica y Comunicaciones (FIEC)")
    print("Asignatura: Estructura de Datos")
    print("Profesor: Ángel Ávila")
    print("Desarrollado por: Justiniano Figueroa")
    print("-" * 60)
    print("Laboratorio 12 - Grafo + BFS + DFS")
    print("=" * 60)
    print()
    print("Instrucciones:")
    print("  1. Se arma un grafo con lista de adyacencia.")
    print("  2. Se recorre con BFS (usa una cola) y con DFS (usa una pila).")
    print("  3. Se prueba con un grafo pequeño y con una red de ciudades")
    print("     de Panamá.")
    print("  4. Al final puedes armar tu propio grafo en un menú.")
    print()


def ejemplo_basico():
    print("--- 1. Grafo de ejemplo ---")
    g = Grafo()
    g.agregar_arista("A", "B")
    g.agregar_arista("A", "C")
    g.agregar_arista("B", "D")
    g.agregar_arista("B", "E")
    print("  A - B - D")
    print("  |   |")
    print("  C   E")
    print()
    print("Lista de adyacencia:")
    g.mostrar_lista()
    print()
    print("Matriz de adyacencia:")
    g.mostrar_matriz()
    print()
    print("BFS desde A:", ", ".join(g.bfs("A")))
    print("DFS desde A:", ", ".join(g.dfs("A")))
    print()


def ejemplo_panama():
    print("--- 2. Red de ciudades de Panamá ---")
    g = Grafo()
    g.agregar_arista("Panamá", "Colón")
    g.agregar_arista("Panamá", "Penonomé")
    g.agregar_arista("Penonomé", "Santiago")
    g.agregar_arista("Santiago", "Chitré")
    g.agregar_arista("Santiago", "David")
    g.agregar_arista("David", "Boquete")
    g.agregar_arista("David", "Changuinola")
    print("Lista de adyacencia:")
    g.mostrar_lista()
    print()
    print("BFS desde Panamá:", ", ".join(g.bfs("Panamá")))
    print("DFS desde Panamá:", ", ".join(g.dfs("Panamá")))
    print()
    print("BFS va por niveles: primero las ciudades más cercanas a Panamá.")
    print("DFS se va lo más lejos que puede por un camino antes de volver.")
    print()


def menu():
    g = Grafo()
    while True:
        print()
        print("1. Agregar arista")
        print("2. Ver lista de adyacencia")
        print("3. Ver matriz de adyacencia")
        print("4. BFS")
        print("5. DFS")
        print("6. Salir")
        opcion = input("Elige una opción: ").strip()
        print()
        if opcion == "1":
            a = input("Vértice 1: ").strip()
            b = input("Vértice 2: ").strip()
            if a == "" or b == "":
                print("Los vértices no pueden estar vacíos.")
                continue
            g.agregar_arista(a, b)
            print(f"Arista {a} - {b} agregada.")
        elif opcion == "2":
            if not g.lista:
                print("El grafo está vacío.")
            else:
                g.mostrar_lista()
        elif opcion == "3":
            if not g.lista:
                print("El grafo está vacío.")
            else:
                g.mostrar_matriz()
        elif opcion == "4":
            inicio = input("Vértice de inicio: ").strip()
            if inicio not in g.lista:
                print("Ese vértice no existe.")
            else:
                print("BFS:", ", ".join(g.bfs(inicio)))
        elif opcion == "5":
            inicio = input("Vértice de inicio: ").strip()
            if inicio not in g.lista:
                print("Ese vértice no existe.")
            else:
                print("DFS:", ", ".join(g.dfs(inicio)))
        elif opcion == "6":
            print("Fin del programa.")
            break
        else:
            print("Opción no válida.")


def main():
    mostrar_presentacion()
    ejemplo_basico()
    ejemplo_panama()
    respuesta = input("¿Quieres armar tu propio grafo? (s/n): ").strip().lower()
    if respuesta == "s":
        menu()
    else:
        print("Fin del programa.")


if __name__ == "__main__":
    main()
