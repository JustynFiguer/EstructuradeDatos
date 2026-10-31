class Navegador:
    def __init__(self):
        self.actual = "about:blank"
        self.pila_atras = []
        self.pila_adelante = []

    def visitar(self, url):
        self.pila_atras.append(self.actual)
        self.actual = url
        self.pila_adelante = []

    def atras(self):
        if not self.pila_atras:
            return False
        self.pila_adelante.append(self.actual)
        self.actual = self.pila_atras.pop()
        return True

    def adelante(self):
        if not self.pila_adelante:
            return False
        self.pila_atras.append(self.actual)
        self.actual = self.pila_adelante.pop()
        return True

    def estado(self):
        print("Página actual :", self.actual)
        print("Pila atrás    :", self.pila_atras)
        print("Pila adelante :", self.pila_adelante)


def mostrar_presentacion():
    print("=" * 60)
    print("UNIVERSIDAD DE PANAMÁ")
    print("Facultad de Informática, Electrónica y Comunicaciones (FIEC)")
    print("Asignatura: Estructura de Datos")
    print("Profesor: Ángel Ávila")
    print("Desarrollado por: Justiniano Figueroa")
    print("-" * 60)
    print("Laboratorio 3 - Taller integrador")
    print("Simulador de historial de navegador")
    print("=" * 60)
    print()
    print("Instrucciones:")
    print("  1. Visita páginas escribiendo una dirección (ejemplo: a.com).")
    print("  2. Usa Atrás y Adelante para moverte por el historial.")
    print("  3. Al visitar una página nueva, la pila de adelante se vacía.")
    print("  4. Con la opción 4 ves el estado de las dos pilas.")
    print()


def menu():
    print()
    print("1. Visitar una página")
    print("2. Atrás")
    print("3. Adelante")
    print("4. Ver estado")
    print("5. Salir")


def main():
    mostrar_presentacion()
    nav = Navegador()
    nav.estado()

    while True:
        menu()
        opcion = input("Elige una opción: ").strip()
        print()
        if opcion == "1":
            url = input("Dirección: ").strip()
            if url == "":
                print("No escribiste ninguna dirección.")
                continue
            nav.visitar(url)
            nav.estado()
        elif opcion == "2":
            if nav.atras():
                nav.estado()
            else:
                print("No hay páginas anteriores.")
        elif opcion == "3":
            if nav.adelante():
                nav.estado()
            else:
                print("No hay páginas adelante.")
        elif opcion == "4":
            nav.estado()
        elif opcion == "5":
            print("Fin del programa.")
            break
        else:
            print("Opción no válida.")


if __name__ == "__main__":
    main()
