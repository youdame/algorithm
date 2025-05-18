
import sys

input = sys.stdin.readline

input_list = list(map(int, input().split(" ")))


if sorted(input_list) == input_list:
    print("ascending")
elif sorted(input_list, reverse=True) == input_list:
    print("descending")
else:
    print("mixed")
