def solution(answers):
    answer = []
    one = [1, 2, 3, 4, 5] * 8000
    two = [2, 1, 2, 3, 2, 4, 2, 5] * 5000
    three = [3, 3, 1, 1, 2, 2, 4, 4, 5, 5] * 4000
    ones = 0
    twos = 0
    threes = 0
    for i in range(len(answers)):
        if one[i] == answers[i]:
            ones += 1
        if two[i] == answers[i]:
            twos += 1
        if three[i] == answers[i]:
            threes += 1
    if ones == max(ones,twos,threes):
        answer.append(1)
    if twos == max(ones,twos,threes):
        answer.append(2)   
    if threes == max(ones,twos,threes):
        answer.append(3)
    return answer