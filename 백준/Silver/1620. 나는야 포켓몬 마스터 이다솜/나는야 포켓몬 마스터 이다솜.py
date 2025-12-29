import sys
from io import StringIO



input = sys.stdin.readline

포켓몬수, 문제개수 = list(map(int, input().split()))

dict1 = {}
dict2 = {}
for i in range(포켓몬수):
    포켓몬 = input().strip()
    dict1[포켓몬] = i + 1
    dict2[i + 1] = 포켓몬
for i in range(문제개수):
    입력 = input().strip()
    if 입력.isdigit():
        print(dict2[int(입력)])
    else:
        print(dict1[입력])
