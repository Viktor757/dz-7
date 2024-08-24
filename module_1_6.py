my_dict={'Петя':2000, 'Вася':1965, 'Иван':2010}
print(my_dict)
print(my_dict['Иван'])
my_dict['Игорь']=1986
print(my_dict.get('Маруся'))
my_dict.update({'Маша':1990, 'Даша': 1976})
a = my_dict.pop('Петя')
print(a)
print(my_dict)
my_set={1,4,1,4,4,'множество',1,5,2,2,3,3,6,6,7,False}
print(my_set)
my_set.add(('Hello',8))
my_set.remove(3)
print(my_set)