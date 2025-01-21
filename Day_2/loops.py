n = int(input("enter no. for the range: " ))

for i in range(n+1):
    if i % 3 ==0:
        if i % 5 == 0:
            print(f"fizzbuzz {i}")
        else : 
            print(f"fizz {i}")
    elif i % 5 ==0:
        print(f"buzz {i}")      
    
    