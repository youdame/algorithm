def solution(s):
    dic = { '0':'zero', '1':'one', '2': 'two', '3': 'three', '4': 'four', '5':'five', '6':'six', '7':'seven', '8':'eight', '9':'nine'}
    reversed_dic = {v: k for k, v in dic.items()}
    

    for word, digit in reversed_dic.items():
        s = s.replace(word, digit)

    return int(s)