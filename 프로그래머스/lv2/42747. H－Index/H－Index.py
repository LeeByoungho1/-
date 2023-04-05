def solution(citations):
    answer = 0
    for i in citations:
        l = []
        mx = 0
        for j in citations:
            if j >= i:
                l.append(j)
        mx = len(l)
        if mx > i:
            mx = i
        if mx > answer:
            answer = mx
    return answer