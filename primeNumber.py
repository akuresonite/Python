def isPrime(n):
    for i in range(2, n):
        if n % i == 0:
            #  is_prime = True
            print('Not a Prime')
            exit()
    print('Prime')
n = int(input('Check this number: '))
isPrime(n)