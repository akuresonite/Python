print("Input the list of student scores,")
studentScores = input(": ").split(",")
scoreInt = []
for i in studentScores:
    scoreInt.append(int(i))
print(f"The highest score in the class is: {max(scoreInt)}")
#  12,13,5353,12323,3534,2
