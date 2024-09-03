import json

# archivo JSON, se agrega el archivo a una varaible para solo colocar la variable cuando ocupemos poner el archivo
archivo_ruta = r'C:\Users\andre\Desktop\lyfter andres\ejercicio semana 8\pokemon.json'

# busque como hacer este ejercicio con otro ejemplos, vi que usabn try y expect cuando se le a;ade info al archivo con el load
try:
    with open(archivo_ruta, 'r') as archivo:
        
        pokemones = json.load(archivo)

except (FileNotFoundError, json.JSONDecodeError):

    print("El archivo {archivo_ruta}  creara un nuevo archivo")
    pokemones = []

nombre = input("Ingresa el nombre del Pokemon: ")
tipo = input("Ingresa el tipo del Pokemon: ")
nivel = int(input("Ingresa el nivel del Pokemon (numero) :  "))

# diccionario poke
nuevo_pokemon = {
    "nombre": nombre,
    "tipo": tipo,
    "nivel": nivel
}

# Agregar nuevo pokemon
pokemones.append(nuevo_pokemon)


with open(archivo_ruta, 'w') as archivo:
    #indent es para la sangria entre mas alto el numero mayor la sangria en el archivo
    json.dump(pokemones, archivo, indent=1)

print(f"El Pokemon {nombre} agregado al archivo {archivo_ruta}")
