def solution(my_string):
    answer = ''
    l = []
    for i in list(my_string):
        if i not in l:
            l.append(i)
    for i in l:
        answer += i
    return answer