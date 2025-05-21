import sys

input = sys.stdin.readline

B진법수, B = input().strip().split()

char_to_num = {}

# 0~9
for i in range(10):
    char_to_num[str(i)] = i

# A~Z
for i in range(10, 36):
    char_to_num[chr(i + 55)] = i

result = 0
for i in range(len(B진법수)):
    result += char_to_num[B진법수[::-1][i]] * (int(B) ** i)

print(result)
