def solution(n):
    answer = []
    l = []
    
    for i in range(2, n+1):
        if n % i == 0:
            l.append(i)
    print(l)
    for i in l:
        l2 = []
        for j in range(2,i+1):
            if i % j == 0:
                l2.append(j)
            if len(l2) == 1:
                answer = answer + l2
            # print(answer)
    a = list(set(answer))
    a.sort()
    return a