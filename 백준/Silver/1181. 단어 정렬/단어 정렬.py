import sys
n = int(input())

for element in sorted(set([line.strip() for line in sys.stdin]), key = lambda x: (len(x),x)):
  print(element)

