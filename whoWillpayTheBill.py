import random
#  ashish,kumar,uchadiya,sameer,nandmehar,preity,mishra,rajesh,kumar,yadav
print("Give me everybody's names seperated by comma.")

names = input(' ').split(',')

# n = random.randint(0, len(names)-1)

# n = random.choice(names)

print(f"{random.choice(names)} is going to buy the meal today!")