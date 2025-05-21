import sys


input = sys.stdin.readline


알파벳위치 = [-1] * 26
인풋 = input().strip()

for i in range(len(인풋)):
    if 알파벳위치[ord(인풋[i]) - ord("a")] == -1:
        알파벳위치[ord(인풋[i]) - ord("a")] = i
print(" ".join(map(str, 알파벳위치)))
