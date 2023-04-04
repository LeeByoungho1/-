def solution(name, yearning, photo):
    answer = []
    for i in photo:
        n = 0
        for j in i:
            if j in name:
                n += yearning[name.index(j)]
        answer.append(n)
    return answer