import sys
from io import StringIO
import math

input = sys.stdin.readline
count = int(input())

숫자배열 = sorted([int(input()) for i in range(count)])

dic = {}


print(round(sum(숫자배열) / len(숫자배열)))

print(숫자배열[len(숫자배열) // 2])


for i in range(len(숫자배열)):
    if 숫자배열[i] in dic:
        dic[숫자배열[i]] += 1
    else:
        dic[숫자배열[i]] = 1

max_num = max(dic.values())

max_count = 0

flag = list(dic.values()).count(max_num) == 1

if flag:
    for key, value in dic.items():
        if value == max_num:
            print(key)
else:
    for key, value in dic.items():
        if value == max_num:
            max_count += 1
            if max_count == 2:
                print(key)
# print(max_num)
print(숫자배열[len(숫자배열) - 1] - 숫자배열[0])
