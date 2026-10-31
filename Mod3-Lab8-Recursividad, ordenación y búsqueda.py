# ==========================================
# UNIVERSIDAD DE PANAMÁ
# FACULTAD DE INFORMÁTICA, ELECTRÓNICA Y COMUNICACIÓN
# ESCUELA DE INFORMÁTICA
# ASIGNATURA: Estructura de Datos (INF222)
# PROFESOR: Ángel Ávila
# DESARROLLADOR: Justino Figueroa
# MÓDULO 3: Recursividad, Ordenación y Búsqueda (Semana 8)
# ==========================================

import os

def limpiar_pantalla():
    os.system('cls' if os.name == 'nt' else 'clear')

def mostrar_encabezado():
    print("=" * 65)
    print("                UNIVERSIDAD DE PANAMÁ")
    print("     FACULTAD DE INFORMÁTICA, ELECTRÓNICA Y COMUNICACIÓN")
    print("                  LICENCIATURA EN INFORMÁTICA")
    print("=" * 65)
    print(" Asignatura : Estructura de Datos")
    print(" Profesor   : Ángel Ávila")
    print(" Estudiante : Justino Figueroa")
    print(" Módulo     : Recursividad, Ordenación y Búsqueda (Semana 8)")
    print("=" * 65)

# 1. Funciones Recursivas
def factorial(n):
    if n == 0 or n == 1:
        return 1
    return n * factorial(n - 1)

def fibonacci(n):
    if n <= 0:
        return 0
    elif n == 1:
        return 1
    return fibonacci(n - 1) + fibonacci(n - 2)

def menu_recursividad():
    while True:
        limpiar_pantalla()
        mostrar_encabezado()
        print("\n--- MÓDULO 1: RECURSIVIDAD ---")
        print("1. Calcular Factorial")
        print("2. Calcular Fibonacci")
        print("3. Volver al Menú Principal")
        opcion = input("\nSeleccione una opción (1-3): ")
        
        if opcion == '1':
            try:
                num = int(input("\nIngrese un número entero no negativo: "))
                if num < 0:
                    print("El número no puede ser negativo.")
                else:
                    res = factorial(num)
                    print(f"El factorial de {num} es: {res}")
            except ValueError:
                print("Por favor, ingrese un número válido.")
            input("\nPresione Enter para continuar...")
        elif opcion == '2':
            try:
                num = int(input("\nIngrese la posición de Fibonacci (n >= 0): "))
                if num < 0:
                    print("La posición no puede ser negativa.")
                else:
                    res = fibonacci(num)
                    print(f"El término {num} de Fibonacci es: {res}")
            except ValueError:
                print("Por favor, ingrese un número válido.")
            input("\nPresione Enter para continuar...")
        elif opcion == '3':
            break
        else:
            print("Opción inválida.")
            input("\nPresione Enter para continuar...")

# 2. Métodos de Ordenación
def ordenar_burbuja(lista):
    n = len(lista)
    for i in range(n):
        for j in range(0, n - i - 1):
            if lista[j] > lista[j + 1]:
                lista[j], lista[j + 1] = lista[j + 1], lista[j]
    return lista

def menu_ordenacion():
    while True:
        limpiar_pantalla()
        mostrar_encabezado()
        print("\n--- MÓDULO 2: ORDENACIÓN (Burbuja) ---")
        print("1. Ordenar una lista de números")
        print("2. Volver al Menú Principal")
        opcion = input("\nSeleccione una opción (1-2): ")
        
        if opcion == '1':
            entrada = input("\nIngrese números separados por espacios (ej: 45 12 8 90 3): ")
            try:
                lista = [int(x) for x in entrada.split()]
                if not lista:
                    print("La lista está vacía.")
                else:
                    print(f"Lista original: {lista}")
                    ordenada = ordenar_burbuja(lista.copy())
                    print(f"Lista ordenada (Burbuja): {ordenada}")
            except ValueError:
                print("Error: Asegúrese de ingresar solo números enteros.")
            input("\nPresione Enter para continuar...")
        elif opcion == '2':
            break
        else:
            print("Opción inválida.")
            input("\nPresione Enter para continuar...")

# 3. Métodos de Búsqueda
def busqueda_lineal(lista, objetivo):
    for i in range(len(lista)):
        if lista[i] == objetivo:
            return i
    return -1

def menu_busqueda():
    while True:
        limpiar_pantalla()
        mostrar_encabezado()
        print("\n--- MÓDULO 3: BÚSQUEDA (Lineal) ---")
        print("1. Buscar un número en una lista")
        print("2. Volver al Menú Principal")
        opcion = input("\nSeleccione una opción (1-2): ")
        
        if opcion == '1':
            entrada = input("\nIngrese números separados por espacios: ")
            try:
                lista = [int(x) for x in entrada.split()]
                if not lista:
                    print("La lista está vacía.")
                else:
                    objetivo = int(input("Ingrese el número que desea buscar: "))
                    pos = busqueda_lineal(lista, objetivo)
                    if pos != -1:
                        print(f"¡Encontrado! El número {objetivo} está en la posición (índice) {pos}.")
                    else:
                        print(f"El número {objetivo} no se encuentra en la lista.")
            except ValueError:
                print("Error: Ingrese valores numéricos válidos.")
            input("\nPresione Enter para continuar...")
        elif opcion == '2':
            break
        else:
            print("Opción inválida.")
            input("\nPresione Enter para continuar...")

def main():
    while True:
        limpiar_pantalla()
        mostrar_encabezado()
        print("\n--- MENÚ PRINCIPAL ---")
        print("1. Recursividad (Factorial y Fibonacci)")
        print("2. Ordenación (Método Burbuja)")
        print("3. Búsqueda (Búsqueda Lineal)")
        print("4. Salir")
        
        opcion = input("\nSeleccione una opción (1-4): ")
        
        if opcion == '1':
            menu_recursividad()
        elif opcion == '2':
            menu_ordenacion()
        elif opcion == '3':
            menu_busqueda()
        elif opcion == '4':
            limpiar_pantalla()
            print("Programa finalizado correctamente. ¡Hasta luego!")
            break
        else:
            print("Opción no válida. Intente de nuevo.")
            input("\nPresione Enter para continuar...")

if __name__ == "__main__":
    main()