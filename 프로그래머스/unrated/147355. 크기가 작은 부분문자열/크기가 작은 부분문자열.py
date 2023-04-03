def solution(t, p):
    answer = 0
    l = []
   
    for i in range(len(t)-len(p)+1):
        l.append(t[i:i+len(p)])
    for i in l:
        if int(i) <= int(p):
            answer += 1
    
    return answer