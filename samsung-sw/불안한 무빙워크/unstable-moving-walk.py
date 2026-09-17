import  sys
from collections import deque
# sys.stdin = open("input.txt")

input = sys.stdin.readline



n , k = map(int, input().split())

arr = list(map(int, input().split()))

safety_queue = deque(arr)
person_exist_queue = deque([False] *  (n))


def 회전하기():
    # 회전
    safety_queue.rotate(1)
    person_exist_queue.rotate(1)
    person_exist_queue[n - 1] = False

def 이동하기():
    # 사람 이동하기
    for i in range(n-2, -1, -1 ):
        if person_exist_queue[i] and not (person_exist_queue[i+1] or safety_queue[i+1] == 0):
            person_exist_queue[i]= False
            person_exist_queue[i + 1] =True
            safety_queue[i+1] -= 1


    person_exist_queue[n - 1]= False


def 사람올리기():
    # n번칸에 사람 있으면 내림
    if not person_exist_queue[0] and safety_queue[0] != 0:
        person_exist_queue[0] = True
        safety_queue[0] -= 1


# 하나의 실험 set


count = 0

while True:
    count +=1

    회전하기()
    이동하기()
    사람올리기()
    # print(safety_queue)
    # print(person_exist_queue)

    if safety_queue.count(0) >= k:
        print(count)
        break
"""
if arr에 0의 개수가 k개 이상이면 종료 
아니면 반복 
"""