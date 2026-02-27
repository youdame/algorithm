import sys
from io import StringIO
from collections import deque


input = sys.stdin.readline
N = int(input())

record = []
for _ in range(N):
    record.append(input().split())


queue = deque([])
for element in record:
    if len(element) == 2:
        oper, num = element[0], int(element[1])
        if oper == 'push_front':
            queue.appendleft(num)
        elif oper == 'push_back':
            queue.append(num)
    else:
        oper = element[0]
        if oper == "front":
            print(queue[0] if queue else -1)
        elif oper == "back":
            print(queue[-1]if queue else -1) 
        elif oper == "pop_front":
            print(queue.popleft() if queue else -1)
        elif oper == "pop_back":
            print(queue.pop() if queue else -1)
        elif oper == "empty":
            print(0 if queue else 1)
        elif oper == "size":
            print(len(queue))

        
