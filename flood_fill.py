import random 

matrix  = [
    [1,1,1,1],
    [0,1,0,1],
    [1,0,1,0]
]


def get_indices(row:int, col:int, matrix:list) -> list:
    max_row = len(matrix) - 1
    max_col = len(matrix[0]) - 1
    l = []
    if (row - 1) >= 0 :
        l.append([row-1, col])
    if (row + 1) <= max_row:
        l.append([row+1, col])
    if (col - 1) >= 0:
        l.append([row, col-1])
    if (col + 1) <= max_col:
        l.append([row, col+1])
    return l

def flood_fill(indices:list, matrix:list) -> list:
    for index in indices:
        if matrix[index[0]][index[1]] == 1:
            matrix[index[0]][index[1]] = 2
            indices = get_indices(index[0], index[1], matrix)
            matrix = flood_fill(indices, matrix)
    else:
        return matrix

def generate_matrix(n, m):
    l = []
    for rows in range(m):
        row = []
        for col in range(n):
            row.append(random.randrange(0,2))
        l.append(row)
    return l



for i in range(100):
    matrix = generate_matrix(3,3)
    ans = flood_fill([[1,1]], matrix)
    for i in ans:
        print(*i)
    print("\n")