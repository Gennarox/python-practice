for i in range(1,11):
  print(i)

my_iterable = iter(range(1,3))
print(my_iterable) #referencia en memoria, no crea un array entero en memoria si no que lo va generando de la sgte manera:

print(next(my_iterable))
print(next(my_iterable))
print(next(my_iterable)) #StopIteration

#El iterable es util en manejo de archivos, es un ciclo for "manual"