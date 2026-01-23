import sys
input = sys.stdin.readline

T = int(input())

tri = []
n = 1
while True:
    t = n * (n + 1) // 2
    if t > 1000:
        break
    tri.append(t)
    n += 1

for _ in range(T):
    K = int(input())
    found = 0

    for a in tri:
        for b in tri:
            for c in tri:
                if a + b + c == K:
                    found = 1
                    break
            if found:
                break
        if found:
            break

    print(found)