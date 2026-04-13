
import math

def calculate_minutes(hours, minutes):
    return hours * 60 + minutes
    
def solution(fees, records):
    기본시간, 기본요금, 단위시간, 단위요금 = fees
    
    def calculate_fee(minutes):
        if minutes <= 기본시간:
            return 기본요금
        
        final_fee = 기본요금

        minutes -= 기본시간

        final_fee += math.ceil(minutes / 단위시간) * 단위요금
        return final_fee
    
    

    cars = dict()
    fee_cars = dict()
    
    total_minutes_car = dict()
    """
    in은 무조건 있음 out은 없을 수 있음 -> 없으면, 23:59 out
    차량번호가 key 나머지는 배열로 넣기 
    
    
    """
    for record in records:
        시간, 차량번호, 내역 = record.split()
        
        if 차량번호 not in cars:
            cars[차량번호] = [시간]
        
        else:
            cars[차량번호].append(시간)
            
    for key, value in cars.items():
        if len(value) % 2 != 0:
            cars[key].append("23:59")

        for index in range(0, len(value), 2):
            출차시간, 입차시간 = (value[index+1], value[index])
            
            hour1, minute1 = map(int, 출차시간.split(":"))
            hour2, minute2 = map(int, 입차시간.split(":"))


            total_minutes = calculate_minutes(hour1, minute1) - calculate_minutes(hour2,minute2)

            if key in total_minutes_car:
                total_minutes_car[key] += total_minutes
            else: 
                total_minutes_car[key] = total_minutes

    
    for key, value in total_minutes_car.items():
        fee_cars[key] = calculate_fee(value)

    answer = []
    
    for key, value in sorted(fee_cars.items(), key = lambda x : x[0]):
        answer.append(value)
    
    return answer