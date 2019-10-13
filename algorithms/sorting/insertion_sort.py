

def insertion_sort(unsorted_list):
    unsorted_list_len = len(unsorted_list)

    for j in range(1, unsorted_list_len):
        next_elm = unsorted_list[j]

        i = j - 1  
        
        while i >= 0 and unsorted_list[i] > next_elm:
            unsorted_list[i+1] = unsorted_list[i]
            i = i - 1
        unsorted_list[i+1] = next_elm

    return unsorted_list
a = [10,1,1,1,1,111,7,5, 2, 4, 6, 1, 3]

print(insertion_sort(a))