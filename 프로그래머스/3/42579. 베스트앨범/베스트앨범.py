from collections import defaultdict
def solution(genres, plays):
    
    n = len(genres)
    genre_record = defaultdict(list)
    for i in range(n): 
        genre_record[genres[i]].append([plays[i], i])
    
    sorted_list = sorted(genre_record.items(), key = lambda x : (-sum([i[0] for i in x[1]])))

    
    answer = []
    
    for genre, music_list in sorted_list:
        music_list.sort(key = lambda x : -x[0])
        if len(music_list) == 1:
            answer.append(music_list[0][1])
        else:
            answer.append(music_list[0][1])
            answer.append(music_list[1][1])
    return (answer)
    