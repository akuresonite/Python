# alphabet = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']
# a = 'ashish'
# x = [i for i in a]
# for i in range(0, len(a)):
#     if x[i] in alphabet:
#         print(x[i], alphabet[alphabet.index(x[i])+2])
# l = ['a', 's', 'k', 'm', ' ']
# a='ashish kumar'
# for i in range(0,len(a)):
#     if a[i] in l:
#         print(a[i],'-','True')
# l = ['a', 's', 'k', 'm', ' ']
# print(len(l))
# for i in range(0,len(l)):
#    print(i, l[i])
#a = ''
#msg = 'ashihs kumar,'
#for i in range(len(msg)):
#    a += msg[i]
#print(a)
# import sys

# print(round(2.7))

# student_scores = {
#     "Harry": 81,
#     "Ron": 78,
#     "Hermione": 99,
#     "Draco": 74,
#     "Neville": 62,
# }
# student_scores.update({"Sameer": 95})
# student_scores["Rajesh"] = 89
#
# print(student_scores.keys())
# print(student_scores.values())
# # print(student_scores.__len__())
# # print(max(student_scores.values()))
# # print(student_scores["Harry"])
# highestScore = 0
# # topper = ''
# for i in student_scores:
#     n = student_scores[i]
#     if n > highestScore:
#         highestScore = n
#         topper = i
# print(topper, highestScore)
#
# a = int(input(sys.argv[1]))
# # print(sys.argv[0])
# b = int(input(sys.argv[2]))
# c = a + b
# print(c)
# Python program to demonstrate
# sys.argv


# import sys
# print("This is the name of the program:", sys.argv[0]
# print("Argument List:", str(sys.argv))
# print(int(sys.argv[1]) + int(sys.argv[2]) + int(sys.argv[3]))
# a = int(input(f"Enter a: {sys.argv[1]}"))
# print(a)
# l = []
# for i in range(len(sys.argv)):
#     l.append(sys.argv[i])
# print(l)
#a = input("Enter: ")
#print("you have entered", a, a.lower(), a.capitalize(), a.title())

# Enter your code here. Read input from STDIN. Print output to STDOUT
a = int(input())
b = int(input())
m = int(input())
p1 = a**b
p2 = pow(a,b,m)
print(p1)
print(p2)