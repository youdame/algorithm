import sys
from io import StringIO

S, P = map(int, input().split())
DNA_str = input().strip()

A, C, G, T = map(int, input().split())

min_count = dict({'A': A, 'C': C, 'G': G, 'T':T})

answer = 0

left = 0
right = P

# 첫 샘플
candidate = DNA_str[left:right]
record = dict({'A': 0, 'C': 0, 'G': 0, 'T': 0})

# 매번 이렇게 for문을 도는 게 아니라 이전 계산 값에서 일부만 수정 
# 문자열 + 슬라이딩 윈도우
for element in candidate:
    record[element] += 1

possible = True
for key, value in record.items(): 
    if min_count[key] > record[key]:
        possible = False
        break

if possible:
    answer += 1
left += 1
right += 1


while right <= S:
    sub_str = DNA_str[left - 1]
    add_str = DNA_str[right - 1]

    record[sub_str] -= 1
    record[add_str] += 1
    
    possible = True
    for key, value in record.items(): 
        if min_count[key] > record[key]:
            possible = False
            break
    
    if possible:
        answer += 1
    left += 1
    right += 1
    

print(answer)
        
    