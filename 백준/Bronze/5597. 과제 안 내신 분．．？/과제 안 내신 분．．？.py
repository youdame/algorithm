import sys

input = sys.stdin.readline

빈도 = [0] * 31
for i in range(28):
    빈도[int(input())] += 1
for element in [i for i in range(len(빈도)) if 빈도[i] == 0]:
    if element != 0:
        print(element)
