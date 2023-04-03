def solution(s):
    answer = []
    l = list(s)
    ll = []
    answer = []
    for i in range(len(l)):
        if l[i] in ll:
            n = abs(l.index(l[i])-i)
            answer.append(n)
            l[l.index(l[i])] = '0'

        else:
            answer.append(-1)
        ll.append(l[i])
    return answer