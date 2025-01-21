items = ["dog", "cat", "dog", "fish", "cat", "dog"]

search_item = input("Enter an item to search for: ")

count = 0

for item in items:
    if item == search_item:
        count += 1

print(f"'{search_item}' appears {count} times in the list.")
print(len(items))