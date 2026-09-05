
from collections import defaultdict 
from bisect import bisect_left
def solution(info, query):
    db = defaultdict(list)    
    
    
    
    
    for each_info in info:
        each_splited_info = each_info.split(" ")

        
        
        result = []
        def backtrack():
            if len(result) == 4:
                db["".join(result)].append(int(each_splited_info[4]))
                return 
            curr_value = each_splited_info[len(result)]
            for value in (curr_value, "-"):
                result.append(value)
                backtrack()
                result.pop()
        backtrack()
        
        
    result = []
    

    for key in db:
        db[key].sort()
    for each_query in query:
        key, cote = "".join(each_query.split(" and ")).split(" ")
        
        values = db[key]
        # print(values)
        count = 0
        idx = bisect_left(values, int(cote))
        result.append(len(values) - idx)
        
    return result
        