import sys 
from io import StringIO


input = sys.stdin.readline 
N = int(input())

arr = []
for _ in range(N):
    arr.append(list(map(int, list(input().strip()))))


def isSame(x, y, size):
    is_same = True
    start_node = arr[x][y]
    for i in range(x, x+size):
        for j in range(y, y+size):
            if arr[i][j] != start_node:
                is_same = False
                break
        if not is_same:
            break
    return is_same

def compress(x, y, size):
    if isSame(x, y, size):
        return str(arr[x][y])
    else:
        half = size // 2
        왼위 = compress(x, y, half)
        오위 = compress(x, y+half, half)
        왼아래 = compress(x+half, y, half)
        오아래 = compress(x+half, y+half, half)
        return "(" + 왼위 + 오위 + 왼아래 + 오아래 +")"
        
print(compress(0, 0, N))