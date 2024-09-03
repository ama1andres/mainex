list_keys = ['access_level', 'age']
employee = {'name': 'andres', 'email': 'andm@gmail.com', 'access_level': '2', 'age': '19'}
#usando del logre ver que si tengo una variable ejemplo key y le doy el valor de mi lista, 
# y si key ya con el valor de los string esta dentro de employee, lograre borrar el valor de key si esta en employee e imprimir employee ya sin los valores de key.

for key in list_keys:
    if key in employee:
        del employee[key]

print(employee)