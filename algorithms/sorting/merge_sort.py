
def merge(q,r ):

    res = []
    i, j = 0, 0
    while i < len(q) and j < len(r):
        if q[i] < r[j]:
            res.append(q[i])
            i+=1
        else:
            res.append(r[j])
            j+=1
 
    res += q[i:]
    res += r[j:]
    return res
def merge_sort(A):
    
    if len(A) == 1:
        return A

    q = merge_sort(A[:len(A)/2])
    r = merge_sort(A[len(A)/2:])
    
    return merge(q,r)
    


    # if len(A) == 1:
    #     return A[0]
    # if len(A) == 2:
    #     if A[0] <= A[1]:
    #         return A[0], A[1]
    #     else:
    #         return A[1], A[0]
    
    # q = merge_sort(A[:len(A)/2])
    # r = merge_sort(A[len(A)/2:])
    # l = [i for i in q] + [i for i in r]
    # print(l)
    # return l

print(merge_sort([3,2,5,3,4]))