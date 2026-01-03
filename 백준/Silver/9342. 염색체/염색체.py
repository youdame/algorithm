import sys
from io import StringIO


input = sys.stdin.readline
N = int(input().strip())


def check(염색체):
    # print("염색체", 염색체)
    alphabet = ["A", "B", "C", "D", "E", "F"]

    if 염색체[0] not in alphabet or 염색체[len(염색체) - 1] not in alphabet:
        return False
    if 염색체[0] != "A":
        염색체 = 염색체[1:]
    if 염색체[-1] != "C":
        염색체 = 염색체[: len(염색체) - 1]
    나머지 = ""
    for index in range(len(염색체)):
        if 염색체[index] != 염색체[index - 1]:
            나머지 += 염색체[index]
    if 나머지 != "AFC":
        return False
    return True


for i in range(N):
    염색체 = input().strip()
    print("Infected!" if check(염색체) else "Good")
