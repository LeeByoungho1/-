def solution(cards1, cards2, goal):
    answer = 'Yes'
    g = goal.copy()
    for i in goal:
        if len(cards1) > 0:
            if i  == cards1[0]:
                cards1.remove(i)
                g.remove(i)
        if len(cards2) > 0:
            if i == cards2[0]:
                cards2.remove(i)
                g.remove(i)
    if len(g) > 0:
        answer = "No"
    return answer