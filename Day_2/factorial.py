n = int(input("enter number to calculate factorial: "))
counter = 1
factorial = 1

while counter <= n:
    factorial *= counter
    counter +=1

print(f"factorial of {n} is {factorial}")
