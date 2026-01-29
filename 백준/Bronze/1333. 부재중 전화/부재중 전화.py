import sys
from io import StringIO



input = sys.stdin.readline


N, L, D = map(int, input().split())

time = 0
album_end = N * L + (N-1) * 5

while True:    
    if time >= album_end:
        break
    if time % (L + 5) >= L:
        break
    time += D
    
print(time)