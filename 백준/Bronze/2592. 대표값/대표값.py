import sys

input = sys.stdin.readline

배열 = []
dic = dict()


for i in range(10):
    숫자 = int(input().strip())

    배열.append(숫자)

    if 숫자 in dic:
        dic[숫자] += 1
    else:
        dic[숫자] = 1


print(sum(배열) // 10)

for key, value in dic.items():
    if value == max(dic.values()):
        print(key)
        exit()
