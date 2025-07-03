import sys


input = sys.stdin.readline

개수 = int(input())

가격 = []
for i in range(개수):
    a, b, c = list(map(int, input().strip().split(" ")))

    if a == b == c:
        가격.append(10000 + a * 1000)
    elif a == b or a == c or b == c:
        if b == c:
            가격.append(1000 + b * 100)
        else:
            가격.append(1000 + a * 100)

    else:
        가격.append(max(a, b, c) * 100)

print(max(가격))
