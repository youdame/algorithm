
시도횟수 = int(input())
answer = 0
for i in range(시도횟수):
    리스트 = list(map(int, input().strip().split(" ")))
    print(f"#{i+1} {max(리스트)}")

    



