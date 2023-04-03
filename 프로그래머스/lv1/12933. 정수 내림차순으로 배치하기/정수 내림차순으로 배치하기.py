def solution(n):
    l = list(str(n))
    l.sort()
    l.reverse()
    n = ''
    for i in l:
        n += i
    answer = int(n)   
    return answer