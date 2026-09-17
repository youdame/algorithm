import sys

# sys.stdin = open("input.txt", "r")


input = sys.stdin.readline



n = int(input())


record = dict()
for _ in range(n*n):
    student_list = list(map(int, input().split()))
    record[student_list[0]] = set(student_list[1:])
# print(record)

"""

주변에 좋아하는 친구가 가장 많은 위치에 앉아야함
"""
grid = [[0] * n for _ in range(n)]

def 배치하기(key):
    candidate = []
    for y in range(n):
        for x in range(n):
            # 해당 좌표
            if grid[y][x] == 0:
                # 주변에 내가 좋아하는 친구가 몇 명인지
                like_count = 0
                # 주변에 빈칸이 몇 개인지
                zero_count = 0
                for dy, dx in [(-1, 0), (1, 0), (0, 1), (0, -1)]:
                    ny = dy + y
                    nx = dx + x
                    if 0 <= ny < n and 0 <= nx < n :
                        if grid[ny][nx] == 0:
                            # print(y, x , ny,nx)
                            zero_count += 1
                        if grid[ny][nx] in record[key]:
                            like_count += 1



                candidate.append((like_count, zero_count, y, x))
    candidate.sort(key= lambda x : (-x[0], -x[1], x[2], x[3]))
    _, _, r, c = candidate[0]

    grid[r][c] = key

def 점수계산하기():
    score = [0, 1, 10, 100, 1000]

    answer = 0
    for y in range(n):
        for x in range(n):
            like_count = 0
            for dy, dx in [(-1, 0), (1, 0), (0, 1), (0, -1)]:
                ny = dy + y
                nx = dx + x
                if 0 <= ny < n and 0 <= nx < n:
                    if grid[ny][nx] in record[grid[y][x]]:
                        like_count += 1
            answer += score[like_count]
            # print(score[like_count])

    return answer
for key in record.keys():
    배치하기(key)
# print(grid)
print(점수계산하기())