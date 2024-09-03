my_list = [
    '2',
    '54',
    'hola',
    '84',
]

if len(my_list) > 1:
    my_list[0], my_list[-1] = my_list[-1], my_list[0]
    print(my_list)