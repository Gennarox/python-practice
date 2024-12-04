def find_volume(length, width, depth):
  return length + width + depth

#find_volume() #requiere argumentos, a no ser...

#Si definimos valores por defecto
def find_volume2(length=1, width=1, depth=1):
  return length + width + depth

print(f"El resultado es -> {find_volume(1, 2, 3)}.")

#Tambien es posible enviar solo un parametro y dejar los demas por defecto
print(f"El resultado 2 es -> {find_volume2(depth=50)}.")

def find_volume_list(length=1, width=1, depth=1):
  return length*width*depth,length+width+depth,length-width-depth, length/width/depth

print(find_volume_list(20,50,70))
