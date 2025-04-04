def solution(price, money, count):
    i = 0
    필요한돈 = 0
    이용금액 = price
    while i < count: 
        필요한돈 += 이용금액 
        이용금액 += price
        i+=1
    return max(필요한돈 - money, 0)
       