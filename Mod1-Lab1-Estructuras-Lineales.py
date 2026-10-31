# Universidad de Panamá
# Facultad de Informática, Electrónica y Comunicación (FIEC)
# Asignatura: Estructura de Datos - INF222
# Laboratorio 1: Implementación de una pila
# Desarrollado por: Justiniano Figueroa
# Profesor: Ángel Ávila


class Pila:
    
    def __init__(self):
        self.datos = []

    def push(self, dato):
        self.datos.append(dato)

    def pop(self):
        if self.is_empty():
            raise IndexError("La pila está vacía")
        return self.datos.pop()

    def peek(self):
        if self.is_empty():
            raise IndexError("La pila está vacía")
        return self.datos[-1]

    def is_empty(self):
        return len(self.datos) == 0

    def size(self):
        return len(self.datos)

    def mostrar(self):
        return self.datos


def probar_pila_vacia():
    pila = Pila()
    assert pila.is_empty()
    assert pila.size() == 0


def probar_agregar_y_ver():
    pila = Pila()
    pila.push(10)
    pila.push(20)
    assert pila.peek() == 20
    assert pila.size() == 2
    assert not pila.is_empty()


def probar_orden_de_salida():
    pila = Pila()
    pila.push(1)
    pila.push(2)
    pila.push(3)
    assert pila.pop() == 3
    assert pila.pop() == 2
    assert pila.pop() == 1
    assert pila.is_empty()


def probar_operaciones_con_pila_vacia():
    pila = Pila()

    try:
        pila.pop()
    except IndexError:
        pass
    else:
        raise AssertionError("pop debía indicar que la pila está vacía")

    try:
        pila.peek()
    except IndexError:
        pass
    else:
        raise AssertionError("peek debía indicar que la pila está vacía")


def probar_diferentes_datos():
    pila = Pila()
    pila.push("Hola")
    pila.push(25)
    pila.push(3.5)
    assert pila.pop() == 3.5
    assert pila.pop() == 25
    assert pila.pop() == "Hola esta es una prueba"


def probar_invertir_palabra():
    pila = Pila()
    for letra in "hola":
        pila.push(letra)

    palabra = ""
    while not pila.is_empty():
        palabra += pila.pop()

    assert palabra == "aloh"


def probar_parentesis():
    def esta_balanceado(texto):
        pila = Pila()
        for caracter in texto:
            if caracter == "(":
                pila.push(caracter)
            elif caracter == ")":
                if pila.is_empty():
                    return False
                pila.pop()
        return pila.is_empty()

    assert esta_balanceado("(a + b)")
    assert esta_balanceado("((()))")
    assert not esta_balanceado("(()")
    assert not esta_balanceado("())(")


if __name__ == "__main__":
    pruebas = [
        probar_pila_vacia,
        probar_agregar_y_ver,
        probar_orden_de_salida,
        probar_operaciones_con_pila_vacia,
        probar_diferentes_datos,
        probar_invertir_palabra,
        probar_parentesis
    ]

    print("*****************************************")
    print("       LABORATORIO 1 - PILA")
    print("*****************************************")
    print("Desarrollado por: Justiniano Figueroa M")
    print("Estructura de Datos")
    print("Profesor: Ángel Ávila")
    print("*****************************************")

    correctas = 0
    for prueba in pruebas:
        prueba()
        correctas += 1
        print("Prueba realizada:", prueba.__name__)

    print("*****************************************")
    print("Pruebas completadas:", correctas)
    print("La pila funciona correctamente.")
    print("*****************************************")
    input("\nPresiona ENTER para salir...")