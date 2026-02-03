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
        if not path or (path and path[-1] < x):
            if x not in path:
                path.append(x)
                dfs()
                path.pop()
            
dfs()