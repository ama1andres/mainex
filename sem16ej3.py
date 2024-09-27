#se crea un parametro para guardar el string que queremos con una variable y le indicamos que lo invierta
import pytest

def string_inv(palabras):
    return palabras[::-1]

parametro_palabras = "me gusta la playa"
resultado = string_inv(parametro_palabras)
print(f'El string invertido es: "{resultado}"')

def test_string_inv():
    assert string_inv("me gusta la playa") == "ayalp al atsug em" 
    assert string_inv("Hola mundo") == "odnum aloH"               
    assert string_inv("Python") == "nohtyP"                       
