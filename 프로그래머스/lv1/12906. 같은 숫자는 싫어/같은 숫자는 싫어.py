def solution(arr):
    answer = [-1]
    for i in arr:
        if answer[-1] != i:
            answer.append(i)
    answer.remove(-1)
    return answer