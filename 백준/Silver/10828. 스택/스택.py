import sys


input = sys.stdin.readline

count = int(input())

스택= []
for i in range(count):

  명령어 = (input().strip().split(" "))
  if len(명령어) == 2:
    스택.append(명령어[1])
  else:
    if 명령어[0] == "top":
      print(스택[-1] if 스택 else -1)
    elif 명령어[0] == "size":
      print(len(스택))
    elif 명령어[0] == "empty":
      print(0 if len(스택) > 0  else 1)
    elif 명령어[0] == "pop":
      print(스택.pop() if len(스택)  else -1)

    