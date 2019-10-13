    #!/bin/python3

    import math
    import os
    import random
    import re
    import sys

    # Complete the countingValleys function below.
    def countingValleys(n, s):
        count = 0
        valleys = 0
        is_up = False
        for i in s:
            if i == "U":
                count += 1
                is_up = True
            elif i == "D":
                count -= 1
                is_up = False
            if count == 0 and is_up:
                valleys += 1
        return valleys
    if __name__ == '__main__':
        fptr = open(os.environ['OUTPUT_PATH'], 'w')

        n = int(input())

        s = input()

        result = countingValleys(n, s)

        fptr.write(str(result) + '\n')

        fptr.close()
