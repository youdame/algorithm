import sys
from io import StringIO

input = sys.stdin.readline
N = int(input().strip())


def check(염색체):
    flag = True
    alphabet = ["A", "B", "C", "D", "E", "F"]

    if 염색체[0] not in alphabet or 염색체[len(염색체) - 1] not in alphabet:
        flag = False
        return flag

    next_alphabet = ["A", "F", "C"]
    alphabet_index = 0
    for index in range(1, len(염색체) - 1):
        if 염색체[index] not in next_alphabet:
            flag = False
            return flag
        # print(염색체[index], next_alphabet[alphabet_index])
        if 염색체[index] == next_alphabet[alphabet_index]:
            continue
        else:
            alphabet_index += 1
        if alphabet_index == 3:
            return False
    return flag


for i in range(N):
    염색체 = input().strip()
    print("Infected!" if check(염색체) else "Good")
