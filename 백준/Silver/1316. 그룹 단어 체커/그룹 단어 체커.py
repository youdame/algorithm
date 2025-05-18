import sys


input = sys.stdin.readline

count = int(input())

answer = 0
for i in range(count):
  단어 = input().strip()
  
  is_group = True
 
  seen = set()
  prev=""
  for 알파벳 in 단어:
    if 알파벳 in seen:
      if 알파벳 != prev:
        is_group = False
        continue
    else:
      prev = 알파벳
      seen.add(알파벳)
    
  answer += is_group
print(answer)
