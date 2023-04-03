def solution(my_string, num1, num2):
    answer = ''
    l = list(my_string)
    one = l[num1]
    two = l[num2]
    l[num1] = two
    l[num2] = one
    for i in l:
        answer += i
    return answer