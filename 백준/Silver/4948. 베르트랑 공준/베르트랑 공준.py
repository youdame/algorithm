import sys
from io import StringIO

input = sys.stdin.readline

MAX = 246912
is_prime = [True] * (MAX + 1) 
is_prime[0] = False
is_prime[1] = False

for i in range(2, int(MAX**0.5)+1):
    if is_prime[i]:
        for j in range(i*i, MAX + 1, i):
            is_prime[j] = False

while True:
    N = int(input())
    
    if N == 0:
        break

    count = 0

    # n
    for j in range(N+1, 2*N+1):
        if is_prime[j]:
            count += 1
    print(count)
            