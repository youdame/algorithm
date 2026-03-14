import math

def get_lcm(a, b):
    return a * b // math.gcd(a,b)
def get_color(second, signal):
    g, y, r = signal

    color = (second % sum(signal) )

    if color <= g:
        return 0
    elif color <= g + y:
        return 1
    else:
        return 2
    
def solution(signals):
    period = 1
    for signal in signals:
        period = get_lcm(sum(signal), period)
    
    for second in range(1, period):
        possible = True
        for signal in signals:
            if get_color(second, signal) != 1:
                possible = False
        if possible:
            return second
    return -1

    
    