# FizzBuzz
n = int(input("Enter n: "))
for i in range(1, n+1):
    if i % 3 == 0 and i % 5 == 0:
        print("FizzBuzz")
    elif i % 3 == 0:
        print("Fizz")
    elif i % 5 == 0:
        print("Buzz")
    else:
        print(f"{i}")

# # # # ********************************************
# # # # ********************************************

# # # # PROGRAM FOR RANDOM LIST < SUM AND AVG >

# # # # ********************************************
# # # # # ********************************************
# # import random
# # nlist = [random.randint(1,50) for _ in range(10)] 
# # print(nlist)

# # total = 0

# # for i in nlist:
# #     total +=i
# #     avg = total/len(nlist)

# # print(total)
# # print(avg)
# # nlist[4] = 56

# # print(nlist)
# # # **************************************************
# # # **************************************************

# # # PROGRAM FOR FILTERING THE LIST

# # # ************************************************** 
# # # ************************************************** 

# import random

# nlist = [random.randint(1, 50)for _ in range (10)]
# print(nlist)

# print("Hello")

# filter_list = []

# for i in nlist:
#     if i > 20:
#         filter_list.append(i)

# print(filter_list)
