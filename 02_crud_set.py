set_countries = {'par', 'arg', 'bra', 'uru'}

size = len(set_countries)
print(size)

print('par' in set_countries)
print('bol' in set_countries)

#add
#set_countries.add('per', 'bol')
set_countries.add('per')
set_countries.add('per')
set_countries.add('bol')
print(set_countries)

#uptade
set_countries.update({'ecu','col','mex','per'})
print(set_countries)

#remove
set_countries.remove('col')
set_countries.remove('mex')
#set_countries.remove('usa') #error not find

#discard
set_countries.discard('usa') #no arroja error, al contrario de remove
print(set_countries)

#clear
set_countries.clear()
print(set_countries)
print(len(set_countries))