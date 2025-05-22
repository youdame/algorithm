import sys


input = sys.stdin.readline

n = int(input())

people = [tuple(map(int, input().strip().split(" "))) for i in range(n)]

for i in range(len(people)):
    등수 = 1

    for j in range(len(people)):
        if people[i][0] < people[j][0] and people[i][1] < people[j][1]:
            등수 += 1
    print(등수, end=" ")
