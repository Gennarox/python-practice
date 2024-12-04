print(0/0) #ZeroDivisionError: division by zero
(0/0 #SyntaxError: '(' was never closed
print("Esto no se va a ejecutar a")  #python detiene el programa al identificar un error, no imprime lo sgte

a_numbers = [1, 2, 3]
b_numbers = [4, 5, 6]
value = list(map(lambda x, y: x * y, a_numbers, b_numbers))
new_values = list(filter(lambda x: x > 5, value))
print(f"Map aplicado sobre dos listas -> {value}")
print(f"Filter aplicado -> {new_values}")

#assert = prueba de hipotesis, verificacion para seguir ejecutando el programa

suma_v2 = lambda x, y: x + y
assert suma_v2(10, 20) == 30  #AssertionError
print(type(suma_v2))

age = 10
if age <= 18:
  raise Exception("No se permiten menores de edad") #Exception
