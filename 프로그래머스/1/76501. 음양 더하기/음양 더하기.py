def solution(absolutes, signs):
    result = 0
    for i in range(len(absolutes)):
        sign = 1 if signs[i] else -1
        result += absolutes[i] * sign
    return result