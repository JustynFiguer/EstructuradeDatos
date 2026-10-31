# ============================================================================
# Universidad de Panamá
# Facultad de Informática, Electrónica y Comunicación
# Escuela de Ciencias de la Computación y Computación Móvil
# Asignatura: Estructura de Datos II (INF 222)
# Estudiante: Justiniano Figueroa
# Profesor: [Nombre del Profesor]
# Fecha: 31 de octubre de 2026
# Descripción: Laboratorio N° 10 - Recursividad, Ordenación y Búsqueda
# ============================================================================

def busqueda_binaria_recursiva(arr, izquierda, derecha, valor):
    if izquierda > derecha:
        return -1  # No encontrado
    
    medio = izquierda + (derecha - izquierda) // 2
    
    if arr[medio] == valor:
        return medio
    if arr[medio] > valor:
        return busqueda_binaria_recursiva(arr, izquierda, medio - 1, valor)
    return busqueda_binaria_recursiva(arr, medio + 1, derecha, valor)

def mostrar_lista(arr):
    print(" ".join(map(str, arr)))

def main():
    print("============================================================")
    print(" Universidad de Panama")
    print(" Facultad de Informatica, Electronica y Comunicacion")
    print(" Laboratorio N 10 - Recursividad y Búsqueda")
    print("============================================================")
    print()

    datos = [12, 25, 38, 45, 59, 72, 84, 91, 105]
    valor_buscado = 72

    print("Elementos de la lista ordenada: ", end="")
    mostrar_lista(datos)

    resultado = busqueda_binaria_recursiva(datos, 0, len(datos) - 1, valor_buscado)

    if resultado != -1:
        print(f"Elemento {valor_buscado} encontrado en el indice: {resultado}")
    else:
        print(f"Elemento {valor_buscado} no encontrado en la lista.")

    print()
    input("Presiona ENTER para salir...")

if __name__ == "__main__":
    main()
