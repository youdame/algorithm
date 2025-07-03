import sys



input = sys.stdin.readline

개수 = int(input())
dic = dict()
for i in range(개수):
    첫글자 = input().strip()[0]
    dic[첫글자] = dic.get(첫글자, 0) + 1

result = ""
for key, value in dic.items():
    if value >= 5:
        result += key
if result == "":
    print("PREDAJA")
else:
    print("".join(sorted(result)))
