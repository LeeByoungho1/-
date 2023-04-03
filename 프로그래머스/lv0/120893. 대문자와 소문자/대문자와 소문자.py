def solution(my_string):
    answer = ''
    ll = []
    for i in my_string:
        if i.islower() == True:
            ll.append(i.upper())
        else:
            ll.append(i.lower())
    for i in ll:
        answer += i
    return answer