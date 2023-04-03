def solution(dots):     
    a = 0
    b = 0
    for i in range(1,4):
        if dots[0][0] == dots[i][0]:
            a = abs(dots[0][1]-dots[i][1])
    for i in range(1,4):
        if dots[0][1] == dots[i][1]:
            b = abs(dots[0][0]-dots[i][0])
    answer = a * b
    return answer