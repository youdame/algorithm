import sys
input = sys.stdin.readline


n = int(input())
nums = sorted(list(map(int, input().split(" "))))
목표 = int(input())
num_set = set(nums)

count = 0
for num in nums:
  if 목표 - num in num_set:
    count+=1

print(count // 2)
