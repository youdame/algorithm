import sys
input = sys.stdin.readline

빼는것=[]
아홉명 = sorted([int(input()) for i in range(9)])
for i in range(len(아홉명)):
  for j in range(i + 1, len(아홉명)):
    if sum(아홉명)- 아홉명[i] - 아홉명[j] == 100:
      for k in range(len(아홉명)):
        if k not in [i, j]:
          print(아홉명[k])
      exit()


