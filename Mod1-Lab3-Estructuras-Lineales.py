print("." * 52)
print("UNIVERSIDAD DE PANAMÁ")
print("FACULTAD DE INFORMÁTICA, ELECTRÓNICA Y COMUNICACIÓN")
print("TÉCNICO DE COMUNICACIONES - FIEC")
print("ESTRUCTURA DE DATOS - INF222")
print("LABORATORIO N.º 3: HISTORIAL DE NAVEGADOR")
print("Desarrollado por: Justiniano Figueroa")
print("Profesor: Ángel Ávila")
print("Segundo semestre")
print("=" * 52)


class HistorialNavegador:
    def __init__(self):
        self.atras = []
        self.adelante = []
        self.actual = "about:blank"

    def visitar(self, pagina):
        self.atras.append(self.actual)
        self.actual = pagina
        self.adelante.clear()
        print("Página abierta:", self.actual)

    def volver(self):
        if self.atras:
            self.adelante.append(self.actual)
            self.actual = self.atras.pop()
            print("Página actual:", self.actual)
        else:
            print("No hay páginas anteriores.")

    def avanzar(self):
        if self.adelante:
            self.atras.append(self.actual)
            self.actual = self.adelante.pop()
            print("Página actual:", self.actual)
        else:
            print("No hay páginas siguientes.")

    def mostrar(self):
        print("\nHistorial anterior:", self.atras)
        print("Página actual:", self.actual)
        print("Historial siguiente:", self.adelante)


def menu():
    navegador = HistorialNavegador()

    while True:
        print("\n----------- MENÚ PRINCIPAL -----------")
        print("1. Visitar una página")
        print("2. Atrás")
        print("3. Adelante")
        print("4. Mostrar historial")
        print("5. Salir")

        opcion = input("Seleccione una opción: ").strip()

        if opcion == "1":
            pagina = input("Escriba la dirección de la página: ").strip()
            if pagina:
                navegador.visitar(pagina)
            else:
                print("Debe escribir una dirección.")
        elif opcion == "2":
            navegador.volver()
        elif opcion == "3":
            navegador.avanzar()
        elif opcion == "4":
            navegador.mostrar()
        elif opcion == "5":
            print("Programa finalizado.")
            break
        else:
            print("Opción no válida. Intente nuevamente.")


if __name__ == "__main__":
    menu()
