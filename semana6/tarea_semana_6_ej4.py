
#se crea un parametro para guardar el string que queremos con una variable y le indicamos que lo invierta
def string_inv(palabras):
    return palabras [::-1]

parametro_palabras = "me gusta la playa "

resultado = string_inv(parametro_palabras)

print (f'el string invertido es {resultado}')


