import sys


input = sys.stdin.readline

count = int(input())

for i in range(count):
  is_valid = True
  스택=[]
  for j in input().strip():
    if j == "(":
      스택.append(j)
    elif j == ")":
      if len(스택) > 0:
        스택.pop()
      else:
        is_valid = False
        break

  
  if is_valid and not 스택:
    print("YES")
  else:
    print("NO")
      
