
def mayusculas_minusculas(texto):
    
    mayusculas = 0
    minusculas = 0

    for caracter in texto:
        if caracter.isupper():
            mayusculas += 1
        elif caracter.islower():
            minusculas += 1  
    
    print(f'La cantidad de mayúsculas es {mayusculas}')
    print(f'La cantidad de minúsculas es {minusculas}')

mi_string = "AndrEs MadrigAL"
mayusculas_minusculas(mi_string)