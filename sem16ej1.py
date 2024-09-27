import pytest
# este ejemplo me guie con ejemplos que busque  de bubble sort para hacer la lista  vacia y parametros que no son lista, ademas de buscar de nuevo el algoritmo
#  algoritmo bubble_sort
def bubble_sort(arr):
    if not isinstance(arr, list):
        raise TypeError("Input be a list")
    n = len(arr)
    for i in range(n):
        for j in range(0, n - i - 1):
            if arr[j] > arr[j + 1]:
                arr[j], arr[j + 1] = arr[j + 1], arr[j]

# Funciona con una lista pequeña
def test_small_list():
    data = [3, 2, 1]

    expected = [1, 2, 3]
    bubble_sort(data)
    assert data == expected

#  Funciona con una lista de 100 elementos
def test_large_list():
    data = list(range(100, 0, -1)) 
    expected = list(range(1, 100))  
    bubble_sort(data)
    assert data == expected

# Funciona lista vacia
def test_empty_list():
    data = []
    expected = []

    bubble_sort(data)
    assert data == expected

# No funciona con parametros que no son lista
def test_non_list_parameter():
    data = 401
    with pytest.raises(TypeError):
        bubble_sort(data)
