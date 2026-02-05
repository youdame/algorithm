import sys 
from io import StringIO

input = sys.stdin.readline

N, M = map(int, input().split())
not_mix = [[] for _ in range(N+1)]
for _ in range(M):
    A, B = map(int, input().split())
    not_mix[A].append(B)
    not_mix[B].append(A)
path = []

answer = 0
def dfs():
    if len(path) == 3:
        return 1

    count = 0 
    for x in list(range(1, N+1)):
        if not path : 
            path.append(x)
            count += dfs()
            path.pop()
        elif path and path[-1] < x and all (x not in not_mix[element] for element in path):
                    path.append(x)
                    count += dfs()
                    path.pop()
    return count
answer += dfs()
print(answer)