print("UNIVERSIDAD DE PANAMÁ")
print("FACULTAD DE INFORMÁTICA, ELECTRÓNICA Y COMUNICACIÓN (FIEC)")
print("TÉCNICO DE COMUNICACIONES")
print("Desarrollado por: Justiniano Figueroa")
print("Profesor: Ángel Ávila")
print("Segundo semestre")
print("LABORATORIO N.º 2: PILAS ENLAZADAS Y COLAS")
print("-" * 45)

class Nodo:
    def __init__(self, dato):
        self.dato = dato
        self.siguiente = None

class Pila:
    def __init__(self):
        self.tope = None

    def agregar(self, dato):
        nuevo = Nodo(dato)
        nuevo.siguiente = self.tope
        self.tope = nuevo

    def quitar(self):
        if self.tope is None:
            return "La pila está vacía"
        dato = self.tope.dato
        self.tope = self.tope.siguiente
        return dato

    def mostrar(self):
        actual = self.tope
        while actual:
            print(actual.dato)
            actual = actual.siguiente

class Cola:
    def __init__(self):
        self.frente = None
        self.final = None

    def agregar(self, dato):
        nuevo = Nodo(dato)
        if self.frente is None:
            self.frente = nuevo
        else:
            self.final.siguiente = nuevo
        self.final = nuevo

    def quitar(self):
        if self.frente is None:
            return "La cola está vacía"
        dato = self.frente.dato
        self.frente = self.frente.siguiente
        if self.frente is None:
            self.final = None
        return dato

    def mostrar(self):
        actual = self.frente
        while actual:
            print(actual.dato)
            actual = actual.siguiente

def parentesis_balanceados(texto):
    pila = Pila()
    pares = {")": "(", "]": "[", "}": "{"}
    for caracter in texto:
        if caracter in "([{":
            pila.agregar(caracter)
        elif caracter in pares:
            if pila.quitar() != pares[caracter]:
                return False
    return pila.tope is None

def evaluar_postfija(expresion):
    pila = []
    for elemento in expresion.split():
        if elemento in "+-*/":
            b = pila.pop()
            a = pila.pop()
            resultado = {"+": a + b, "-": a - b, "*": a * b, "/": a / b}[elemento]
            pila.append(resultado)
        else:
            pila.append(float(elemento))
    return pila.pop()

print("\n1. PILA ENLAZADA")
pila = Pila()
pila.agregar(10)
pila.agregar(20)
pila.agregar(30)
print("Elementos de la pila:")
pila.mostrar()
print("Elemento eliminado:", pila.quitar())

print("\n2. PARÉNTESIS BALANCEADOS")
print("{[()]}", parentesis_balanceados("{[()]}"))
print("{[(])}", parentesis_balanceados("{[(])}"))

print("\n3. COLA ENLAZADA")
cola = Cola()
cola.agregar("Ana")
cola.agregar("Luis")
cola.agregar("Marta")
print("Personas en la cola:")
cola.mostrar()
print("Atendido:", cola.quitar())

print("\n4. COLA DE IMPRESIÓN")
impresora = Cola()
impresora.agregar("Documento de Justiniano")
impresora.agregar("Tarea de Ana")
impresora.agregar("Informe de Luis")
while impresora.frente:
    print("Imprimiendo:", impresora.quitar())

print("\n5. EXPRESIÓN POSTFIJA")
print("3 4 + 5 * =", evaluar_postfija("3 4 + 5 *"))

print("\nLaboratorio finalizado.")
input("Presiona ENTER para salir...")
