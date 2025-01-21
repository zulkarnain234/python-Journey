import random

def Game():
    number = random.randint(1,50)
    attempt = 0

    print("guess the Number between 1 to 50")

    while True:
        guess = int(input("Enter your guess: "))
        attempt +=1

        if guess < number:
            print("it's too low")
        elif guess > number:
            print("guess is too high")
        else:
            print("Congratulations, that's the right number.")
            break
        
    print(f"You guessed it in {attempt} tries ")

Game()