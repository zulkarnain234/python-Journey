items = ["apple", "banana", "apple", "orange", "banana", "apple", "kiwi", "watermelon", "apple", "grapes", "kiwi"]
search_item = str(input("Enter the name if fruit you want to count occurence: "))

# count = items.count(search_item)

# print(items.count)
# print(f"'{search_item}' appear {count} times")

count = 0

for item in items:
    if item == search_item:
        count +=1

print(f"'{search_item}' appears {count} times")