
import pytest

def num_primo(n):
    if n <= 1:
        return False
    for i in range(2, n):
        if n % i == 0:
            return False
    return True


def obtener_primos(lista_numeros):
    lista_primos = []
    for n in lista_numeros:
        if num_primo(n):
            lista_primos.append(n)
    return lista_primos


numeros = [281, 4, 77, 7, 54, 1, 71]
primos = obtener_primos(numeros)
print(f"Los numeros primos son: {primos}")


def test_num_primo():
    assert num_primo(7) == True
    assert num_primo(10) == False     
    assert num_primo(1) == False      
    assert num_primo(2) == True       
    assert num_primo(0) == False      


def test_obtener_primos():
    assert obtener_primos([281, 4, 77, 7, 54, 1, 71]) == [281, 7, 71]
    assert obtener_primos([2, 3, 5, 7]) == [2, 3, 5, 7]     
    assert obtener_primos([0, 1, 4, 6]) == []                             
