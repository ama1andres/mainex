#no me quedo del todo clara al primera instruccion.
def primera_variable ():
    variable_local = "variable"
    print (variable_local)
primera_variable()


variable_global  = "variable global"


def segunda_variable ():
    variable_global = "valor modificado"
    print (variable_global)


#si printeo la funcion, la variable global cambia su valor por el definido en la funcion
segunda_variable()


#si printeo la variable global, mantiene su valor
print(variable_global)