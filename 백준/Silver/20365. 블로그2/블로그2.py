import sys
from io import StringIO

input = sys.stdin.readline
N = int(input())
blog_title = input().strip()

합치기 = ""
for index in range(N):
    if index == 0 or blog_title[index - 1] != blog_title[index]:
        합치기 += blog_title[index]
B의개수 = 합치기.count("B")
R의개수 = 합치기.count("R")

if B의개수 > R의개수:
    print(1 + R의개수)
else:
    print(1 + B의개수)
