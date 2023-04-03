def solution(n):

    l = list(range(1,501))
    for i in l:
        if i % 3 == 0:
            l.remove(i)
    
    ll = []
    for i in l:
        ll.append(str(i))
    
    for i in ll:
        if '3' in i:
            ll.remove(i)
    for i in ll:
        if '3' in i:
            ll.remove(i)
    for i in ll:
        if '3' in i:
            ll.remove(i)
    for i in ll:
        if '3' in i:
            ll.remove(i)
    for i in ll:
        if '3' in i:
            ll.remove(i)
    lll = []       
    for i in ll:
        lll.append(int(i))
    
    answer = lll[n-1] 
    return answer