import sys

from io import StringIO
import math


parameter = input().strip()


def find_count_to_turn_out_to_all_zero_or_all_one(string):
    count0 = 0
    count1 = 0

    if string[0] == "0":
        count0 += 1
    else:
        count1 += 1

    for i in range(1, len(string)):
        if string[i] != string[i - 1]:
            if string[i] == "0":
                count0 += 1
            else:
                count1 += 1

    return min(count0, count1)


result = find_count_to_turn_out_to_all_zero_or_all_one(parameter)
print(result)
