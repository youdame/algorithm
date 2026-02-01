import sys
from io import StringIO



input = sys.stdin.readline

A, B, C = map(int, input().split())

# A를 B번 곱한 수를 알고싶다

def recursive(A, B):
    if B == 1:
        return A**B
    if B % 2 == 0:
        result = recursive(A, B // 2)
        return (result * result) % C
    else:
        return (A * recursive(A, B-1)) % C

print(recursive(A,B) % C)


    