print("Input the list of student heights,")
stuHeights = input(": ").split(',')
# print(stuHeights)
totalHeight = 0
count = 0
for height in stuHeights:
    # totalHeight = totalHeight + int(stuHeights[int(i) - 1])
    totalHeight = totalHeight + int(height)
    count += 1
print(f"Average height of students is {totalHeight / count}")
print(max(stuHeights))

#  1 2 3 4
#  0 1 2 3
#  23,2343,32,978,343,52423,2344