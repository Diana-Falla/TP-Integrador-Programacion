# Integrantes: Diana Falla, Claudio Fiorito
from colorama import init, Fore, Back, Style
init()
# 
# 
# Algoritmo de ordenamiento: Selection Sort
def ordenamiento_s_sort(lista):
    n = len(lista)
    for i in range(n):
        min_indice = i
        for j in range(i+1, n):
            if lista[j] < lista[min_indice]:
                min_indice = j
        lista[i], lista[min_indice] = lista[min_indice], lista[i]

# Algoritmo de búsqueda: Búsqueda lineal
def busqueda_lineal(lista, valor):
    for i in range(len(lista)):
        if lista[i] == valor:
            return i
    return -1

# Lista de edades
edades = [21, 18, 25, 19, 22, 20, 23]

print(Fore.GREEN + "Lista de EDADES de los estudiantes:", edades)

# Ordenar la lista
ordenamiento_s_sort(edades)
print(Fore.CYAN + "Lista ordenada:", edades)

# Buscar una edad específica
edad_buscada = int(input(Fore.LIGHTMAGENTA_EX + "Ingrese la edad a buscar: "))
posicion = busqueda_lineal(edades, edad_buscada)

if posicion != -1:
    print(f"La edad {edad_buscada} se encuentra en la posición {posicion} de la lista.")
else:
    print(f"La edad {edad_buscada} no se encuentra en la lista.")
