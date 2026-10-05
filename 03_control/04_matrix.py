matrix = [
    [1, 2, 3],
    [4, 5, 6],
    [7, 8, 9],
]


for row in matrix:
    for item in row:
        print(item)

print(matrix[0][2])

# new_matrix = [
#     [0, 1, 2],
#     [0, 1, 2],
#     [0, 1, 2],
# ]

matrix = []

for i in range(3):
    row = []
    for j in range(3):
        # [0, 1, 2]
        row.append(j)
    # [[0, 1, 2]]
    # [[0, 1, 2], [0, 1, 2]]
    # [[0, 1, 2], [0, 1, 2], [0, 1, 2]]
    matrix.append(row)

print(matrix)
