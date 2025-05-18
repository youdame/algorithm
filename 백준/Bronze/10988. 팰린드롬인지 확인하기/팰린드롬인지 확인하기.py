import sys


input = sys.stdin.readline

is_pel = True
인풋 = input().strip()
for i in range(len(인풋) // 2):
    # print(i, len(인풋) - i - 1)
    if 인풋[i] != 인풋[len(인풋) - i - 1]:
        is_pel = False
print(1 if is_pel else 0)
