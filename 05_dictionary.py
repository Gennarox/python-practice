dict = {}
for i in range(1,11):
  dict[i] = i*2

print(dict)

#con dictionary comprehension

dict_v2 = {i:i*2 for i in range(1,5)}
print(dict_v2)

#ejercicio sin comprehension
import random

countries = ["col","mex","bol","pe"]
population = {}
for country in countries:
  population[country]  = random.randint(1,100)

print(population) 

#con comprehension
poppulation_v2 = {country:random.randint(1,100) for country in countries}
print(population)

print("*"*20)
names = ["Ivan", "Violeta", "Dylan"]
ages = [12,25,30]

print(list(zip(names,ages)))

persons = {name:age for (name,age) in zip(names,ages)}
print(persons)
