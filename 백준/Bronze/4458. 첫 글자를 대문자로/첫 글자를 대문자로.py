import sys



input = sys.stdin.readline
n = int(input())
for i in range(n):
    문장 = input().strip()
    print(문장[0].upper() + 문장[1:])
