def reduce(y):
  return round(y / 2)


def hof_function(x, func):
  return f"El valor del hof v1 es {x * func(x)}"


print(hof_function(21, reduce))

#version lambda
reduce_v2 = lambda y: round(y / 2)
print(type(reduce_v2))
hof_function_v2 = lambda x, func: f"El valor del hof v2 es {x*func(x)}"

print(hof_function_v2(21, reduce_v2))
