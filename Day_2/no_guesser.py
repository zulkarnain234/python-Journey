import random
n = int(input("Enter the no. for the range: "))

random_number = random.randint(1,n+1)
print("A random no. has been chosen") 


i = int(input("guess the number: "))
counter = 1

while i != random_number:
    if i < random_number:
        print("guess is too low")
    elif i > random_number : 
        print("guess is too high")

    i = int(input("guess the number: "))
    counter +=1

if counter == 1:
    print(f"Congratulations, You guessed the no. in {counter} time")
else:
    print(f"Congratulations, You guessed the no. in {counter} times")

print(f"{random_number}")

