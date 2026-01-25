import sys
input = sys.stdin.readline

S1, S2, S3 = map(int, input().split())

cnt = {}

for i in range(1, S1 + 1):
    for j in range(1, S2 + 1):
        for k in range(1, S3 + 1):
            s = i + j + k
            cnt[s] = cnt.get(s, 0) + 1

max_v = max(cnt.values())
print(min(k for k, v in cnt.items() if v == max_v))