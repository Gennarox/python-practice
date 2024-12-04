set_a = {'par', 'bra'}
set_b = {'arg', 'bol'}

#union
set_c = set_a.union(set_b) #metodo
print(set_c)
set_d = set_a | set_b #operador
print(set_d)

#intersection
set_a.add('arg')
set_c = set_a.intersection(set_b) #metodo
print(set_c)
set_d = set_a & set_b #operador
print(set_d)

#difference
set_a = {'par', 'bra', 'arg', 'bol', 'usa'}
set_c = set_a.difference(set_b) #metodo
print(set_c)
set_d = (set_a - set_b) #operador
print(set_d)

#symetric difference
set_a = {'par', 'bra', 'usa'}
set_b = {'arg', 'bol', 'usa'}

set_c = set_a.symmetric_difference(set_b) #metodo
print(set_c)
set_d = set_a ^ set_b #operador
print(set_d)

set_e = set_a.difference(set_b)
print(set_e)