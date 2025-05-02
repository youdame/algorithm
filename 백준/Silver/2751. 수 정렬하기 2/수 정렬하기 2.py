import sys
n = int(input())

for element in sorted([int(line.strip()) for line in sys.stdin]):
  print(element)

