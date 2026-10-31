# ==============================================================================
# UNIVERSIDAD DE PANAMÁ
# FACULTAD DE INFORMÁTICA, ELECTRÓNICA Y COMUNICACIÓN (FIEC)
# Asignatura: Estructura de Datos (INF222)
# Profesor: Ángel Ávila
# Estudiante / Desarrollador: Justiniano Figueroa
# Periodo: Segundo Semestre 2026
# Laboratorio 9: Ordenamiento y Búsqueda Avanzada
# ==============================================================================

def busqueda_binaria_recursiva(lista, objetivo, izquierda, derecha):
    if izquierda > derecha:
        return -1
    
    medio = (izquierda + derecha) // 2
    
    if lista[medio] == objetivo:
        return medio
    elif lista[medio] > objetivo:
        return busqueda_binaria_recursiva(lista, objetivo, izquierda, medio - 1)
    else:
        return busqueda_binaria_recursiva(lista, objetivo, medio + 1, derecha)

def quicksort(lista):
    if len(lista) <= 1:
        return lista
    
    pivote = lista[len(lista) // 2]
    izquierda = [x for x in lista if x < pivote]
    medio = [x for x in lista if x == pivote]
    derecha = [x for x in lista if x > pivote]
    
    return quicksort(izquierda) + medio + quicksort(derecha)

def main():
    print("UNIVERSIDAD DE PANAMÁ")
    print("FACULTAD DE INFORMÁTICA, ELECTRÓNICA Y COMUNICACIÓN (FIEC)")
    print("Asignatura: Estructura de Datos (INF222)")
    print("Profesor: Ángel Ávila")
    print("Estudiante / Desarrollador: Justiniano Figueroa")
    print("Periodo: Segundo Semestre 2026")
    print("Laboratorio 9: Ordenamiento y Búsqueda Avanzada")
    
    print("-----------------------------------------------------")   
    
    
    datos = [42, 15, 8, 90, 23, 55, 4, 71, 36]
    print("Lista original:", datos)
    
    datos_ordenados = quicksort(datos)
    print("Lista ordenada:", datos_ordenados)
    
    objetivo = 55
    resultado = busqueda_binaria_recursiva(datos_ordenados, objetivo, 0, len(datos_ordenados) - 1)
    
    if resultado != -1:
        print(f"Elemento {objetivo} encontrado en el índice: {resultado}")
    else:
        print(f"Elemento {objetivo} no encontrado.")
        
    input("\nPresiona Enter para salir...")

if __name__ == "__main__":
    main()
