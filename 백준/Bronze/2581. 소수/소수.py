import sys
from io import StringIO



M = int(input())
N = int(input())

def is_prime(num):
    for i in range(2, int(num**0.5)+1):
        if num % i == 0:
            return False
    return True
            
        
        
min_value = 1e9
total_sum = 0
for num in range(M, N+1):
    if num == 1:
        continue
    if is_prime(num):
        min_value = min(min_value, num)
        total_sum += num
if total_sum > 0:
    print(total_sum)
    print(min_value)
else:
    print(-1)
