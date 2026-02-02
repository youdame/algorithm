import sys
from io import StringIO



input = sys.stdin.readline

N, M = map(int, input().split())

path = []

def dfs():
    if len(path) == M : 
        print(*path)
        return
    for x in range(1, N + 1):
        if not path or path[-1] <= x:
            path.append(x)   # 선택
            dfs()
            path.pop()       # 선택 취소 (되돌아감)
        

dfs()