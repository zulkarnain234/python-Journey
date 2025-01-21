# import random

# elements = int(input("how many items would you like to add? : "))

# list = []

# for _ in range (elements):
#     num = random.randint(1,100)
#     list.append(num)

# print(list)
# reversed_list = list [:: -1]

# print(reversed_list)

import random

elements = int(input("how many items would you like to add? : "))

list = []

for _ in range (elements):
    num = random.randint(1,100)
    list.append(num)    

print(list)

n = elements


for i in range(n//2):
    list[i], list[n-1-i] = list[n-1-i], list[i]

print(list)

