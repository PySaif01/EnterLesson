my_dict = {'Николай':1990, 'Станислав':1991, 'Евгений': 1987}
print(my_dict)
print(my_dict['Станислав'])
print(my_dict.get('Владимир'))
my_dict.update({'Мария': 1995, 'Анна': 1988})
d = my_dict.pop('Николай')
print(d)
print(my_dict)

my_set = {22,30,30,21,22,24,26,30,22,21,44,50,22,24,34,26,
          (1,2,3),(9,2,5),(1,2,3),(1,2,3),
          True,True,True,False,
          'Zhenya', 'Masha', 'Anna', 'Zhenya', 'Anna'}
print(my_set)
my_set.add(51)
my_set.add('Stas')
my_set.discard(True)
print(my_set)