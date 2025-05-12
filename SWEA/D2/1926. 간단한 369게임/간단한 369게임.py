
시도횟수 = int(input())

for i in range(1, 시도횟수 + 1):
    count = 0
    count += str(i).count("3")
    count += str(i).count("6")
    count += str(i).count("9")

    if count > 0:
        print(count * "-", end = " " )
    else:
        print(i , end =" ")

    



