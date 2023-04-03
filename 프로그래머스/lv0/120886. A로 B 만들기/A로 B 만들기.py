def solution(before, after):
    answer = 0
    a = list(after)
    b = list(before)
    a.sort()
    b.sort()
    r = 0
    for i in range(len(a)):
        if a[i] == b[i]:
            r += 1
    if r == len(a):
        answer = 1
    return answer