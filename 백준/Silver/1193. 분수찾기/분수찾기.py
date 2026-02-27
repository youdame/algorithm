import sys
from io import StringIO

N = int(input())



line = 1

while N > line:
    N -= line
    line += 1
    
c = line + 1


if line % 2 != 0:
    print(f"{c-N}/{N}")
else: 
    print(f"{N}/{c-N}")

