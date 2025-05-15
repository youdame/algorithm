import sys

input = sys.stdin.readline

count = int(input())

큐= []
for i in range(count):
  명령어 =  input().strip().split(" ")
  if len(명령어) == 2:
    큐.append(int(명령어[1]))
  else:
    if 명령어[0] == "front":
      print(큐[0] if 큐 else -1)
    elif 명령어[0] == "back":
       print(큐[-1] if 큐 else -1)
    elif 명령어[0] == "size":
      print(len(큐))
    elif 명령어[0] == "empty":
      print(0 if 큐  else 1)
    elif 명령어[0] == "pop":
      if 큐:
        print(큐[0])
        del 큐[0]
      else: 
        print(-1)

    