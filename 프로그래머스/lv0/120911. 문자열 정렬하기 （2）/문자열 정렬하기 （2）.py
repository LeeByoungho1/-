def solution(my_string):
    answer =''
    l = list(my_string.lower())
    l.sort()
    for i in l:
        answer += i
    return answer