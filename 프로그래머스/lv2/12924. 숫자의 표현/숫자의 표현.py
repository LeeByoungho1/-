def solution(n):
    answer = 1
    for i in range(1,n//2+1):
        for j in range(i+1,i+1+n//i):
            if sum(range(i,j)) == n:
                answer += 1
            elif sum(range(i,j)) > n:
                break
    return answer