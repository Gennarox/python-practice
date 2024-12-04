try:
  div = lambda a:a/0
  print(type(div))
  result = div(1000)
except ZeroDivisionError as error:
  print(f"Aqui hubo un error -> {error}") #es una buena practica de ing. capturar errores y tratar esos datos de manera apartada

try:
  assert 1 != 1, "Uno no es uno bro"
except AssertionError as error:
  print(type(error))
  print(f"Cagaste aqui bro -> {error}")

print("Jajaj, esto se ejecutó igual")

#Finalmente un bloque de codigo real quedaría asi con la logica y las excepciones finalmente
try:
  div = lambda a:a/0
  print(type(div))
  print("*"*20) #esto si se ejecuta
  result = div(1000) #error
  print("*"*20) #esto ya no se ejecuta
  assert 1 != 1, "Uno no es uno bro"

except ZeroDivisionError as error:
  print(f"Aqui hubo un error -> {error}")

except AssertionError as error:
  print(type(error))
  print(f"Cagaste aqui bro -> {error}")

print("Jajaj, esto se ejecutó igual x2")

print("*"*10 + "Ejercicio platzi, excepcion directa sin capturar error en variable" + "*"*10)
def my_divide(a, b):
   try:
      result = a / b
   except ZeroDivisionError:
      result = "No se puede dividir por 0"
   return result

response = my_divide(10, 2)
print(response) # 5

response = my_divide(10, 0)
print(response) # No se puede dividir por 0
