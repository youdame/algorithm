import sys
from io import StringIO


input = sys.stdin.readline

N = int(input())
M = int(input())
buttons = list(map(str, list(set([0, 1, 2, 3, 4, 5, 6, 7, 8, 9]) - set((map(int, input().split()))))))



compare_100 = abs(N - 100)

available_number = []
for num in range(1000000):
    available = True
    for number in list(str(num)):
        if number not in buttons:
            available = False
            break
    if not available:
        continue
    else:
        available_number.append(num)

min_answer = 1e9
for number in available_number:
    answer = len(str(number)) + abs(number - N)
    min_answer = min(answer, min_answer)
min_answer = min(min_answer, compare_100)
print(min_answer)