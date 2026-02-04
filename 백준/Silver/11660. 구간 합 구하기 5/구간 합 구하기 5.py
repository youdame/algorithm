import sys 
from io import StringIO


input = sys.stdin.readline

N, M = list(map(int, input().split()))

arr = [list(map(int, input().split())) for _ in range(N)]

psum = [[0] * N for _ in range(N)]


for i in range(N):
    for j in range(N):
        if i > 0:
            psum[i][j] += psum[i-1][j]
        if j > 0 and i > 0:
            psum[i][j] -= psum[i-1][j-1]
        if j > 0:
            psum[i][j] += psum[i][j-1] 
        psum[i][j] += arr[i][j]

for _ in range(M):
    x1, y1, x2, y2 = list(map(int, input().split()))
    x1 -= 1
    y1 -= 1
    x2 -= 1
    y2 -= 1
    answer = psum[x2][y2]
    if x1 > 0:
        answer -= psum[x1-1][y2]
    if y1 > 0:
        answer -= psum[x2][y1-1]
    if x1 > 0 and y1 >0 :
        answer +=  psum[x1-1][y1-1]
    print(answer)




