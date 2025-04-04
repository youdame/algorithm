def solution(s):
    arr = s.split(" ")
    arr2 = []

    for word in arr:
        if word == "":
            arr2.append("")  # 공백 유지
        else:
            arr2.append(word[0].upper() + word[1:].lower())

    return " ".join(arr2)
