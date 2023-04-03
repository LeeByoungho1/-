def solution(a, b, n):
    answer = 0
    bung = n
    while bung > (a-1):
        answer += b * (bung // a)
        bung = bung - a*(bung // a) + b*(bung // a)
    return answer