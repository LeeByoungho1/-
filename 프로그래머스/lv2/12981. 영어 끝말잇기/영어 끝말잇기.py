def solution(n, words):
    answer = [0,0]
    l = [words[0]]
    a1 = 2
    a2 = 1
    for i in range(1,len(words)):
        if words[i-1][-1] == words[i][0] and words[i] not in l:
            a1 += 1
            if a1 > n:
                a1 = 1
                a2 += 1
            l.append(words[i])
        else:
            answer = [a1,a2]
            break
    return answer