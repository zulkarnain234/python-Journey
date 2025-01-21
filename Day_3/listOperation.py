elements = int(input("how many items would you like to add? : "))

list = []

for _ in range(elements):
    num = int(input("Enter a number: "))
    list.append(num)

print(f"The list is: {list}")

total = 0

for i in list:
    total +=i

print(f"{total}")