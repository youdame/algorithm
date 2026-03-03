import sys 
from io import StringIO


input = sys.stdin.readline 


N = int(input())

arr = []
for _ in range(N):
    arr.append(list(map(int, input().split())))


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

white = 0
blue = 0

def compress(x, y, size):
    global white, blue
    if isSame(x, y, size):
        if arr[x][y] == 1:
            blue += 1
        else: 
            white += 1
        return arr[x][y]
    else:
        half = size // 2
        compress(x, y, half)
        compress(x, y+half, half)
        compress(x+half, y, half)
        compress(x+half, y+half, half)
        
compress(0, 0, N)
print(white)
print(blue)