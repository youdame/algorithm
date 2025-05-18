import sys


input = sys.stdin.readline

입력 = input().strip()


크로아티아알파벳 = ["c=", "c-", "dz=", "d-", "lj", "nj", "s=", "z="]
answer = 0
for 알파벳 in 크로아티아알파벳:
    if 알파벳 in 입력:
        입력 = 입력.replace(알파벳, "*")
answer = 입력.count("*")
입력 = 입력.replace("*", "")
answer += len(입력)

print(answer)
