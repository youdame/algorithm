import sys

n = int(input())
이름리스트 = []
for element in sys.stdin:
  나이, 이름 = element.strip().split(" ")
  이름리스트.append((이름, int(나이)))
튜플 = sorted(이름리스트, key = lambda x: x[1])
for 이름, 나이 in 튜플:
  print(나이, 이름)

