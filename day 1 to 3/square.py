list = []

n = int(input("Enter the range: "))

for i in range(1, n+1):
    list.append(i**2)

print(f"{list},\n {len(list)}")