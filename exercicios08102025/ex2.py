import random

def particao(array, inicio, final):
    pivo = array[final]
    i = inicio - 1

    for j in range(inicio, final):
        if array[j] <= pivo:
            i += 1
            array[i], array[j] = array[j], array[i]

    array[i + 1], array[final] = array[final], array[i + 1]
    return i + 1


def quick_sort(array, inicio, final):
    if inicio < final:
        posicao = particao(array, inicio, final)

        # Esquerda
        quick_sort(array, inicio, posicao - 1)

        # Direita
        quick_sort(array, posicao + 1, final)

    return array


# Demonstração com 1000 números
lista_numeros = [random.randint(0, 10000) for _ in range(1000)]
print("\nQuick Sort - Lista ordenada (1000 números):")
print(quick_sort(lista_numeros, 0, len(lista_numeros) - 1))

# Demonstração com lista de nomes
nomes = ["Ana", "Carlos", "Beatriz", "Eduardo", "João", "Felipe", "Bruna"]
print("\nQuick Sort - Lista de nomes ordenada:")
print(quick_sort(nomes, 0, len(nomes) - 1))
