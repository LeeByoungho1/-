def solution(A, B):
    answer = 0
    la = list(A)
    lb = list(B)
    while la != lb:
        la.insert(0,la.pop())
        answer += 1
        if answer > len(la):
            answer = -1
            break    
    return answer