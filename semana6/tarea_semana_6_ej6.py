def orden_palabras (texto):
#split convierte el sitrng en una lista de palabras, separa lo que le indiquemos en el parentesis "-"
    palabras = texto.split ('-')
#.sort ordena la lista alfabeticamentr
    palabras.sort()
#.join une la lista ya ordenada de nuevo separado por guiones
    texto_ordenado = '-'.join(palabras)

    return texto_ordenado


mi_string = "hola-mi-nombre-es-andres"

resultado = orden_palabras(mi_string)

print(f'las palabras ordenadas son: {resultado}')