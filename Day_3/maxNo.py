import random

elements = int(input("how many items would you like to add? : "))

list = []

for _ in range(elements):
    num = random.randint(1,100)
    list.append(num)

print(list)

max = list[0]

for num in list:
    if num > max:
        max = num

print(f"max no. is {max}")