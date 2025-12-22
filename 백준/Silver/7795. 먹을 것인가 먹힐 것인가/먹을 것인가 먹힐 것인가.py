import sys


input = sys.stdin.readline

T = int(input())

count = 1
while count <= T:
    N, M = list(map(int, input().strip().split(" ")))
    count += 1
    answer = 0
    A = sorted(list(map(int, input().strip().split(" "))))
    B = sorted(list(map(int, input().strip().split(" "))))
    # print(A, B)
    A_point = 0
    B_point = 0
    while A_point < N:
        if B_point == M:
            answer += M
            A_point += 1
        else:
            if A[A_point] > B[B_point]:
                B_point += 1
            else:
                A_point += 1
                answer += B_point

    print(answer)
