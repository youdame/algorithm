import sys
from io import StringIO

input = sys.stdin.readline
N, Q = map(int, input().split())
input_str = list(input().strip())

for i in range(Q):
    query, l, r = map(int, input().split())

    if query == 1:
        sub_str = list(input_str[l - 1 : r])
        alphabet_buckets = []
        alphabet_bundle = sub_str[0]
        for index in range(1, len(sub_str)):
            if alphabet_bundle[0] == sub_str[index]:
                alphabet_bundle += sub_str[index]
            else:
                alphabet_buckets.append(alphabet_bundle)
                alphabet_bundle = sub_str[index]
        alphabet_buckets.append(alphabet_bundle)
        print(len(alphabet_buckets))
    elif query == 2:
        for index in range(l - 1, r):
            will_change_word = chr(ord(input_str[index]) + 1)
            if will_change_word == "[":
                will_change_word = "A"
            input_str[index] = will_change_word
