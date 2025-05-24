import sys

input = sys.stdin.readline


def solution(i, target):
    n = i
    while i:
        n += i % 10
        i = i // 10
    return target == n


target = int(input())
flag = False
for i in range(target):
    if solution(i, target):
        print(i)
        flag = True
        break
if not flag:
    print(0)

# N = int(input())

# for i in range(1, N):  # 1부터 N-1까지 모든 수 검사
#     합 = i + sum(int(d) for d in str(i))  # 분해합 = 자기 자신 + 자리수 합
#     if 합 == N:
#         print(i)  # 생성자 출력
#         break
# else:
#     print(0)  # 생성자 없음


# for i in range(1, target):
#     합 = i + sum(int(d) for d in str(i))
#     if 합 == target:
#         print(i)
#         break
#     else:
#         print(0)
