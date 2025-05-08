n = int(input())
answer = -1

# 5kg 봉지를 최대한 써보고, 하나씩 줄여가며 확인
for five in range(n // 5, -1, -1):  
    남은 = n - (five * 5)
    if 남은 % 3 == 0:
        three = 남은 // 3
        answer = five + three
        break

print(answer)
