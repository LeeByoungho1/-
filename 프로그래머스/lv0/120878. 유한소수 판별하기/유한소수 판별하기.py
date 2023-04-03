def solution(a, b):
    answer = 0
    n = a / b
    le = len(str(n))
    if le > 15:
        answer = 2
    else:
        answer = 1
    return answer