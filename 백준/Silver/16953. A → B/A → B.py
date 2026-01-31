import sys
from io import StringIO



input = sys.stdin.readline

A, B = map(int, input().split())



count = 1

possible =True
while A != B:
    if str(B)[-1] == "1":
        B = int(str(B)[:len(str(B))-1]) 

    elif B % 2 == 0: 
        B = B // 2
    else: 
        possible = False
        break
    if B < A:
        possible = False
        break

    count += 1

    
print(count if possible else -1)