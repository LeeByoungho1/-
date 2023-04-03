def solution(numlist, n):
    l = []
    for i in numlist:
        l.append(abs(n-i))
    ll = l.copy()
    ll.sort()
    lll = []
    for i in ll:
        lll.append(numlist[l.index(i)])
    nn = 0
    m1 = 0
    for i in range(len(lll)):
        if lll[i] == nn:
            lll[i-1] = lll[i] + (n-lll[i]) *2
            if lll[i-1] < lll[i]:
                m1 = lll[i]
                lll[i] = lll[i-1]
                lll[i-1] = m1
        nn = lll[i]
    return lll