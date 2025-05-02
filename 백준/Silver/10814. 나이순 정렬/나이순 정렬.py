n = int(input())
members = []

for _ in range(n):
    age, name = input().split()
    members.append((int(age), name))  # 순서대로 저장

# 나이 기준으로 정렬 (파이썬 sort는 안정 정렬 = 순서 보존)
members.sort(key=lambda x: x[0])

for age, name in members:
    print(age, name)
