import sys
from io import StringIO
from queue import PriorityQueue


input = sys.stdin.readline

T = int(input())


queue = PriorityQueue()
for i in range(T):
    start, end = list(map(int, input().strip().split(" ")))
    queue.put((start, end))

end = 0
answer = []


while not queue.empty():
    start1, end1 = queue.get()
    if start1 >= end:
        answer.append((start1, end1))
        end = end1

    answer_start, answer_end = answer[-1]
    # print(start1, end1, answer_start, answer_end)

    if end1 < answer_end:
        answer.pop()
        answer.append((start1, end1))
        end = end1
print(len(answer))
# 우선순위 큐?
