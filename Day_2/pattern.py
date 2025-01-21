N = int(input("Enter a positive integer: "))

for row in range(1, N + 1):
    for num in range(1, row + 1):
        print(num, end=" ")
    print()
