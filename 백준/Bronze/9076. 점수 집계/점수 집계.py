import sys

input = sys.stdin.readline

배열 = []
for i in range(int(input())):
    배열 = sorted(map(int, input().strip().split(" ")))

    if 배열[3] - 배열[1] >= 4:
        print("KIN")
        continue
    배열.remove(배열[0])
    배열.remove(배열[-1])
    print(sum(배열))
