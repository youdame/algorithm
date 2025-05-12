
def 약수구하기(num):
    return [ i for i in range(1, num +1 ) if num % i == 0 ]
print(약수구하기(int(input())))


