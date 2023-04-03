def solution(n):
    answer = []
    l = list(str(n))
    l.reverse()
    for i in l:
        answer.append(int(i))
    return answer