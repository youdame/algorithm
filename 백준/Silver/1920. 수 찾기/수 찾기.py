import sys



input = sys.stdin.readline

여기서찾기_list_count = int(input())

여기서찾기 = (set(map(int, input().split(" "))))

후보들수=int(input())
후보들 = (list(map(int, input().split(" "))))

for element in 후보들:
  if element in 여기서찾기:
    print(1)
  else:
    print(0)