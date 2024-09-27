# Función que cuenta las letras mayúsculas y minúsculas en un string


import pytest
def mayusculas_minusculas(texto):
    mayusculas = 0
    minusculas = 0

    for caracter in texto:
        if caracter.isupper():
            mayusculas += 1
        elif caracter.islower():
            minusculas += 1  
    
    print(f'La cantidad de mayusculas es {mayusculas}')
    print(f'La cantidad de minusculas es {minusculas}')

    return mayusculas, minusculas

mi_string = "AndrEs MadrigAL"
mayusculas_minusculas(mi_string)

def test_mayusculas_minusculas():
    assert mayusculas_minusculas("AndrEs MadrigAL") == (5, 8)
    assert mayusculas_minusculas("Hola Mundo") == (2, 7)      
    assert mayusculas_minusculas("PYTHON") == (6, 0)             
