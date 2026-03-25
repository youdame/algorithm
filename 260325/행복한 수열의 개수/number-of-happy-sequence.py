N, M = map(int, input().split())
grid = [list(map(int, input().split())) for _ in range(N)]
"""
어떤 숫자든 상관없고 연속해서 M개의 숫자가 나와야함 
행으로 쭉 보고, 열로 쭉 보기


"""
answer = 0
for row in grid:
    count = 1
    for i in range(N-1):
        if row[i] == row[i+1]:
            count += 1
        else:
            count = 1
    if count >= M :
        answer += 1 

"""
(0, 0)   (0, 1)
(n-1, 0) (n-1, 1)
"""

for i in range(N):
    col = []
    for j in range(N):
        col.append(grid[j][i])
    count = 1
    for k in range(N-1):
        if col[k] == col[k+1]:
            count += 1

        else:
            count = 1
    if count >= M :
        answer += 1 

print(answer)