def solution(k, score):
    answer = []
    lank = []
    for i in score:
        if len(lank) > k-1:
            lank.append(i)
            lank.remove(min(lank))
        else:
            lank.append(i)
        answer.append(min(lank))
    return answer