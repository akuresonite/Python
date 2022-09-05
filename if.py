l1 = ['ashish', 'kumar', 'uchadiya', 14, 5, 'august', 1999, 'morena', 476001,
      'mp',
      22082028, 9784916529, 9354931641,
      'iitbhu']
p = 1
for item in l1:
    # if (type(item) is int) and (item > 6): #methode 1
    if str(item).isnumeric() and item > 6:  #method 2
        print(p, item)
        p += 1
