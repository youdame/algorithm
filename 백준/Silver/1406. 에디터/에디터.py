import sys 
from io import StringIO
from collections import deque


input = sys.stdin.readline 


start_txt = input().strip()

M = int(input())

stack1 = deque(list(start_txt))
stack2 = deque([])
for _ in range(M):
    oper_input = input().split()
    oper = oper_input[0]
    if oper == "L" and stack1:
        stack2.appendleft(stack1.pop())
    if oper == "D" and stack2:
        stack1.append(stack2.popleft())
    if oper == "B" and stack1:
        stack1.pop()
    if oper == "P":
        x = oper_input[1]
        stack1.append(x)
print("".join(list(stack1 + stack2)))      