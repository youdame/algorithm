import sys
from io import StringIO
from itertools import permutations


input = sys.stdin.readline

N = int(input())
input_arr = []
for i in range(N):
    num, strike, ball = map(int, input().split())
    input_arr.append((list(map(int, str(num))), strike, ball))


def check(permutation, input):
    num, strike, ball = input
    ball = strike + ball

    permutation_strike = 0
    permutation_ball = 0
    for index1 in range(len(num)):
        for index2 in range(len(permutation)):
            if num[index1] == permutation[index2] and index1 == index2:
                permutation_strike += 1
        if num[index1] in permutation:
            permutation_ball += 1
    if permutation_strike == strike and permutation_ball == ball:
        return True
    else:
        return False


count = 0
for permutation in list(permutations([i for i in range(1, 10)], 3)):
    is_answer = True
    for input in input_arr:
        if not check(permutation, input):
            is_answer = False
            break
    if is_answer:
        count += 1
print(count)
