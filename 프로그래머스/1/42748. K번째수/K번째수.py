def solution(array, commands):
    result = []
    for command in commands:
        i, j ,k = command
        arr = sorted(array[i-1:j])
        result.append(arr[k-1])
    return result