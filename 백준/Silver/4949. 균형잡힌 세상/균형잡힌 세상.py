import sys

input = sys.stdin.readline

while True:
    인풋 = input().rstrip()  # rstrip() 사용

    if 인풋 == ".":  # 이제 제대로 비교됨
        break

    arr = []
    flag = True
    for element in 인풋:
        if element == "(" or element == "[":
            arr.append(element)
        elif element == ")":
            if len(arr) > 0 and "(" == arr[-1]:
                arr.pop()
            else:
                flag = False
                break
        elif element == "]":
            if len(arr) > 0 and "[" == arr[-1]:
                arr.pop()
            else:
                flag = False
                break

    print("yes" if flag and len(arr) == 0 else "no")
