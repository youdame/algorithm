def 이진변환(num):
    배열 = []
    숫자 = num
    while 숫자 > 0:
        배열.append(str(숫자 % 2)) 
        숫자 //= 2 
    return 배열[::-1]

def 영제거함수(arr): 
    removed_zero_list = [element for element in arr if element != '0']
    제거된영개수 = (len(arr) - len(removed_zero_list))
    return 제거된영개수, removed_zero_list

def solution(s):
    num_list = list(s)
    removed_zero_num_count = 0
    
    count = 0
    
    while True:
        이번에제거된영개수, removed_zero_list = 영제거함수(num_list) 
        num_list = 이진변환(len(removed_zero_list))
        print(num_list)
        
        removed_zero_num_count += 이번에제거된영개수
        count += 1
        
        if num_list == ['1']:
            break   
    return ([count,removed_zero_num_count ])
    
        
        
