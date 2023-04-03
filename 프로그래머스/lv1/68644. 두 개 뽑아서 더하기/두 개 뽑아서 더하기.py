def solution(numbers):

    l = []
    ll = []
    for i in numbers:
        l = numbers.copy()
        l.remove(i)
        for j in l:
            ll.append(i+j)
    ll.sort()
    answer = list(set(ll))
    answer.sort()
    return answer