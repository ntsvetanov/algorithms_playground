# Enter your code here. Read input from STDIN. Print output to STDOUT

def get_pair(arr, n):
    colors = {}
    pairs_count = 0
    for i in arr:
        if i in colors.keys():
            colors[i] += 1
            
        else:
            colors[i] = 1

        if colors[i] % 2 == 0:
            pairs_count += 1
    return pairs_count

if __name__ == "__main__":
    n = input()
    arr = []    
    for i in input().split(): 
        element = int(i) 
        arr.append(element)

    print(get_pair(arr, n))