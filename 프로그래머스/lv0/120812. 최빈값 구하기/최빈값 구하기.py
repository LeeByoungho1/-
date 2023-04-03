def solution(array):
    a = set(array)
    a = list(a)
    l = []
    for i in a:
        l.append(array.count(i))
        
    mx = l[0]
    for i in l:
        if i > mx:
            mx = i
    
    answer = a[l.index(mx)]
    if l.count(mx) > 1:
        answer = -1
    return answer