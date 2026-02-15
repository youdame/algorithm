import sys 
from io import StringIO


input = sys.stdin.readline

psum = [int(input())]



min_value = abs(psum[0] - 100)
min_index = 0

for i in range(1, 10):
    element = psum[i-1] + int(input())
    psum.append(element)

    minus_100 = abs(element - 100)
    if min_value >= minus_100:
        min_value = minus_100
        min_index = i
print(psum[min_index])
        

