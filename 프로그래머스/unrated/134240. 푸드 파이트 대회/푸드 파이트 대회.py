def solution(food):
    answer = ''
    for i in range(1,len(food)):
        for j in range(food[i]//2):
            answer += f'{i}'
    answer = answer + '0' + answer[::-1]
    return answer