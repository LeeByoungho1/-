def solution(my_string, letter):
    answer = ""
    l = []
    for i in my_string:
        if i != letter:
            l.append(i)
    for i in l:
        answer += i
    return answer