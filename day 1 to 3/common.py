list1 = ['40', '50', '60','80', '90']
list2 = ['45','50','56','60', '90','40']

common_elements = []

for item in list1:
    if item in list2 and item not in common_elements:
        common_elements.append(item)

print(f"{common_elements}")