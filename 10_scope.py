price = 100 #global

def increment_global():
  return price

def increment_local():
  price = 200 #local
  result_local_context = ["Esto", "es", "prueba"]
  price = price * 2 #al ser declarada esta var dentro de la def ya es considerada local y Python entiende que se esta price local se refiere a price local, se crea un bucle y da error porque el contexto de esta variable es diferente a la global (por mas de que se llamen igual)
  return price


print("Var global -> ",price)
print(increment_global())
print(increment_local())

prunt(result_local_context) #da error, no esta dentro del mismo contexto, es local de la funcion increment_local