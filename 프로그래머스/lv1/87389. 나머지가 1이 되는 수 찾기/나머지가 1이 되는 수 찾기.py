def solution(n):
    
    l = []
    for i in range(1,n+1):
        if n % i == 1:
            l.append(i)
    answer = min(l)
    return answer