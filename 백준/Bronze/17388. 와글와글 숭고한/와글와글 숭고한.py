import sys
input = sys.stdin.readline

a, b, c = map(int, input().split(" "))


if a + b + c >= 100:
    print("OK")
else:
    최소값 = min(a, b, c)
    if 최소값 == a:
        print("Soongsil")
    if 최소값 == b:
        print("Korea")
    if 최소값 == c:
        print("Hanyang")
