#tenemos que importar el objeto csv
import csv

#usamos el newline para evitar errores con espacios 
with open("C:\\Users\\andre\\Desktop\\lyfter andres\\ejercicio semana 8\\juegos.txt", "w", newline='') as archivo:

    # se usa csv writer para escribir en el archivo y un delimitador que por cada palabra se usa un espacio de tabulacion 't'
    writer = csv.writer(archivo, delimiter='\t')
    
    # header
    writer.writerow(["nombre", "genero", "desarrollador", "clasificacion"])
    

    cantidad_juegos = int(input("Ingrese la cantidad de juegos: "))
    
    for juegos in range(cantidad_juegos):
        nombre = input("Ingrese el nombre del juego: ")
        genero = input("Ingrese el género del juego: ")
        desarrollador = input("Ingrese el desarrollador del juego: ")
        clasificacion = input("Ingrese la clasificación del juego: ")
        
        # writer.row escribe los input en el archivo por columnas
        writer.writerow([nombre, genero, desarrollador, clasificacion])

print(f'Se guardaron {cantidad_juegos} juegos en C:\\Users\\andre\\Desktop\\lyfter andres\\ejercicio semana 8\\juegos.txt')
#nombre	genero	desarrollador	clasificacion
#r	r	r	d
#s	s	s	s 

