def solution(num, k):
    a = [-1]
    l = list(str(num))
    for i in range(len(l)):
        if int(l[i]) == k:
            a.append(i+1)
    if len(a) > 1:
        answer = a[1]
    else:
        answer = a[0]
    return answer