import sys

from io import StringIO
import math

def 약수구하기(num):
    result = []
    for i in range(1, math.floor(num / 2) + 1):
        if num % i == 0:
            result.append(i)
    return result


while True:
    num = int(input().strip())
    if num == -1:
        break
    약수배열 = 약수구하기(int(num))
    if (sum(약수배열)) == num:
        print(f"{num} = {' + '.join(map(str, 약수배열))}")
    else:
        print(f"{num} is NOT perfect.")
