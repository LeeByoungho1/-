def solution(left, right):
    answer = 0
    numlist = list(range(left,right+1))
    
    for i in numlist:
        l = []
        for j in range(1,i+1):
            if i % j == 0:
                l.append(j)
        if len(l) % 2 == 0:
            answer += i
        else:
            answer -= i
    return answer