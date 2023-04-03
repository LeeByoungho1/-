def solution(numbers):
    answer = 0
    l = []
    for i in numbers:
        for j in numbers:
            l.append(i*j)
        l.remove(i*i)
    answer = max(l)
    return answer