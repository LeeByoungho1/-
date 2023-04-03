def solution(s):
    if len(s) % 2 == 0:
        n = int(len(s) / 2)
        answer = s[n-1:n+1]
    else:
        answer = s[(len(s)//2)]
    return answer