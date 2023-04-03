def solution(n):
    answer = 0
    if n < 2:
        answer = 1
    elif n < 6:
        answer = 2
    elif n < 24:
        answer = 3
    elif n < 120:
        answer = 4
    elif n < 720:
        answer = 5
    elif n < 5040:
        answer = 6
    elif n < 40320:
        answer = 7
    elif n < 362880:
        answer = 8
    elif n < 3628800:
        answer = 9
    else:
        answer = 10
    return answer