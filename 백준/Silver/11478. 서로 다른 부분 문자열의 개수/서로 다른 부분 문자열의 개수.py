import sys
from io import StringIO


S = input().strip()


sub_S = []
for i in range(len(S)):
    for j in range(len(S) - i):
        sub_S.append(S[j:j+i+1])

print(len(set(sub_S)))