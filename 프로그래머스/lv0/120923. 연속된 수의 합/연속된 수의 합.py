def solution(num, total):
    answer = []
    for i in range(-1000,1000):
        if total == sum(range(i,i+num)):
            answer = list(range(i,i+num))
    return answer