def solution(X, Y):
    answer = '-1'
    x = list(X)
    y = list(Y)
    s = list(set(X) & set(Y))
    l = []
    if len(s) > 0:
        answer = ''
        for i in s:
            mi = x.count(i)
            if mi > y.count(i):
                mi = y.count(i)
            for j in range(mi):
                l.append(i)
        l.sort(reverse=True)
        for i in l:
            answer += i
        if answer[0] == '0':
            answer = '0'
    return answer