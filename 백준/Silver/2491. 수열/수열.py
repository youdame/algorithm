import sys
from io import StringIO
input = sys.stdin.readline


N = int(input())
numbers = list(map(int, input().split()))

max_inc_len = 1
max_dec_len = 1

inc_len = 1
dec_len = 1

for i in range(1, len(numbers)):
    if numbers[i - 1] < numbers[i]:
        inc_len += 1
        dec_len = 1

    elif numbers[i - 1] > numbers[i]:
        dec_len += 1
        inc_len = 1
    else:
        inc_len += 1
        dec_len += 1

    max_dec_len = max(max_dec_len, dec_len)
    max_inc_len = max(max_inc_len, inc_len)
print(max(max_inc_len, max_dec_len))
