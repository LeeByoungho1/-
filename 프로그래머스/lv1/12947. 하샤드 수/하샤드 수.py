def solution(x):
    answer = False
    l = list(str(x))
    n = 0
    for i in l:
        n += int(i)
        
    if x % n == 0:
        answer = True
    return answer