import sys
from io import StringIO

input = sys.stdin.readline
input_str = input().strip()
bomb_str = input().strip()


result = []
for alphabet in input_str:
    result.append(alphabet)
    if list(bomb_str) == result[-len(bomb_str) :]:
        for i in range(len(bomb_str)):
            result.pop()
print("".join(result) if result else "FRULA")
