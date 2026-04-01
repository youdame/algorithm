import sys
from io import StringIO
from collections import defaultdict

input = sys.stdin.readline

N = int(input())

arr = []


for i in range(N):
    arr.append(input().strip())

possible_number = [i for i in range(9, -1, -1)]

weight_record = defaultdict(int)

for word in arr:
    for i in range(len(word)):
        weight_record[word[len(word) - 1-i]] += (10**i)

current_num = 9
answer = 0
for key, value in sorted(weight_record.items(), key= lambda x : x[1], reverse=True):
    answer += current_num * value
    current_num -= 1
print(answer)
    




    








