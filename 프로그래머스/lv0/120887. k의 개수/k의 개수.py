def solution(i, j, k):
    answer = 0
    l = []
    for num in range(i,j+1):
        l = list(map(int,str(num)))
        for i in l:
            if i == k:
                answer += 1
    return answer