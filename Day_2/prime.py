N = int(input("Enter a positive integer: "))

if N < 2:
    print(" is not a prime no.")
else: 
    is_prime = True
    for i in range(2, N):
        if N % i == 0:
            is_prime = False
            break
if is_prime:
    print(f"{N} is a prime no.")
else:
    print(f"{N} is not a prime no.")