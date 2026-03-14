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
    second = 1

    total = (sum(sum(signal) for signal in signals))
    while True:
        if second > total * 50000:
            return -1
        possible = True
        for signal in signals:
            if get_color(second, signal) != 1:
                possible = False
        if possible:
            return second
        second += 1

    
    