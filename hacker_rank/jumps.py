# Enter your code here. Read input from STDIN. Print output to STDOUT
# https://www.hackerrank.com/challenges/jumping-on-the-clouds/submissions/code/125966621?h_l=interview&playlist_slugs%5B%5D=interview-preparation-kit&playlist_slugs%5B%5D=warmup
def jumps(arr, n):
    
    allowed_positions =  [i for i, v in enumerate(arr) if v != 1]

    count = 1
    i = 0
    while i < len(allowed_positions) - 2:
        
        if allowed_positions[i] + 2 == allowed_positions[i + 2]:
            i += 2
        else:
            i += 1

        count += 1    
    if allowed_positions[len(allowed_positions) - 2] == allowed_positions[len(allowed_positions) -1]:
        count -= 1
    return count

if __name__ == "__main__":
    n = input()
    arr = []    
    for i in input().split(): 
        element = int(i) 
        arr.append(element)

    print(jumps(arr, n))