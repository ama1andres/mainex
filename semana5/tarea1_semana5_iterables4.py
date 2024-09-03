my_list = [
    '1',
    '2',
    '3',
    '4',
    '5',
    '6',
    '7',
    '8',
    '9',
    '10',
]

num_par = []

num_impar = []

for num in my_list:
    if (int(num) % 2) == 0:
        num_par.append(num)
    else:
        num_impar.append(num)
print("numeros pares",num_par)
print("numeros pares",num_impar)