def factorisation(n):

    print(f"Prime factorization of {n}:")
    c = 2
    while (n > 1):

        if (n % c == 0):
            print(c, end =",")
            n //= c
        else: 
            c +=1

n = int(input("plz enter the number to find factorisation: "))
factorisation(n)