def solution(chicken):
    n = 0
    answer = 0
    for i in range(chicken):
        n += 1
        if n == 10:
            n = 1
            answer += 1

    return answer