def solution(babbling):
    answer = 0
    jo = ["aya", "ye", "woo", "ma"]
    l = []
    for i in range(len(babbling)):
        l.append('')
    for i in range(len(babbling)):
        for j in jo:
            if j in babbling[i]:
                l[i] += j
                
    for i in range(len(babbling)):
        if len(babbling[i]) == len(l[i]):
            answer += 1
    return answer