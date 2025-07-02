import sys

input = sys.stdin.readline


while True:
    인풋 = input().strip()
    if 인풋 == "END":
        break
    print("".join(list(reversed(인풋))))
