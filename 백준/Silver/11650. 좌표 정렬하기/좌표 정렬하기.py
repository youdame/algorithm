import sys

n = int(input())
튜플리스트=[]
for line in sys.stdin:
  x , y = (line.strip().split())
  튜플리스트.append((int(x),int(y)))
for x, y in sorted(튜플리스트, key =lambda x :(x[0], x[1])):
  print(x, y)
