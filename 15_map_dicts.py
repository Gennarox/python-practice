items = [{'item': 'pantalon', 'price': 100}, {'item': 'camisa', 'price': 200}]

#print(list(map(lambda x:x['price'],items)))
#print(list(map(lambda x:x['item'],items)))

prices = list(map(lambda x: x['price'],items))  #map no modifica el array original "items"
print(f'Nueva lista -> {prices}')
print(f'El array original sin modificacion por map y lambda -> {items}')


#Operacion con diccionario
def add_taxes(item):
  item['taxes'] = item['price'] * .1
  return item


new_items = list(map(add_taxes, items))
print(f'Nuevo array -> {new_items}')
print(f'El array original modificado por tema en memoria -> {items}')
