print("Input the list of student scores,")
studentScores = input(": ").split(",")
for i in range(0, len(studentScores)):
    studentScores[i] = int(studentScores[i])
print(f"The highest score in the class is: {max(studentScores)}")
#  12,13,5353,12323,3534,2
