def zero_matrix(matrix, ):

    m = len(matrix)
    n = len(matrix[0])
    new_matrix = []
    to_zero = []
    for i, row in enumerate(matrix):
        for j, col in enumerate(row):
            if col == 0:
                to_zero.append((i, j))
    print(to_zero)
    for i, j in to_zero:
        matrix[i] = [0 for _ in range(n)]
        
        for row in range(m):
            matrix[row][j] = 0
    return matrix


mm  = [
            [1, 2, 3, 4, 0],
            [6, 0, 8, 9, 10],
            [11, 12, 13, 14, 15],
            [16, 0, 18, 19, 20],
            [21, 22, 23, 24, 25]
        ]


