def solution(sides):
    answer = 0
    mx = sides[0]
    if mx < sides[1]:
        mx = sides[1]
    sides.remove(mx)
    mi = sides[0]
    #mx가 가장 긴 변인 경우
    #(mx+1 - min)부터 mx까지의 갯수
    for i in range((mx+1-mi),mx+1):
        answer += 1
    #나머지 한 변이 가장 긴 변인 경우
    #mx+1부터 (mx+min-1)까지의 갯수
    for i in range(mx+1,(mx+mi)):
        answer += 1
    return answer