print('Creacion de listas con ciclos')
numbers = []
for element in range(1,11):
  numbers.append(element)

print(numbers) #Código sin list comprehension

numbers_v2 = [element for element in range(1,11)]
print(numbers_v2) #Código con list comprehension}

#Con operación
numbers = []
for element in range(1,11):
  numbers.append(element*2)

print(numbers)

numbers_v2 = [element *2 for element in range(1,11)]
print(numbers_v2)

print('Creacion de listas con filtro opcional con ciclos')

numbers_pair = []
for i in range(1,101):
  if i%2==0:
    numbers_pair.append(i*2)
print(numbers_pair) #sin list comprehension

numbers_pair = [element*2 for element in range(1,101) if element%2 == 0]
print(numbers_pair) #con list comprehension

#Ejercicio platzi
numbers = [35, 16, 10, 34, 37, 25]

even_numbers = []
for number in numbers:
  if number % 2 == 0:
    even_numbers.append(number)
print('v1 =>', even_numbers)

# Ahora usando List Comprehension 👇
even_numbers_v2 = [number for number in numbers if number%2==0]

print('v2 =>', even_numbers_v2)