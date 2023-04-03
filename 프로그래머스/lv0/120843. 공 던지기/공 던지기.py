def solution(numbers, k):
    answer = 0
    for i in range(0,k):
        if answer > len(numbers):
            answer = answer-len(numbers)
        answer += 2
    return answer-1