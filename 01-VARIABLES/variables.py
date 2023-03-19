# Variables, PYTHON ES UN LENGUAJE INTERPRETADO
# Para definirlas se escribe todo en minuscula, lo normal es poner 'mi_variable'

my_string_variable = "My String variable"
print(my_string_variable)

my_int_variable = 5
print(my_int_variable)

my_bool_variable = True
print(my_bool_variable)

my_int_to_str_variable = str(my_int_variable) #El casteo a un tipo de dato a otro

print(my_int_to_str_variable)
print(type(my_int_to_str_variable))

# Concatenacion de varibles en un print
print(my_string_variable, str(my_int_variable),my_bool_variable)

#Funciones del sistema
print('Los caracteres totales de la variable de dato string es de ',
      len(my_string_variable)) #Cuenta caracteres + espacion (el length de java)

#Variables en una sola linea (No es lo mas inteligente, debido a que se puede meter la pata!!!)

name, surname, alias, edad = 'Eduardo', 'Martin-Sonseca','maraloeDev', 23
print("Mi nombre es ",name, "Mi apellido es",surname, "Y mi alias es ",alias, " . Mi edad es de", edad)

#Mejor asi
print('Nombre ',name)
print('Apellidos ', surname)
print('Alias ',alias)
print('Edad ',edad)

#Input (El scanner de java)
name = input('Cual es tu nombre ')
edad = input('Cual es tu edad ')
print(name)
print(edad)

#Cambiar tipo
name = 23
edad = 'Eduardo'

print(name)
print(edad)

address = 'Mi direccion'
address = 23

print(type(address))