import sys
from io import StringIO



input = sys.stdin.readline

arr = (input().split("-"))

answer = sum(map(int,arr[0].split("+")))
for element in arr[1:]:

    answer -= sum(map(int, (element.split("+"))))
print(answer)