def get_minutes(time_str):
    
    hour, minute = map(int, time_str.split(":"))
    return hour * 60 + minute

def is_opening(op_start, op_end, target_time_str):
    
    start_minutes = get_minutes(op_start)
    end_minutes = get_minutes(op_end)
    target_minutes = target_time_str
    if type(target_time_str) == "str":
        target_minutes = get_minutes(target_time_str)
    return start_minutes <= target_minutes <= end_minutes

def solution(video_len, pos, op_start, op_end, commands):

    current_minutes = get_minutes(pos)
    if is_opening(op_start, op_end, current_minutes):
            current_minutes = get_minutes(op_end)
    for command in commands:
        if command == "next":
            current_minutes = get_minutes(video_len) if get_minutes(video_len) - current_minutes < 10 else current_minutes + 10 
        elif command == "prev":
            current_minutes = max(current_minutes - 10, 0)
        if is_opening(op_start, op_end, current_minutes):
            current_minutes = get_minutes(op_end)
            
        print(current_minutes // 60, current_minutes % 60)
    return  (f"{current_minutes // 60 if len(str(current_minutes // 60)) == 2 else "0" + str(current_minutes // 60) }:{current_minutes % 60 if len(str(current_minutes % 60)) == 2 else "0" + str(current_minutes % 60)}")
