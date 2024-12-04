numbers = [1, 2, 3]
transform_numbers = []

for x in numbers:
  transform_numbers.append(x * 2)

print(transform_numbers)

print(list(map(lambda x: x * 2, numbers)))

#operaciones con dos listas
numbers_1 = [1, 3, 5]
numbers_2 = [2, 4, 6]

new_list = list(map(lambda x, y: x * y, numbers_1, numbers_2))
print(new_list)