import sys
input = sys.stdin.readline

N = int(input())

count = 0

# 열 사용 여부
col_used = [False] * N

# ↘ 대각선 (row + col)
diag1 = [False] * (2 * N)

# ↙ 대각선 (row - col + N)
diag2 = [False] * (2 * N)


def dfs(row):
    global count

    if row == N:
        count += 1
        return

    for col in range(N):

        # 열 / 대각선 충돌 검사
        if col_used[col] or diag1[row + col] or diag2[row - col + N]:
            continue

        # 퀸 배치
        col_used[col] = True
        diag1[row + col] = True
        diag2[row - col + N] = True

        dfs(row + 1)

        # 백트래킹
        col_used[col] = False
        diag1[row + col] = False
        diag2[row - col + N] = False


dfs(0)

print(count)