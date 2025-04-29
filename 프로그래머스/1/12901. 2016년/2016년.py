요일 = ['SUN','MON','TUE','WED','THU','FRI','SAT']
month_days = [31, 29, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31]

def 전체일(a, b) :
    return sum(month_days[:a-1]) + b

def solution(a, b):

    return (요일[(전체일(a,b) + 4) % 7])
    