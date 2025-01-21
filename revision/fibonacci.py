# Enter a number and have the program generate the Fibonacci sequence to that number or to the Nth number.
def fibonacci(n):
            if n <= 0:
                print("wrong selection")
                return
            i , j = 0, 1
            print("Fibonacci Sequence: ")
            for _ in range (n):
                print (i, end=", ")
                i, j = j, i + j

n = int(input("Enter a last number for fibonacci: "))
fibonacci(n)

