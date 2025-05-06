import sys
input = sys.stdin.readline


n , m = list(map(int, input().split(" ")))

nums = list(map(int, input().split(" ")))

#print(nums)
answer = 0
for i in range(n):
  for j in range(i + 1 , n):
    for k in range(j + 1 ,n):
      세개합 = nums[i] + nums[j] + nums[k]
      if 세개합 <= m:
        answer = max(answer, 세개합)
print(answer)
        