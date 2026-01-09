import sys
from io import StringIO


input = sys.stdin.readline


warehouse_status = input().strip()

for index in range(10):
    if warehouse_status[index] == "@":
        로봇위치 = index
    if warehouse_status[index] == "#":
        박스위치 = index
    if warehouse_status[index] == "!":
        목표위치 = index

count = 0
if 로봇위치 < 박스위치 < 목표위치:
    count += 박스위치 - 로봇위치 - 1
    count += 목표위치 - 박스위치
    print(count)
elif 로봇위치 > 박스위치 > 목표위치:
    count += 로봇위치 - 박스위치 - 1
    count += 박스위치 - 목표위치
    print(count)
else:
    print(-1)
