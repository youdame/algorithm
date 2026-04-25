from collections import defaultdict
def solution(genres, plays):
    
    n = len(genres)
    genre_play_count = defaultdict(int)
    genre_songs = defaultdict(list) # (재생수, 인덱스)
    
    for i, (g, p) in enumerate(zip(genres, plays)):
        genre_play_count[g] += p
        genre_songs[g].append((p, i))
    
    
    sorted_genres = sorted(genre_play_count.items(), key =lambda x : -x[1] )
    answer = []
    for i in range(len(sorted_genres)):
        songs = sorted(genre_songs[sorted_genres[i][0]], key = lambda x : -x[0])
        answer.extend([idx for [play, idx] in songs[:2]])
    return answer
    