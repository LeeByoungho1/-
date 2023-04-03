def solution(s):
    answer = 0
    answer2 = 0
    while s != '1':    
        l = list(s)
        s = bin(l.count('1'))[2:]
        answer2 += l.count('0')
        answer += 1
    l = [answer, answer2]
    return l