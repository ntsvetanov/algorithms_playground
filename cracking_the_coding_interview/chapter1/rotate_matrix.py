def rotate_matrix(matrix, N):

    aa = []
    for i in matrix[::-1]:
        aa.append(i)
    
    return [[i[m] for i in aa] for m in range(N)]
    

mm  = [ 
    [1,2,3],
    [4,5,6],
    [7,8,9]
]

