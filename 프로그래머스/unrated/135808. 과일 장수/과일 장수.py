def solution(k, m, score):
    answer = 0
    score.sort(reverse=True)
    n = len(score) % m
    for i in range(n):
        score.pop()
    for i in range(len(score)):
        if i % m == 0:
            answer += score[i-1] * m
    return answer