import copy

print("LABORATORIO 4 - REFERENCIAS Y ALIASING")
print("Justiniano Figueroa - INF222")

print("\n--- Ejercicio 1: id() con enteros ---")
a = 42
b = a
print("a is b:", a is b)
b = b + 1
print("a =", a, "| b =", b)
print("a is b:", a is b)

print("\n--- Ejercicio 2: aliasing con listas ---")
lista_a = [1, 2, 3]
lista_b = lista_a
print("lista_a is lista_b:", lista_a is lista_b)
print("id iguales:", id(lista_a) == id(lista_b))
lista_b.append(4)
print("lista_a =", lista_a)
print("lista_b =", lista_b)

print("\n--- Ejercicio 3: copias de una lista ---")
original = [1, 2, 3]
copia1 = original.copy()
copia2 = list(original)
copia3 = copy.deepcopy(original)
copia1.append(99)
print("original =", original)
print("copia1 =", copia1)
print("copia2 =", copia2)
print("copia3 =", copia3)
print("copia1 is original:", copia1 is original)

print("\n--- Ejercicio 4: copia superficial y copia profunda ---")
matriz = [[1, 2], [3, 4]]
superficial = matriz.copy()
profunda = copy.deepcopy(matriz)
matriz[0][0] = 99
print("matriz =", matriz)
print("superficial =", superficial)
print("profunda =", profunda)
print("superficial[0] is matriz[0]:", superficial[0] is matriz[0])
print("profunda[0] is matriz[0]:", profunda[0] is matriz[0])

print("\n--- Ejercicio 5: tipos inmutables ---")
texto = "hola"
otro = texto
otro += " mundo"
print("texto =", texto)
print("otro =", otro)
tupla = (1, 2)
otra = tupla
otra = otra + (3,)
print("tupla =", tupla)
print("otra =", otra)

print("\n--- Ejercicio 6: referencias dentro de funciones ---")


def agregar_a_lista(lista, valor):
    lista.append(valor)


def reasignar_lista(lista):
    lista = [0]
    return lista


datos = [1]
agregar_a_lista(datos, 2)
print("datos despues de agregar_a_lista:", datos)
datos2 = [5]
reasignar_lista(datos2)
print("datos2 despues de reasignar_lista:", datos2)

print("\n--- Ejercicio 7: lista como parametro por defecto ---")


def acumular(valor, lista=[]):
    lista.append(valor)
    return lista


print(acumular(1))
print(acumular(2))
print(acumular(3))

print("\n--- Ejercicio 8: mutar in situ o devolver una copia ---")


def agregar(lista, valor, in_situ=False):
    if in_situ:
        destino = lista
    else:
        destino = lista.copy()
    destino.append(valor)
    return destino


numeros = [1, 2, 3]
resultado1 = agregar(numeros, 4, in_situ=True)
print("in_situ=True  -> resultado is numeros:", resultado1 is numeros)
print("numeros =", numeros)
resultado2 = agregar(numeros, 5, in_situ=False)
print("in_situ=False -> resultado is numeros:", resultado2 is numeros)
print("numeros =", numeros)
print("resultado2 =", resultado2)

input("\nPresiona ENTER para salir...")
