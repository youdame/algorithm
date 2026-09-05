def solution(files):

    arr = []
    for j in range(len(files)):
        file_name = files[j]
        n = len(file_name)
        start = 0
        end = n
        for i in range(n):
            each_value = file_name[i]
            
            if start == 0:
                if each_value.isdigit():
                    start = i
            else:
                if not each_value.isdigit():
                    end = i
                    break
        arr.append((file_name[:start], file_name[start:end], file_name[end:]))

    arr.sort(key = lambda x : (x[0].lower(), int(x[1])))
    # print(arr)
    
    
    arr = [a + b + c for a,b,c in arr]
    return arr