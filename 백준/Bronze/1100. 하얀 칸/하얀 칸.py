import sys



input = sys.stdin.readline

count = 0
for i in range(8):
    inputs = input().strip()
    for j in range(len(inputs)):
        if (i + j) % 2 == 0 and inputs[j] == "F":
            count += 1
print(count)
