#  verificar si un número es primo
def num_primo(n):
    num_primo = n > 1 
    for i in range(2, n):
        if n % i == 0:
            num_primo = False
            break
    return num_primo


# filtrar los  primos de una lista, busque este ejemplo, se utiliza . append para agregar el numero primo que se descubre en la primera funcion con el parametro "n", se agrega a lista primos
def obtener_primos(lista_numeros):
    lista_primos = []
    for n in lista_numeros:
        if num_primo(n):
            lista_primos.append(n)
    return lista_primos


numeros = [281, 4, 77, 7, 54, 1, 71]
primos = obtener_primos(numeros)

print(f"Los numeros primos en la lista son: {primos}")
