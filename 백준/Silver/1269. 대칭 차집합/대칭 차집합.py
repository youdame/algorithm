import sys
from io import StringIO


input = sys.stdin.readline

a_count, b_count = list(map(int, input().split()))
a_set = set(map(int, input().split()))
b_set = set(map(int, input().split()))
print(len(a_set - b_set) + len(b_set - a_set))
