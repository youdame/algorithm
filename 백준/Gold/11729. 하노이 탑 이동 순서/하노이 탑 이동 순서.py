import sys 
from io import StringIO

input = sys.stdin.readline 


N = int(input())


answer = []
def hanoi(count, start, end, aux):
    if count == 1:
        answer.append((start, end))
        return

    hanoi(count-1, start, aux, end)
    answer.append((start, end))
    hanoi(count-1, aux, end, start)
    

hanoi(N, 1, 3, 2)
print(len(answer))
for start, end in answer : 
    print(start, end)