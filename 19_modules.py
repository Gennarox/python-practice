import sys

print(sys.path)

import re

text = "Mi numero de telefono es 981504471, tengo 23 años y mido 1 metro con 70"
result = re.findall('[0-9]+', text)
print(result)

import time

timestamp = time.time()
print(timestamp)  #formato ilegible
local = time.localtime()
result = time.asctime(local)
print(f'Hora formateada -> {result}')

import collections  #ojo, muy util, crea un diccionario con la distribucion de los elementos de una lista

numbers = [1, 1, 1, 1, 1, 3, 3, 3, 5, 6, 6, 5, 7, 8, 1, 10]
counter = collections.Counter(numbers)
print(counter)
