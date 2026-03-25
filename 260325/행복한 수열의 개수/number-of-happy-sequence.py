N, M = map(int, input().split())
grid = [list(map(int, input().split())) for _ in range(N)]
"""
어떤 숫자든 상관없고 연속해서 M개의 숫자가 나와야함 
행으로 쭉 보고, 열로 쭉 보기

(0, 0)   (0, 1)
(n-1, 0) (n-1, 1)
"""
answer = 0
for row in grid:
    count = 0
    for i in range(0, N-1):
        # 연속해서 count만큼의 숫자가 나오는지 확인하는 법,,,, 
        # 새로운 숫자가 나오면 갱신 
        if row[i] == row[i+1]:
            count += 1
        else:
            count = 0
        if count == M:
            answer += 1 
            break
    print(count)
    print(answer)

for i in range(N):
    col = []
    for j in range(N):
        col.append(grid[j][i])
    print(col)