def primed_and_ready():
    for i in range(3,101,1):
        isPrime = True
        for j in range(2,i//2):
            if (i % j == 0):
                isPrime = False
        if (isPrime):
            print(i)

primed_and_ready()
