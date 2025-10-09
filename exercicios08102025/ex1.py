def merge_sort(array):
    # Divisão do Array
    if len(array) > 1:
        meio = len(array) // 2
        esquerda = array[:meio]
        direita = array[meio:]

        merge_sort(esquerda)
        merge_sort(direita)

        i = j = k = 0

        # Ordena esquerda e direita
        while i < len(esquerda) and j < len(direita):
            if esquerda[i] < direita[j]:
                array[k] = esquerda[i]
                i += 1
            else:
                array[k] = direita[j]
                j += 1
            k += 1

        # Ordenação final
        while i < len(esquerda):
            array[k] = esquerda[i]
            i += 1
            k += 1

        while j < len(direita):
            array[k] = direita[j]
            j += 1
            k += 1

    return array


# Demonstração com 1000 números
import random
lista_numeros = [random.randint(0, 10000) for _ in range(1000)]
print("Lista ordenada (1000 números):")
print(merge_sort(lista_numeros))

# Demonstração com lista de nomes
nomes = ["Ana", "Carlos", "Beatriz", "Eduardo", "João", "Felipe", "Bruna"]
print("\nLista de nomes ordenada:")
print(merge_sort(nomes))
