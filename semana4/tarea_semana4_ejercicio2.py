#2.Cree un programa que le pida al usuario su
#  nombre, apellido, y edad, y muestre si es un bebé, niño, preadolescente, adolescente, adulto joven, adulto, o adulto mayor.
nombre_usuario = input("ingrese su nombre ")

apellido_usuario = input("ingrese su apellido ")

edad_usuario = int(input("ingrese su edad "))

if (edad_usuario < 5 ):
    print(f'{nombre_usuario} {apellido_usuario} es un bebe')
elif(edad_usuario < 10):
    print(f'{nombre_usuario} {apellido_usuario} es un nino')
elif(edad_usuario < 15):
    print(f'{nombre_usuario} {apellido_usuario} es un preadolescente')

elif(edad_usuario < 18):
    print(f'{nombre_usuario} {apellido_usuario} es un adolescente')

elif(edad_usuario < 30):
    print(f'{nombre_usuario} {apellido_usuario} es un adulto joven')

elif(edad_usuario < 65):
    print(f'{nombre_usuario} {apellido_usuario} es un adulto')

else:
    print(f'{nombre_usuario} {apellido_usuario} es un adulto mayor')
    
print("muchas gracias")