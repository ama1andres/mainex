numero_usuario = int(input("ingrese un numero del 1 al 10: "))

numero_adivina = 9

while numero_usuario != numero_adivina:
    print("numero incorrecto, intenta de nuevo ")
    numero_usuario = int(input("ingrese un numero del 1 al 10: "))

print("el numero  es correcto")