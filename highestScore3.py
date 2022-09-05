print("Input the list of student scores,")
studentScores = input(": ").split(",")
for i in range(0, len(studentScores)):
    studentScores[i] = int(studentScores[i])

for y in range(0, len(studentScores) - 1):
    for x in range(0, len(studentScores) - 1):
        if studentScores[x] > studentScores[x + 1]:
            (studentScores[x + 1], studentScores[x]) = (studentScores[x], studentScores[x + 1])
print(f"The highest score in the class is: {studentScores[len(studentScores)-1]}")
#  print(f"The highest score in the class is: {max(studentScores)}")
#  12,13,5353,12323,3534,2
