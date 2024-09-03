

contador_de_notas = 1
cantidad_de_notas_aprobadas = 0
cantidad_de_notas_desaprobadas = 0
promedio_de_notas_aprobadas = 0
promedio_de_notas_desaprobadas = 0
promedio_de_notas_total = 0

total_de_notas = int(input("Ingrese la cantidad de notas: "))

while contador_de_notas <= total_de_notas:
    print(f"Ingrese la nota numero {contador_de_notas} ")
    nota_actual = int(input("ingrese la nota "))
    
    if nota_actual < 70:
        cantidad_de_notas_desaprobadas = cantidad_de_notas_aprobadas + 1
        promedio_de_notas_desaprobadas = promedio_de_notas_desaprobadas + nota_actual
    else:
        cantidad_de_notas_aprobadas = cantidad_de_notas_aprobadas + 1
        promedio_de_notas_aprobadas = promedio_de_notas_aprobadas + nota_actual
    
    promedio_de_notas_total = promedio_de_notas_total +  (nota_actual / total_de_notas)
    
    contador_de_notas = contador_de_notas +1



if cantidad_de_notas_aprobadas > 0:
    promedio_de_notas_aprobadas = promedio_de_notas_aprobadas  /  cantidad_de_notas_aprobadas 

if cantidad_de_notas_desaprobadas > 0:
    promedio_de_notas_desaprobadas = promedio_de_notas_desaprobadas / cantidad_de_notas_desaprobadas
#incluir estado reprobado o aprovado para practicar.
if promedio_de_notas_total < 70 :
    print("el estudiante esta reprobado")
elif promedio_de_notas_aprobadas >= 70:
    print("el estudiante esta aprobado")

print(f"el estudiante tiene: {cantidad_de_notas_aprobadas} notas aprobadas")
print(f"el promedio de las notas aprobadas es: {promedio_de_notas_aprobadas:}")
print(f"el estudiante tiene: {cantidad_de_notas_desaprobadas} notas desaprobadas")
print(f"el promedio de las notas desaprobadas es: {promedio_de_notas_desaprobadas}")
print(f"el promedio total de las notas es: {promedio_de_notas_total:}")

