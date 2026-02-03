import sys 
from io import StringIO


input = sys.stdin.readline

N, M = map(int, input().split())
arr = sorted(list(map(int, input().split())))

path = []
visited = [False] * N
def dfs():
    if len(path) == M:
        print(*path)
        return
    prev = None
    for index in range((N)):
        if prev == arr[index]:
            continue
        
        if not visited[index] and (not path or (path and path[-1] <= arr[index])):
            path.append(arr[index])
            prev = arr[index]
            visited[index] = True
            dfs()
            path.pop()
            visited[index] = False
        
dfs()