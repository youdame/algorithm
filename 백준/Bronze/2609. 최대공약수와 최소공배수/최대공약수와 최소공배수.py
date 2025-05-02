
def gcd(a, b):
    while b:
        a, b = b, a % b
    return a

def lcm(a, b):
    return (a * b) // gcd(a, b)

a,b = list(map(int,input().split()))
print(gcd(a, b))  # 6
print(lcm(a, b))  # 36
