print(
    "Hola mundo"
)  #Funcion print, recibe un parametro de cadena de texto, en este ejemplo un argumento de Hola Mundo


#Funciones
def my_print():
  print("This is my print function")
  print("Hola" * 3)


def my_print2():
  text = input("Cual quieres que sea tu texto?")
  print(f"El texto que digite fue {text}.")


def suma():
  a = int(input("Primer valor -> "))
  b = int(input("Segundo valor -> "))

  print(f"La suma de los valores es {a+b}.")


#Funcion con parametros
def suma2(a, b):
  print(f"La suma es -> {a+b}")


my_print()
my_print2()
suma()
suma2(300, 99)


#Funcion dentro de una funcion
def funcion_compuesta(a, b):
  my_print()
  print(a / b)


funcion_compuesta(100, 50)
