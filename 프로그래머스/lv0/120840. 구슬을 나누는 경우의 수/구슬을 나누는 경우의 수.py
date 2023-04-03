def solution(balls, share):
    #   balls!
    # (balls-share)! * share!
    n=1
    for i in range(balls,1,-1):
        n = n * i
    nm=1
    for i in range((balls-share),1,-1):
        nm = nm * i
    m=1
    for i in range(share,1,-1):
        m = m * i
        
        
        
    answer = n / nm /m
    return answer