import sys
input = sys.stdin.readline

n = int(input())



for i in range(n):
  answer = 0
  count = 0
  한줄 = input().strip()
  # print(한줄)
  for j in range(len(한줄)):
    if j == 0 and 한줄[j] == "O" :
      count += 1
    elif 한줄[j] == "X":
      count = 0
    elif 한줄[j] == "O" and 한줄[j-1] == "O":
      count += 1
    elif 한줄[j] == "O" and 한줄[j-1] != "O":
      count = 1
   
    # print("count", count)
    answer += count
  print(answer)
