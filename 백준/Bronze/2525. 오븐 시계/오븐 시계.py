import sys



input = sys.stdin.readline

hour, minutes = list(map(int, input().split()))
소요시간 = int(input())


print((hour + (minutes + 소요시간) // 60) % 24 , (minutes + 소요시간) % 60)