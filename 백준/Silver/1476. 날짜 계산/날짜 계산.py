import sys
from io import StringIO



input = sys.stdin.readline

E, S, M = map(int, input().split())


count = 0

while True:
    e = count % 15 + 1
    s = count % 28 + 1
    m = count % 19 + 1
    
    if e == E and s == S and m == M :
        print(count + 1)
        break
    
    count += 1 
