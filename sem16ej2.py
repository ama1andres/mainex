#3. Cree una función que retorne la suma de todos los números de una lista.
    #1. La función va a tener un parámetro (la lista) y retornar un numero (la suma de todos sus elementos).

import pytest

def lista_numeros(lista):
    suma_numeros = sum(lista) 
    return suma_numeros

def test_lista_numeros():
    assert lista_numeros([1, 6, 4, 21]) == 32
    assert lista_numeros([0, 0, 0]) == 0       

lista = [1, 6, 4, 21]
resultado = lista_numeros(lista)
print(f'El resultado de la suma es {resultado}')
