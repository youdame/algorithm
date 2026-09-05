K, N = map(int, input().split())

# Please write your code here.


result = []


def backtrack(count):
    if count >= 3:
        return 

    if len(result) == N:
        print(" ".join(map(str, result)))
        return

    for i in range(1, K + 1):
        # 넣기 전에 직전 값(result[-1])과 이번에 넣을 i가 같은지 확인
        if result and result[-1] == i:
            next_count = count + 1
        else:
            next_count = 1  # 새로운 숫자니까 연속 횟수는 1부터 시작!

        result.append(i)
        backtrack(next_count)
        result.pop()


backtrack(0)