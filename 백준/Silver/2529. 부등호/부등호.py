import sys 
from io import StringIO
from itertools import permutations

input = sys.stdin.readline

k = int(input())

arr = list(input().strip().replace(" ", ""))


answer = []

for permutation in permutations(list(range(0, 10)), k+1):  
    possible = True
    for index in range(len(arr)):
        if arr[index] == "<":
            if permutation[index] > permutation[index+1]:
                possible = False
                break
        else:
            if permutation[index] < permutation[index+1]:
                possible = False
                break
    if not possible:
        continue
    if possible:
        answer.append(permutation)
print("".join(map(str, answer[-1])), "".join(map(str, answer[0])))
        

