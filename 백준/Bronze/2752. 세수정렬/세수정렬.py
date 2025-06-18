import sys

input = sys.stdin.readline


answer = list(map(int, input().strip().split(" ")))

print(" ".join(map(str, sorted(answer))))
