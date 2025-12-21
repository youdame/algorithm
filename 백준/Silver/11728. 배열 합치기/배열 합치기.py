import sys

input = sys.stdin.readline
N, M = list(map(int, input().strip().split(" ")))
arr1 = list(map(int, input().strip().split(" ")))
arr2 = list(map(int, input().strip().split(" ")))

print(" ".join(map(str, sorted(arr1 + arr2))))
