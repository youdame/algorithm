import sys
from io import StringIO


input = sys.stdin.readline


for line in sys.stdin:
    A, B = line.strip().split()
    a_point = 0
    b_point = 0
    # print(A, B)
    while b_point < len(B) and a_point < len(A):
        if A[a_point] == B[b_point]:
            a_point += 1

        b_point += 1

    if a_point == len(A):
        print("Yes")
    else:
        print("No")
