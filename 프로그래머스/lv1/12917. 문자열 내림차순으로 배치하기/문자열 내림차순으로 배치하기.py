def solution(s):
    answer = ''
    l = list(s)
    l.sort()
    l.reverse()
    for i in l:
        answer += i
    return answer