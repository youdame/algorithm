def solution(n):
    answer = n
    while n > 0:
        answer += n % 10
        n = n // 10

    return answer


for i in sorted(
    list(
        set([i for i in range(1, 10000)]) - set([solution(i) for i in range(1, 10000)])
    )
):
    print(i)
