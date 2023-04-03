def solution(n):
    l = []
    for i in range(1,n+1):
        if n % i == 0:
            l.append(i)
    if len(l) % 2 == 1:
        answer = 1
    else:
        answer = 2
    return answer