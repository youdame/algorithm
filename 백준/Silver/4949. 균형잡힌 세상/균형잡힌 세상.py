import sys

input = sys.stdin.readline
while True:
    한줄 = input().rstrip()
    stack = []
    flag = True
    if 한줄 == ".":
        break
    for 한글자 in 한줄:
        if 한글자 == "(" or 한글자 == "[":
            stack.append(한글자)
        elif 한글자 == ")":
            if len(stack) > 0 and stack[-1] == "(":
                stack.pop()
            else:
                flag = False
                break
        elif 한글자 == "]":
            if len(stack) > 0 and stack[-1] == "[":
                stack.pop()
            else:
                flag = False
                break


    print("yes" if len(stack) == 0 and flag else "no")
