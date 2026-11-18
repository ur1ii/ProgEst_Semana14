
#Version Básica

def burbuja(lista):
    n = len(lista)
    for i in range(n - 1):              # número de pasadas
        for j in range(n - 1 - i):      # los últimos i ya están ordenados
            if lista[j] > lista[j + 1]:
                # intercambio al estilo Python
                lista[j], lista[j + 1] = lista[j + 1], lista[j]
    return lista

numeros = [5, 3, 8, 4, 2]
print(burbuja(numeros))   # [2, 3, 4, 5, 8]

#Version Optimizada

def burbuja_optimizada(lista):
    n = len(lista)
    for i in range(n - 1):
        hubo_intercambio = False
        for j in range(n - 1 - i):
            if lista[j] > lista[j + 1]:
                lista[j], lista[j + 1] = lista[j + 1], lista[j]
                hubo_intercambio = True
        if not hubo_intercambio:   # si no se movió nada, ya está ordenada
            break
    return lista

print(burbuja_optimizada([1, 2, 3, 4, 5]))  # termina tras 1 sola pasada → O(n)

#Con Contadores

def burbuja_analisis(lista):
    comparaciones = 0
    intercambios = 0
    n = len(lista)
    for i in range(n - 1):
        for j in range(n - 1 - i):
            comparaciones += 1
            if lista[j] > lista[j + 1]:
                lista[j], lista[j + 1] = lista[j + 1], lista[j]
                intercambios += 1
    print("Comparaciones:", comparaciones)
    print("Intercambios:", intercambios)
    return lista

burbuja_analisis([5, 3, 8, 4, 2])
#Comparaciones: 10
#Intercambios: 7

#Practica

'''
Resultado esperado: (Escrito en cuaderno)
97 - 79
95 - 59
93 - 39
91 - 19

75319

75 - 57
73 - 37
71 - 17

53179

53 - 35
51 - 15

31579

31 - 13

13579
'''
burbuja_analisis([9, 7, 5, 3, 1])

#Retorna al revez
def burbuja(lista):
    n = len(lista)
    for i in range(n - 1):              # número de pasadas
        for j in range(n - 1 - i):      # los últimos i ya están ordenados
            if lista[j+1] > lista[j]:
                # intercambio al estilo Python
                lista[j+1], lista[j] = lista[j], lista[j+1]
    return lista

numeros = [5, 3, 8, 4, 2]
print(f"{burbuja(numeros)} \n")   # [2, 3, 4, 5, 8]

import time
import random
import math

import time
import random

# 1. BUBBLE SORT OPTIMIZADO

def bubble_sort(lista):
    arr = lista.copy()
    n = len(arr)

    for i in range(n - 1):
        cambiado = False

        for j in range(n - i - 1):
            if arr[j] > arr[j + 1]:
                arr[j], arr[j + 1] = arr[j + 1], arr[j]
                cambiado = True

        if not cambiado:
            break

    return arr



# 2. SELECTION SORT OPTIMIZADO

def selection_sort(lista):
    arr = lista.copy()
    n = len(arr)

    for i in range(n - 1):
        minimo = i

        for j in range(i + 1, n):
            if arr[j] < arr[minimo]:
                minimo = j

        if minimo != i:
            arr[i], arr[minimo] = arr[minimo], arr[i]

    return arr



# 3. INSERTION SORT OPTIMIZADO

def insertion_sort(lista):
    arr = lista.copy()

    for i in range(1, len(arr)):
        actual = arr[i]

        if actual >= arr[i - 1]:
            continue

        j = i - 1

        while j >= 0 and arr[j] > actual:
            arr[j + 1] = arr[j]
            j -= 1

        arr[j + 1] = actual

    return arr



# 4. MERGE SORT OPTIMIZADO

def merge_sort(lista):
    arr = lista.copy()
    auxiliar = [0] * len(arr)

    def ordenar(izquierda, derecha):
        if derecha - izquierda <= 1:
            return

        mitad = (izquierda + derecha) // 2

        ordenar(izquierda, mitad)
        ordenar(mitad, derecha)

        # Evita mezclar si ambas mitades ya están ordenadas
        if arr[mitad - 1] <= arr[mitad]:
            return

        i = izquierda
        j = mitad
        k = izquierda

        while i < mitad and j < derecha:
            if arr[i] <= arr[j]:
                auxiliar[k] = arr[i]
                i += 1
            else:
                auxiliar[k] = arr[j]
                j += 1
            k += 1

        while i < mitad:
            auxiliar[k] = arr[i]
            i += 1
            k += 1

        while j < derecha:
            auxiliar[k] = arr[j]
            j += 1
            k += 1

        arr[izquierda:derecha] = auxiliar[izquierda:derecha]

    ordenar(0, len(arr))
    return arr



# 5. QUICK SORT OPTIMIZADO

