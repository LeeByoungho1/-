def solution(price, money, count):
    answer = 0
    l = []
    for i in range(1,count+1):
        l.append(price*i)
    s = sum(l)
    if s > money:
        answer = s - money
    return answer