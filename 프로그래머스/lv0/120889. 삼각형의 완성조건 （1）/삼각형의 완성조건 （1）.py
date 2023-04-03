def solution(sides):
    mx = sides[0]
    SUM = sides[0]+sides[1]+sides[2]
    for i in sides:
        if mx < i:
            mx = i
    if mx >= (SUM-mx):
        answer = 2
    else:
        answer = 1
    return answer