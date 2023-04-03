def solution(A,B):
    answer = 0
    A.sort()
    B.sort()
    AB = A + B
    for i in range(len(A)):
        answer += AB[i] *AB[-i-1]
        print(AB[i] ,AB[-i-1])
    return answer