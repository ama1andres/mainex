lista = [

]
while len (lista) < 10:

    numeros = int(input(f"ingresa la lista {len (lista) +1 } "))
    lista.append(numeros)
print("numeros ingresados" ,lista)

max_num = max(lista)
print(f"el numeros mas alto es {max_num}")