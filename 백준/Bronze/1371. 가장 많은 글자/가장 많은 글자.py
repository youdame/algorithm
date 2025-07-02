import sys


input = sys.stdin.readlines


count = [0] * 26
for line in input():
    for element in line.strip():
        if element == " ":
            continue
        count[ord(element) - ord("a")] += 1
for i in range(len(count)):
    if count[i] == max(count):
        print(chr(i + ord("a")), end="")
