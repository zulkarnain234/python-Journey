n = int(input("Enter the number to check of multiples of 3 & 5 in between: "))
sum = 0

for i in range(1, n+1):
    if i % 3 == 0 or i % 5 == 0:
        print(f"{i}")
        sum = sum + i

print(f"total is {sum}")