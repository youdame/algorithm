import sys
from io import StringIO


input = sys.stdin.readline
N, M = map(int, input().split())




set_record = set(input().strip() for _ in range(N))

count = 0

for _ in range(M):
    if input().strip() in set_record:
        count += 1
print(count)


        
