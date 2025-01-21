matrix = [
    [1,2,3], 
    [4,5,6],
    [7,8,9]
]

transpose = []

for i in range(len(matrix[0])):
    row = [] 
    for nrow in matrix:
        row.append(nrow[i])
    transpose.append(row)

for nrow in transpose:
    print(nrow)
