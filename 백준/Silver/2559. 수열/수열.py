import sys
from io import StringIO


input = sys.stdin.readline

N, K = list(map(int, input().strip().split(" ")))

arr = list(map(int, input().strip().split(" ")))
psum = []

new_element = sum(arr[:K])
psum.append(new_element)
max = new_element
for i in range(1, len(arr) - K + 1):
    새값 = psum[i - 1] - arr[i - 1] + arr[i + K - 1]
    psum.append(새값)
    if 새값 > max:
        max = 새값
print(max)
