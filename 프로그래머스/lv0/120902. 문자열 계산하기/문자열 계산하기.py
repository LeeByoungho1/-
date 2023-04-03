def solution(my_string):
    a = my_string.split(" ")
    num = 0
    answer = int(a[0])
    for i in range(1,len(a)):
        if i % 2 == 0:
            num = int(a[i])
            if a[i-1] == '+':
                answer += num
            else:
                answer -= num
    return answer