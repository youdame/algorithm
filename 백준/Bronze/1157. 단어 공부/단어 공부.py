import sys
from io import StringIO


input = sys.stdin.readline

word = input()
word = word.upper().strip()
dict = {}
for alphabet in word:
    if alphabet in dict:
        dict[alphabet] += 1
    else:
        dict[alphabet] = 1
max_value = max(dict.values())
count = 0
answer = ""
for key, value in dict.items():
    if value == max_value:
        answer = key
        count += 1
if count > 1:
    print("?")
else:
    print(answer)
