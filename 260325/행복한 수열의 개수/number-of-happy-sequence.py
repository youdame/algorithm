N, M = map(int, input().split())
grid = [list(map(int, input().split())) for _ in range(N)]
"""
어떤 숫자든 상관없고 연속해서 M개의 숫자가 나와야함 
행으로 쭉 보고, 열로 쭉 보기


"""

def is_happy(seq):
    count = 1
    max_count = 1
    for i in range(1, N):
        if seq[i] == seq[i-1]:
            count += 1
        else:
            count = 1
        max_count = max(count, max_count)
    return max_count >= M

answer = 0

for row in grid:
    answer += is_happy(row)

for i in range(N):
    col = [row[i] for row in grid]
    answer += is_happy(col)

print(answer)