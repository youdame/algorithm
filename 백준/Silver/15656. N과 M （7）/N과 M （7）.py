import sys 
from io import StringIO



input = sys.stdin.readline

N, M = map(int, input().split())
arr = sorted(list(map(int, input().split())))

path = []
def dfs():
    if len(path) == M:
        print(*path)
        return
    for x in arr:
        path.append(x)
        dfs()
        path.pop()
        
dfs()