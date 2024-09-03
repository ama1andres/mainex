numero_usuario_1 = int(input("ingrese el primer numero"))
numero_usuario_2 = int(input("ingrese el segundo numero"))
numero_usuario_3 = int(input("ingrese el tercer numero"))

numero_mayor = 0

if (numero_usuario_1 >= numero_usuario_2) and (numero_usuario_1 >= numero_usuario_3):
    numero_mayor = numero_usuario_1
elif (numero_usuario_2 >= numero_usuario_1) and (numero_usuario_2 >= numero_usuario_3):
    numero_mayor = numero_usuario_2
else:
    numero_mayor = numero_usuario_3

print(f'el numero mayor es {numero_mayor}')