movie = ["3 idiots", "Chak de India", "the martian", "inception"]
movie.append("one piece")
movie.insert(1,"interstellar")
print(len(movie))
print(movie)


# Creating a list of fruits
fruits = ["apple", "banana", "cherry", "orange"]
# print(fruits)  # Output: ['apple', 'banana', 'cherry', 'orange']


last_fruit = fruits.pop()  # Removes and returns the last element ('grape')
print(last_fruit)
print(fruits)  # Output: ['apple', 'blueberry', 'cherry', 'orange']
