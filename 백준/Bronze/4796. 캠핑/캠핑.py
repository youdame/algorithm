import sys
from io import StringIO

count = 1
while True:
    
    L, P, V = map(int , input().split())
    if L == P == V == 0:
        break

    몫 = (V // P)
    나머지 = min(L, V - 몫 * P)
    print(f"Case {count}: {몫 * L + 나머지}")
    count += 1