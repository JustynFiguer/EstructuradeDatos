from collections import deque


class Grafo:
    def __init__(self):
        self.lista = {}

    def agregar_arista(self, a, b):
        if a not in self.lista:
            self.lista[a] = []
        if b not in self.lista:
            self.lista[b] = []
        self.lista[a].append(b)
        self.lista[b].append(a)

    def bfs(self, inicio):
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
        visitados = []
        pila = [inicio]
        while pila:
            actual = pila.pop()
            if actual not in visitados:
                visitados.append(actual)
                for vecino in self.lista[actual]:
                    if vecino not in visitados:
                        pila.append(vecino)
        return visitados


def presentacion():
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
    print("  1. El programa arma un grafo de ejemplo.")
    print("  2. Muestra su lista de adyacencia.")
    print("  3. Recorre el grafo con BFS y con DFS.")
    print("  4. Puedes probar otro vértice de inicio.")
    print()


def main():
    presentacion()

    g = Grafo()
    g.agregar_arista("A", "B")
    g.agregar_arista("A", "C")
    g.agregar_arista("B", "D")
    g.agregar_arista("B", "E")

    print("Grafo:")
    print("  A - B - D")
    print("  |   |")
    print("  C   E")
    print()
    print("Lista de adyacencia:")
    for vertice in g.lista:
        print(f"  {vertice}: {g.lista[vertice]}")
    print()
    print("BFS desde A:", ", ".join(g.bfs("A")))
    print("DFS desde A:", ", ".join(g.dfs("A")))
    print()

    while True:
        inicio = input("Otro vértice de inicio (A-E, Enter para salir): ").strip().upper()
        if inicio == "":
            print("Fin del programa.")
            break
        if inicio not in g.lista:
            print("Ese vértice no existe.")
            continue
        print("BFS desde", inicio + ":", ", ".join(g.bfs(inicio)))
        print("DFS desde", inicio + ":", ", ".join(g.dfs(inicio)))
        print()


if __name__ == "__main__":
    main()
