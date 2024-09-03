#ejercicio calculadora, definir variable para numero actual en 0

numero_actual = 0

while True:
    print(f' Su numero actual es : {numero_actual} ')
    print(" menu de opciones ")
    print(" 1. suma ")
    print(" 2. resta ")
    print(" 3. multiplicacion ")
    print(" 4. division ")
    print(" 5. borrar resultado ")
    print(" 6. salir ")

    menu_calculadora = input(" ingrese una opcion del menu del 1 al 6 : ")

    # encontre la opcion de not in, se usa para buscar el numero ingresado en la lista y si no esta, continua con el print y sale programa.
    if menu_calculadora not in ['1', '2', '3', '4', '5', '6']:
        print (" Opcion invalida, ingrese un numero del 1 al 6 ")
        continue

    if menu_calculadora == '6':
        print(" saliendo del programa ")
        print(" muchas gracias :) ")
        break

    if menu_calculadora == '5':
        numero_actual = 0
        print(f' El resultado fue borrado')
        continue

    try:
        numero_usuario = float(input(" Ingrese el numero para la operacion : "))
    except ValueError:
        print(" valor invalido, ingrese un numero ")
        continue

    if menu_calculadora == '1':
        numero_actual = numero_actual + numero_usuario
        
    elif menu_calculadora == '2':
        numero_actual = numero_actual - numero_usuario
    elif menu_calculadora == '3':
        numero_actual *= numero_usuario
    elif menu_calculadora == '4':
        
        numero_actual = numero_actual / numero_usuario

    print ( f' El reultado es {numero_actual}')
    