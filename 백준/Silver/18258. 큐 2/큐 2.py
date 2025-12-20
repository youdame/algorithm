import sys
from io import StringIO
from collections import deque

queue = deque()
input = sys.stdin.readline
N = int(input())


# "push" "pop" "size" "empty" "front" "back"

for i in range(N):
    한줄 = input().strip()
    if 한줄.startswith("push"):
        queue.append(한줄.split(" ")[1])
    elif 한줄 == "pop":
        print(queue.popleft() if queue else -1)
    elif 한줄 == "size":
        print(len(queue))
    elif 한줄 == "empty":
        print(1 if not queue else 0)
    elif 한줄 == "front":
        print(queue[0] if queue else -1)
    elif 한줄 == "back":
        print(queue[-1] if queue else -1)
