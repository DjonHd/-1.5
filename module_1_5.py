immutable_var = (1,2,'a','b')
print(immutable_var)
#immutable_var[0] = 50 не возможно заменить 1 на 50. 1 есть 1
#print(immutable_var)
print('Immutable var: '+ str(immutable_var))
mutable_list = [1,2,'a','b']
print(mutable_list)
mutable_list.append('Modified')
print('Mutable list: ' + str(mutable_list))



