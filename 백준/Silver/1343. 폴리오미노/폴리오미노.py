import sys
from io import StringIO



input = sys.stdin.readline
board = input().strip().split(".")
answer = []

flag = True
for index in range(len(board)):
    if len(board[index]) % 4 == 0:
        answer.append("AAAA" * (len(board[index]) // 4))
    elif len(board[index]) >= 4:
        A숫자 = len(board[index]) // 4
        not_divide = (len(board[index]) - (len(board[index]) // 4) * 4) % 2
        if not_divide != 0:
            flag = False
            print(-1)
            break
        B숫자 = (len(board[index]) - (len(board[index]) // 4) * 4) // 2
        answer.append("AAAA" * A숫자 + "BB" * B숫자)
    elif len(board[index]) % 2 == 0:
        answer.append("BB" * (len(board[index]) // 2))
    else:
        flag = False
        print(-1)
        break

    if index != len(board) - 1:
        answer.append(".")
if flag:
    print("".join(answer))
