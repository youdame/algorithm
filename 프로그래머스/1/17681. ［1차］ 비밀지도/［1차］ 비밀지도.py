def binary(num):
    return bin(num)

def solution(n, arr1, arr2):
    result = []
    answer = []
    for i in range(len(arr1)):
        result.append(bin(arr1[i] | arr2[i])[2:].zfill(n))
        answer.append(format_str(result[i]))
    return answer
def format_str(str):
    answer = ""
    for i in str:
        if i == "1":
            answer+= "#"
        else:
            answer+= " "
    return answer