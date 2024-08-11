immutable_var = 1, True, 'tool'
print(immutable_var)
#immutable_var[0] = 3
#print(immutable_var)
#TypeError: 'tuple' object does not support item assignment
#потому что кортеж это неизменяемый тип данных

mutable_list = ['tools','staf','objects']
mutable_list[2] = 'personal'
mutable_list[0] = True
mutable_list[1] = 4
print(mutable_list)