def solution(s):
    answer = ''
    l = s.split(" ")
    for i in l:
        ll = list(i)
        for j in range(len(ll)):
            if j == 0:
                answer += ll[j].upper()
            else:
                answer += ll[j].lower()
        answer += " "
    answer = answer[:-1]
    return answer