import random

array = [random.randint(1, 100) for _ in range(1000)]

print(f'{array}')

def bubble_sort(array):
    n = len(array)
    for i in range (n):
        for j in range(0, n - i - 1):
            if array[j] > array[j+1]:
                temp = array[j]
                array[j] = array[j + 1]
                array[j + 1] = temp
    return array

print(f'{array}')