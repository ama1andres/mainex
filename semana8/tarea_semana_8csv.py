#tuve un error de SyntaxError: (unicode error) 'unicodeescape' codec can't decode bytes in position 2-3: truncated \UXXXXXXXX escape, lo arregle usando doble barrar en el file

archivo = open("C:\\Users\\andre\\Desktop\\lyfter andres\\ejercicio semana 8\\juegos.txt", "w")

archivo.write("nombre,genero,desarrollador,clasificacion\n")

cantidad_juegos = int(input("Ingrese la cantidad de juegos: "))

for juegos in range(cantidad_juegos):
    nombre = input("Ingrese el nombre del videojuego: ")
    genero = input("Ingrese el género del videojuego: ")
    desarrollador = input("Ingrese el desarrollador del videojuego: ")
    clasificacion = input("Ingrese la clasificación del videojuego: ")

    archivo.write(f'{nombre},{genero},{desarrollador},{clasificacion}\n')

archivo.close()

print(f'Se guardaron {cantidad_juegos} juegos en C:\\Users\\andre\\Desktop\\lyfter andres\\ejercicio semana 8\\juegos.txt')
