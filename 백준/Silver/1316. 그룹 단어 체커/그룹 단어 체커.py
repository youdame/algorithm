import sys

input = sys.stdin.readline

count = int(input())

answer = 0
for i in range(count):
  단어 = input().strip()
  
  그룹단어여부 = True
 
  알파벳집합 = set()

  for j in range(len(단어)):
    # print(j)
    if 단어[j] in 알파벳집합 and len(단어) != 1:
      if 단어[j] != 단어[j-1]:
        그룹단어여부 = False
    else:
      알파벳집합.add(단어[j])
    # print(그룹단어여부)
  answer += 그룹단어여부
print(answer)
