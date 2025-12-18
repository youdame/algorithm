import sys

input = sys.stdin.readline

arr = [-1] * 26
인풋 = input().strip()
for index in range(len(인풋)):
    if arr[(ord(인풋[index]) - ord("a"))] != -1:
        continue
    arr[(ord(인풋[index]) - ord("a"))] = index

print(" ".join(map(str, arr)))
