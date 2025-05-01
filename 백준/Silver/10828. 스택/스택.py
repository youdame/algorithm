import sys

n = int(sys.stdin.readline())
stack = []

for _ in range(n):
    배열 = sys.stdin.readline().split()
    
    if len(배열) == 2:
        _, b = 배열
        stack.append(int(b))
        continue

    명령 = 배열[0]

    if 명령 == "top":
        print(stack[-1] if stack else -1)
    elif 명령 == "pop":
        print(stack.pop() if stack else -1)
    elif 명령 == "size":
        print(len(stack))
    elif 명령 == "empty":
        print(0 if stack else 1)
