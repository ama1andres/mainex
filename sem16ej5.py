
import pytest


def orden_palabras(texto):
    palabras = texto.split('-')
    palabras.sort()
    texto_ordenado = '-'.join(palabras)
    return texto_ordenado

mi_string = "hola-mi-nombre-es-andres"
resultado = orden_palabras(mi_string)
print(f'Las palabras ordenadas son: {resultado}')

def test_orden_palabras():
    assert orden_palabras("hola-mi-nombre-es-andres") == "andres-es-hola-mi-nombre"
    assert orden_palabras("python-variable-funcion-computadora-monitor") == "computadora-funcion-monitor-python-variable" 

