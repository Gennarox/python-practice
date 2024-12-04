import functools

numbers = [1,2,3,4,5]

list = list(functools.reduce(lambda item,counter:item+counter,numbers))

#desglose en funcion def

def accum(item,counter):
  print("item -> ", item)
  print("counter -> ", counter)

  return item+counter

