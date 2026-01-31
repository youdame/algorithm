import sys
from io import StringIO



input = sys.stdin.readline

A, B = map(int, input().split())



count = 1

while B > A:
    if B % 10 == 1:
        B //= 10
    elif B % 2 == 0: 
        B = B // 2
    else: 
        print(-1)
        break
    count += 1

else:   
    # break 없이 while이 끝났을 때만 실행
    print(count if A == B else -1)