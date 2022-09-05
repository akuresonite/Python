print('Method 1:')
a = input('a: ')
b = input('b: ')
t = a
a = b
b = t
print('a = ', a)
print('b = ', b)
print('Method 1:')
(a,b) = (b,a)
print('a = ', a)
print('b = ', b)


