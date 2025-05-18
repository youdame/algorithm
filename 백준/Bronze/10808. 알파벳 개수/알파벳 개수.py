import sys



input = sys.stdin.readline

인풋 = input().strip()
알파벳빈도 = [0] * 26

for 알파벳 in 인풋:
    알파벳빈도[ord(알파벳) - ord("a")] += 1


print(" ".join(map(str, 알파벳빈도)))
