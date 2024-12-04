set_countries = {'par', 'arg', 'bra', 'uru'} #similar a diccionario
print(set_countries)
print(type(set_countries))

#no puede tener elementos repetidos
set_countries = {'par', 'arg', 'bra', 'uru', 'uru'} #elimina el duplicado
print(set_countries)

set_anything = {'par', 123, False, 'uru', True, 0.33333} #ojo, lo ordena pero no indica un orden realmente en la estructura del dato
print(set_anything)

set_from_string = set('hooooooooooooooOOOOla') #crea un set a partir de un string
print(set_from_string)

set_from_tuples = set(('abc', 'cbv', 'xyz', 123))
print(set_from_tuples)

numbers = [1,2,3,4,5,6,7,8,9,10,1,2,3,4,5,6,7,8,9,10]
set_from_number_list = set(numbers)
print(set_from_number_list)

distinct_numbers = list(set_from_number_list) #eliminamos duplicados
