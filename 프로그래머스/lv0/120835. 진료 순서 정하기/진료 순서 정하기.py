def solution(emergency):
    answer = []
    l = emergency.copy()
    l.sort()
    l = l[::-1]
    print(l)
   
    for j in emergency:
         for i in range(len(l)):
            if l[i] ==j:
                answer.append(i+1)
    return answer