def quick_sort(lista):
    arr = lista.copy()

    def ordenar(izquierda, derecha):
        while izquierda < derecha:

            pivote = arr[(izquierda + derecha) // 2]
            i = izquierda
            j = derecha

            while i <= j:
                while arr[i] < pivote:
                    i += 1

                while arr[j] > pivote:
                    j -= 1

                if i <= j:
                    arr[i], arr[j] = arr[j], arr[i]
                    i += 1
                    j -= 1

            # Procesa primero la partición más pequeña
            if j - izquierda < derecha - i:
                ordenar(izquierda, j)
                izquierda = i
            else:
                ordenar(i, derecha)
                derecha = j

    ordenar(0, len(arr) - 1)
    return arr



# PRUEBA Y COMPARACIÓN DE RENDIMIENTO


numeros = [8, 3, 5, 1, 9, 2, 7, 4, 6]

metodos = [
    ("Bubble Sort", bubble_sort),
    ("Selection Sort", selection_sort),
    ("Insertion Sort", insertion_sort),
    ("Merge Sort", merge_sort),
    ("Quick Sort", quick_sort)
]

print("LISTA ORIGINAL:", numeros)
print("-" * 55)

for nombre, metodo in metodos:
    inicio = time.perf_counter()

    resultado = metodo(numeros)

    fin = time.perf_counter()
    tiempo = fin - inicio

    print(f"{nombre:18} | {resultado}")
    print(f"Tiempo: {tiempo:.8f} segundos")
    print("-" * 55)



# PRUEBA CON UNA LISTA GRANDE


datos = [random.randint(1, 10000) for _ in range(1000)]

print("\nPRUEBA CON 1000 ELEMENTOS")

for nombre, metodo in metodos:
    inicio = time.perf_counter()
    resultado = metodo(datos)
    fin = time.perf_counter()

    print(f"{nombre:18} : {fin - inicio:.6f} segundos")

# 6. COUNTING SORT (Ordenamiento por conteo)

def counting_sort(lista):
    if not lista:
        return []

    minimo = min(lista)
    maximo = max(lista)

    rango = maximo - minimo + 1
    conteo = [0] * rango

    for numero in lista:
        conteo[numero - minimo] += 1

    resultado = []

    for i, cantidad in enumerate(conteo):
        resultado.extend([i + minimo] * cantidad)

    return resultado

# 7. BUCKET SORT (Ordenamiento por cubetas)

def bucket_sort(lista):
    if len(lista) <= 1:
        return lista.copy()

    minimo = min(lista)
    maximo = max(lista)

    if minimo == maximo:
        return lista.copy()

    cantidad = len(lista)
    cubetas = [[] for _ in range(cantidad)]

    rango = maximo - minimo

    for numero in lista:
        indice = int((numero - minimo) * (cantidad - 1) / rango)
        cubetas[indice].append(numero)

    resultado = []

    for cubeta in cubetas:
        cubeta.sort()
        resultado.extend(cubeta)

    return resultado

# 8. RADIX SORT (Ordenamiento por dígitos)

def radix_sort(lista):
    if not lista:
        return []

    arr = lista.copy()

    # Separar números negativos y positivos
    negativos = [-x for x in arr if x < 0]
    positivos = [x for x in arr if x >= 0]

    def ordenar_digitos(numeros):
        if not numeros:
            return []

        maximo = max(numeros)
        exp = 1

        while maximo // exp > 0:
            conteo = [0] * 10
            salida = [0] * len(numeros)

            for numero in numeros:
                indice = (numero // exp) % 10
                conteo[indice] += 1

            for i in range(1, 10):
                conteo[i] += conteo[i - 1]

            for numero in reversed(numeros):
                indice = (numero // exp) % 10
                conteo[indice] -= 1
                salida[conteo[indice]] = numero

            numeros = salida
            exp *= 10

        return numeros

    negativos = ordenar_digitos(negativos)
    positivos = ordenar_digitos(positivos)

    return [-x for x in reversed(negativos)] + positivos

# 9. HEAP SORT (Ordenamiento por montículos)

def heap_sort(lista):
    arr = lista.copy()
    n = len(arr)

    def heapify(n, i):
        mayor = i
        izquierda = 2 * i + 1
        derecha = 2 * i + 2

        if izquierda < n and arr[izquierda] > arr[mayor]:
            mayor = izquierda

        if derecha < n and arr[derecha] > arr[mayor]:
            mayor = derecha

        if mayor != i:
            arr[i], arr[mayor] = arr[mayor], arr[i]
            heapify(n, mayor)

    # Construcción del heap
    for i in range(n // 2 - 1, -1, -1):
        heapify(n, i)

    # Extracción de elementos
    for i in range(n - 1, 0, -1):
        arr[0], arr[i] = arr[i], arr[0]
        heapify(i, 0)

    return arr

# 10. SHELL SORT (Ordenamiento por intervalos)

def shell_sort(lista):
    arr = lista.copy()
    n = len(arr)

    intervalo = n // 2

    while intervalo > 0:

        for i in range(intervalo, n):
            actual = arr[i]
            j = i

            while j >= intervalo and arr[j - intervalo] > actual:
                arr[j] = arr[j - intervalo]
                j -= intervalo

            arr[j] = actual

        intervalo //= 2

    return arr

# PRUEBAS Y COMPARACIÓN

numeros = [8, 3, 5, 1, 9, 2, 7, 4, 6]

metodos = [
    ("Counting Sort", counting_sort),
    ("Bucket Sort", bucket_sort),
    ("Radix Sort", radix_sort),
    ("Heap Sort", heap_sort),
    ("Shell Sort", shell_sort)
]

print("\nLISTA ORIGINAL:", numeros)
print("-" * 55)

for nombre, metodo in metodos:
    inicio = time.perf_counter()

    resultado = metodo(numeros)

    fin = time.perf_counter()

    print(f"{nombre:18} | {resultado}")
    print(f"Tiempo: {fin - inicio:.8f} segundos")
    print("-" * 55)

# PRUEBA CON 1000 ELEMENTOS

datos = [random.randint(-10000, 10000) for _ in range(1000)]

print("\nPRUEBA CON 1000 ELEMENTOS")

for nombre, metodo in metodos:
    inicio = time.perf_counter()
    resultado = metodo(datos)
    fin = time.perf_counter()

    print(f"{nombre:18} : {fin - inicio:.6f} segundos")




