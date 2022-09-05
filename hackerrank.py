def pn(n):
    s = ''
    a = ''
    for i in range(1,n):
        s += f"{i}"
    a = s
    a += f"{n}"
    a += s[::-1]
    return a
N = int(input())
#for i in range(1,N+1):
i = 1
while i != N+1:
    print(pn(i))
    i += 1
    