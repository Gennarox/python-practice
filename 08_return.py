#return
def suma_return(a, b):
  result = 0
  for i in range(a, b):
    result += i

  return result  #ojo con la identacion del return
  #el return no imprime, devuelve el valor al programa para tratarlo o utilizarlo


def mult_same(a):
  number = (a * a)
  return number


resultado = suma_return(1, 100)
print("El resultado de la funcion fue -> ", resultado)
resultado2 = suma_return(resultado, mult_same(resultado))
print(resultado2)
