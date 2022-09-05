d1 = {
    'name' : "ashish",
    'program' : "M. Tech",
    'department' : "Electrical Engineeing",
    'year' : "1st",
    'specilisation' : "Control Systems",
    'institute' : "IIT (BHU)"
}
#print('Student Details\nEnter keyword to search:',end=' ')
key1 = input('Student Details\nEnter keyword to search viz. name, program, department, year,specilisation, institute: ')
if key1 in d1:
    print(d1[key1])
else:
    print('Keyword not found!')