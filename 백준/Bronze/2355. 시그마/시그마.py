import sys
input = sys.stdin.readline

a, b = list(map(int, input().split(" ")))

start = min(a,b)
end = max(a, b)
total = (end - start + 1) * (start + end) // 2
print(total)