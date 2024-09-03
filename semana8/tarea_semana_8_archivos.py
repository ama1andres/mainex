#leer los nombres de canciones como una lista y ordenarlos alfabeticamente

with open('C:\\Users\\andre\\Desktop\\lyfter andres\\ejercicio semana 8\\canciones.txt', 'r') as archivo:
    canciones = archivo.readlines()

canciones.sort()

with open('C:\\Users\\andre\\Desktop\\lyfter andres\\ejercicio semana 8\\canciones_ordenadas.txt', 'w') as archivo:
    for cancion in canciones:
        #\n da un espacio entre cada cancion, escribe el archivo ya ordenado en un nuevo file
        archivo.write(cancion + '\n')

print("Las canciones ordenadas están en 'C:\\Users\\andre\\Desktop\\lyfter andres\\ejercicio semana 8\\canciones_ordenadas.txt'")
