def solution(score):
    answer = []
    l = []
    for i in score:
        l.append((i[0]+i[1]) / 2)
    ll = l.copy()
    ll.sort(reverse=True)
    for i in l:
        answer.append(ll.index(i)+1) 
    return answer