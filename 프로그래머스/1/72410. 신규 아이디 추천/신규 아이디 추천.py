import re
def solution(new_id):

    # print(new_id)
    # 1단계
    new_id = new_id.lower()
    # print(new_id)
    # 2단계
    new_id = re.sub('[^a-z0-9_.-]', '', new_id)
    # print(new_id)
    # 3단계
    while '..' in new_id:
        new_id = new_id.replace('..', '.')
    # print(new_id)
    
    if new_id.startswith('.'):
        new_id = new_id[1:]
    if new_id.endswith('.'):
        new_id = new_id[:len(new_id)-1]
    # print(new_id)
    
    
    if not new_id:
        new_id += 'a'
    # print(new_id)
    if len(new_id) >= 16:
        new_id = new_id[:15]
    if new_id.endswith('.'):
        new_id = new_id[:len(new_id)-1]
    # print(new_id)
    
    if len(new_id) <= 2:
        while len(new_id) < 3:
            new_id += new_id[-1]
    return new_id