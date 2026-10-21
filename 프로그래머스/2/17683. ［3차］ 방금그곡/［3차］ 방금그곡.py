"""
1. 조건이 일치하는 음악이 여러 개일 때에는 라디오에서 재생된 시간이 제일 긴 음악 제목을 반환한다. 재생된 시간도 같을 경우 먼저 입력된 음악 제목을 반환한다.
"""

def change(s):
    return (s.replace("C#", "c").replace("D#", "d").replace("F#", "f")
             .replace("G#", "g").replace("A#", "a").replace("B#", "b"))
    
    
def get_minutes(time):
    hour, minute = map(int, time.split(":"))
    
    return hour * 60 + minute
    

def solution(m, musicinfos):
    answer = None
    answer_running_time = -1e9
    
    m = change(m)

    for musicinfo in musicinfos:      
        
        s_time, e_time, title, melody = musicinfo.split(',')
        
        melody = change(melody)
        running_time = get_minutes(e_time) - get_minutes(s_time)
        

        running_melody = (melody * (running_time // len(melody) + 1))[:running_time]
        

        if m in running_melody and answer_running_time < running_time:
            answer = title
            answer_running_time = running_time
    return answer if answer else "(None)"